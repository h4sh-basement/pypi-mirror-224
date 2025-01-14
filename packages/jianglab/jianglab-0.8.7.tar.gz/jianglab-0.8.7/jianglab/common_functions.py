import os
from treelib import Tree, Node 
import numpy as np
import McsPy.McsCMOSMEA as McsCMOSMEA
from tqdm import tqdm
import scipy
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import scipy.signal as signal
from tqdm import tqdm
import pickle
import cv2
import xmltodict
import matplotlib.animation as animation
from IPython.display import HTML
import matplotlib
from scipy.fftpack import fft, fftfreq
import seaborn as sns
import optuna
import xgboost as xgb

from sklearn.preprocessing import MinMaxScaler, StandardScaler, FunctionTransformer
from sklearn.metrics import roc_auc_score
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import permutation_importance
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.model_selection import RepeatedStratifiedKFold, cross_val_score, GridSearchCV
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering 

from scipy.cluster import hierarchy 
from scipy.spatial import distance_matrix 
import umap

import warnings
import glob





def frame_ref_to_onset(frame_ref, first_onset_index = 184, visualize_window = (250_000,350_000), stimulus_interval = 60, on_duration = 30, sampling_rate = 20000,overlay_split_num = 5):
    '''
        Convert frame_ref to onset_index
        input:
            frame_ref: 2d array, first row is the light, second row is the frame
            first_onset_index: the index of the first onset, it needs to be manually adjusted
            stimulus_interval: the interval between two stimulus in a unit of frame number
            sampling_rate: the sampling rate of the frame_ref
        output:
            It plots the frame_ref and the onset_index with index number
        return: 
            onset_index: the index of all onsets in a unit of sampling number according to sampling_rate
            off_set_index: the index of all offsets in a unit of sampling number according to sampling_rate
            peaks: the index of all frames in a unit of sampling number according to sampling_rate
            first_onset_index: the index of the first onset
        '''
    plt.rcParams['figure.figsize'] = [30, 5]
    def frame_ref_to_onset_plot(frame_ref = frame_ref, first_onset_index = first_onset_index, stimulus_interval = stimulus_interval, on_duration = on_duration, sampling_rate = sampling_rate, overlay_split_num = overlay_split_num, find_first_onset = True, visualize_window = visualize_window):
        
        prominence = 0.5 * max(frame_ref[1])
        distance = sampling_rate / (stimulus_interval + 10)
        peaks, _ = find_peaks(frame_ref[1], prominence=prominence,distance=distance)
        onset_index = peaks[first_onset_index:][::stimulus_interval] # the index of all onsets in a unit of sampling number according to sampling_rate
        offset_index = peaks[first_onset_index + on_duration:][::stimulus_interval]
        
        # lable the peaks with index number
        scale_factor = max(frame_ref[1])/max(frame_ref[0])
        overlay_factor = 0.03 * max(frame_ref[1]) # to avoid overlap of labels

        if find_first_onset:
            for i, peak in enumerate(peaks):
                if i > 2:
                    plt.text(peak, frame_ref[1][peak]+ i % overlay_split_num * overlay_factor, str(i), fontsize=6)
        
        plt.plot(frame_ref[1])
        plt.plot(frame_ref[0]*scale_factor)
        plt.plot(peaks, frame_ref[1][peaks], "x")
        
        if not find_first_onset:
            plt.plot(onset_index, frame_ref[0][onset_index]*scale_factor, "x")
            plt.plot(offset_index, frame_ref[0][offset_index]*scale_factor, "x")

            for i, onset in enumerate(onset_index):
                if i > 1:
                    plt.text(onset, frame_ref[0][onset]*scale_factor+ i % overlay_split_num * overlay_factor, str(i), fontsize=6)
        if visualize_window[1] != 0:
            plt.xlim(visualize_window)
        plt.show()
        return onset_index, offset_index, peaks, first_onset_index
    
    test_light_ref = frame_ref[:,0:visualize_window[1]]
    frame_ref_to_onset_plot(test_light_ref, first_onset_index=0) # find the first onset index by showing the plot indexed frames from 0
    frame_ref_to_onset_plot(test_light_ref, first_onset_index=first_onset_index, find_first_onset=False) # validate the position of the first onset index by showing the plot indexed frames from first_onset_index
    onset_index, offset_index, peaks, first_onset_index = frame_ref_to_onset_plot(frame_ref, first_onset_index=first_onset_index, find_first_onset=False, visualize_window= (0,0))
    plt.rcdefaults()
    return onset_index, offset_index, peaks, first_onset_index

def get_acquisition_rate(filepath):
    raw_data = McsCMOSMEA.McsData(filepath)
    return 1/(float(raw_data.Acquisition.Sensor_Data.SensorMeta["Tick"])*1e-6) # in Hz

def load_light_ref(filepath, sampling_rate=2000):
    ''' load light reference from .cmcr file
    filepath: path to the .cmcr or .cmtr file
    sampling_rate: sampling rate of the light reference
    '''
    raw_data = McsCMOSMEA.McsData(filepath)
    light_ref = raw_data.Acquisition.Analog_Data.ChannelData_1[:,::sampling_rate]
    return light_ref

def hill(x, L, x0, k, b):
    return L * (x**k) / (x0**k + x**k) + b



def get_on_times_off_times_of_steps(light_ref, height = 5e4, distance = 400, verbose = True):
    on_times, _ = find_peaks(np.diff(light_ref), height = 5e4, distance = 400)
    if verbose:
        print(on_times.shape)
        print(np.diff(on_times))
    off_times, _ = find_peaks(-np.diff(light_ref), height = 5e4, distance = 400)
    if verbose:
        print(off_times - on_times)
    return on_times, off_times

def import_cmtr(filename, light_ref_resample_rate_hz = 100):
    all_units = {"units_data":{}, "meta_data":{}}
    processed = McsCMOSMEA.McsData(filename)
    for unit in tqdm(range(processed.Spike_Sorter.Units.shape[0])):
        data = eval("np.array(processed.Spike_Sorter.Unit_" + str(unit+1)+".get_peaks_timestamps())")
        col = eval("processed.Spike_Sorter.Unit_" + str(unit+1) + ".attributes['Column']")
        row = eval("processed.Spike_Sorter.Unit_" + str(unit+1) + ".attributes['Row']")
        waveform = eval("processed.Spike_Sorter.Unit_" + str(unit+1) + ".get_peaks_cutouts().T.mean(axis=1)")
        all_units["units_data"][str(unit+1)] = {"unitID": unit+1, "data": data, "col": col, "row": row, \
            "waveform": waveform, "filename": filename, "globalID": -1}
    # check if a file exist
    cmcr_file_path = filename[:-6]+".cmcr"
    if os.path.exists(cmcr_file_path):
        acq_rate = get_acquisition_rate(cmcr_file_path)
        all_units["meta_data"]["acq_rate"] = acq_rate
        light_ref_resample_rate = int(acq_rate/light_ref_resample_rate_hz)
        all_units["meta_data"]["light_ref"] = load_light_ref(cmcr_file_path, light_ref_resample_rate)
    else:
        all_units["meta_data"]["acq_rate"] = None
        all_units["meta_data"]["light_ref"] = None
    return all_units

def event_rate_in_interval(timestamps, length, interval):
    bins = np.arange(0, length, interval)
    hist, _ = np.histogram(timestamps, bins=bins)
    event_rate = hist / interval *1_000_000
    return event_rate

def load_raw_data(filepath):
    ''' load raw data from .cmcr or .cmtr file
    filepath: path to the .cmcr or .cmtr file'''
    raw_data = McsCMOSMEA.McsData(filepath)
    return raw_data



def cmcr_to_nparray(filepath):
    data = McsCMOSMEA.McsData(filepath)
    data = np.array(data.Acquisition.Sensor_Data.SensorData_1_1)
    return data

def import_cmtr_firing_rate(filename, bin_size = 100): 
    """Import a .cmtr file and return a dictionary of units holding the timestamps and waveforms.
    :param filename: The path to the .cmtr file.
    :return: A dictionary of units holding the timestamps and waveforms.

    Note: 
    1. This function is used for GUI, where is named as import_cmtr_gui
    2. interval is set to 100ms, which is 10Hz
    3. Time scale of timestamps is in nanoseconds and bin_size is defined in milliseconds
    """
    all_units = {}
    processed = McsCMOSMEA.McsData(filename)

    def event_rate_in_interval(timestamps, length, interval):
        bins = np.arange(0, length, interval)
        hist, _ = np.histogram(timestamps, bins=bins)
        event_rate = hist / interval *1_000_000
        return event_rate

    for unit in tqdm(range(processed.Spike_Sorter.Units.shape[0])):
        data = eval("np.array(processed.Spike_Sorter.Unit_" + str(unit+1)+".get_peaks_timestamps())")
        data = event_rate_in_interval(data, length = processed.attributes["LB.RecordingDuration"], interval=bin_size * 1000) # 100ms interval, 10 hz
        col = eval("processed.Spike_Sorter.Unit_" + str(unit+1) + ".attributes['Column']")
        row = eval("processed.Spike_Sorter.Unit_" + str(unit+1) + ".attributes['Row']")
        waveform = eval("processed.Spike_Sorter.Unit_" + str(unit+1) + ".get_peaks_cutouts().T.mean(axis=1)")
        all_units[str(unit+1)] = {"unitID": unit+1, "data": data, "col": col, "row": row, \
            "waveform": waveform, "filename": filename, "globalID": -1}
    return all_units


def import_cmtr_raw(filename):
    """Import a .cmtr file and return a list of units holding the timestamps and waveforms.
    :param filename: The path to the .cmtr file.
    :return: A list of units holding the timestamps and waveforms.
    """
    all_units = {"units_data":[], "meta_data":[]}
    processed = McsCMOSMEA.McsData(filename)
    for unit in tqdm(range(processed.Spike_Sorter.Units.shape[0])):
        data = eval("np.array(processed.Spike_Sorter.Unit_" + str(unit+1)+".get_peaks_timestamps())")
        col = eval("processed.Spike_Sorter.Unit_" + str(unit+1) + ".attributes['Column']")
        row = eval("processed.Spike_Sorter.Unit_" + str(unit+1) + ".attributes['Row']")
        waveform = eval("processed.Spike_Sorter.Unit_" + str(unit+1) + ".get_peaks_cutouts().T.mean(axis=1)")
        all_units["units_data"].append({"unitID": unit+1, "data": data, "col": col, "row": row, \
            "waveform": waveform, "filename": filename, "globalID": -1})
    all_units["meta_data"].append({"analog":None})
    return all_units


def get_file_list(directory, file_extension=".pkl"):
    """
    Get the list of files with a specific extension in a directory and its subdirectories.
    :param directory: The directory to search for files.
    :param file_extension: The file extension to search for.
    :return: A list of file names with their absolute paths.
    """

    # Create an empty list to store the file names and their absolute paths
    file_list = []
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the absolute path of the file
            abs_path = os.path.abspath(os.path.join(root, file))
            
            # Add the file name and its absolute path to the list
            if file.endswith(file_extension):
                file_list.append( abs_path)

    return file_list

def dict_to_tree(data, parent_id=None, tree=None):
    """
    Convert a dictionary to a tree.
    :param data: The dictionary to convert.
    :param parent_id: The parent node id.
    :param tree: The tree object.
    :return: The tree object.

    # Convert the nested dictionary to a tree structure diagram
    tree = dict_to_tree(nested_dict)

    # Display the tree structure diagram
    tree.show()
    """

    if tree is None:
        tree = Tree()
        root_id = "root"
        tree.create_node(tag="Root", identifier=root_id)
        return dict_to_tree(data, parent_id=root_id, tree=tree)

    for key, value in data.items():
        node_id = f"{parent_id}.{key}" if parent_id else key
        tag = f"{key} ({type(value).__name__}"
        
        if isinstance(value, (list, tuple, np.ndarray)):
            tag += f", length: {len(value)}"
        elif isinstance(value, dict):
            tag += f", length: {len(value)}"
        elif isinstance(value, str):
            tag += f", length: {len(value)}"
            tag += f", value: {value}"
        elif isinstance(value, (int, float)):
            tag += f", value: {value}"
        
        tag += ")"
        
        tree.create_node(tag=tag, identifier=node_id, parent=parent_id)
        
        if isinstance(value, dict):
            dict_to_tree(value, parent_id=node_id, tree=tree)

    return tree

def import_gsheet(sheet_name = "MEA dashboard",
                cred = "./credentials/vibrant-epsilon-169702-467fddc26dfc.json"
                ):

    for i in range(3):# search parent folder
        if not os.path.exists(cred): 
            cred = "." + cred

    scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
    ]
    creds_obj = ServiceAccountCredentials.from_json_keyfile_name(cred, scope)
    client = gspread.authorize(creds_obj)
    sheet = client.open(sheet_name).sheet1.get_all_records()
    df = pd.DataFrame.from_dict(sheet)
    df.to_csv("../gsheet_table.csv", index = False)
    return df

def resample_med(np_array, kernel_size = 101, resample_rate =10): # med filter through first axis
    counter = 0
    out_array = np.zeros_like(np_array)
    for i in tqdm(range(np_array.shape[1])):
        for j in range(np_array.shape[2]):
            counter += 1
            # if counter % 100 == 0:
            #     print(counter, " out of 4225")
            out_array[:,i,j] = signal.medfilt(np_array[:,i,j], kernel_size=kernel_size)
    return out_array[::resample_rate]

def get_lowpass_data(raw_cmcr_data, 
                pre_resample_rate = 100,
                post_resample_rate = 10, 
                kernel_size = 51):
        # total resample 1000 result in 20 Hz acq rate
        # 30 mins processing time for 10 mins data
    np_array = raw_cmcr_data.Acquisition.Sensor_Data.SensorData_1_1
    images = np_array[::pre_resample_rate]
    images = resample_med(images, kernel_size= kernel_size, resample_rate = post_resample_rate) 
    return images

def get_lowpass_data_from_file_path(cmcr_file_path,
                                    pre_resample_rate = 100,
                                    post_resample_rate = 10,
                                    kernel_size = 51,
                                    save_data = False):
    raw_cmcr_data = load_raw_data(cmcr_file_path)
    lowpass_data = get_lowpass_data(raw_cmcr_data, pre_resample_rate=pre_resample_rate,\
                                     post_resample_rate=post_resample_rate, \
                                        kernel_size=kernel_size)
    if save_data:
        save_instance(cmcr_file_path[:-5]+"_lp.npy", lowpass_data)
    return lowpass_data

def remove_bad_lanes(data, bad_lanes): # for low pass filtered data
    if len(bad_lanes) != 0:
        data = np.delete(data, [int(lane)-1 for lane in bad_lanes], axis= 2)
    else:
        pass
    return data

def save_instance(filename, instance):
    with open(filename, "wb") as file_:
        pickle.dump(instance, file_, -1)

def load_instance(filename):
    return pickle.load(open(filename, "rb", -1))

def get_bad_lanes(cmcr_file_path):
    gsheet = import_gsheet()
    bad_lanes = cmcr_file_path.split("\\")[-1].replace("-",".").split(".")[:6]
    bad_lanes = ".".join(bad_lanes)
    bad_lanes = gsheet[gsheet.File_name.str.contains(bad_lanes)]["Bad_lanes"]
    #print(list(bad_lanes))
    if pd.isna(bad_lanes).any():
        bad_lanes = []
        print("No bad lanes found")
    # elif len(bad_lanes) == 1:
    #     bad_lanes = bad_lanes
    elif list(bad_lanes[0]) == "":
        bad_lanes = []
    elif "," not in str(list(bad_lanes)[0]):
        bad_lanes = list(bad_lanes)[0]
        bad_lanes = [bad_lanes]
    else:              
        print(list(bad_lanes)[0])        
        bad_lanes = [int(x) for x in list(bad_lanes)[0].split(",")]
    return bad_lanes

def clean_centers_all_process(arr, neighbour_size = (6,6,6)):
    def find_3d_local_min_general(arr, neighbor_size = (6,6,6)):
        if arr.shape[0] != 0:
            counter = 0
            neighbor_size = np.array(neighbor_size)
            pad =  (neighbor_size/2).astype(np.int32)
            arr_pad = np.pad(arr, ((pad[0],pad[0]), (pad[1],pad[1]), (pad[2],pad[2])), 'constant', constant_values = arr.max())
            arr_pad = arr_pad.astype(np.int32)
            center_list = []
            i_range, j_range, k_range = (arr_pad.shape[0]-pad[0]),(arr_pad.shape[1]-pad[1]),(arr_pad.shape[2]-pad[2])
            #surround_varience = []
            for i in tqdm(range(0, i_range,1), desc="Roughly find 3d local minimal"):
                for j in range(j_range):
                    for k in range(k_range):
                        m,n,p = neighbor_size
                        try:
                            if i >= pad[0] and j >= pad[1] and k >= pad[2]:
                                surround = arr_pad[i+pad[0]-m:i+pad[0]+m,j+pad[1]-n:j+pad[1]+n,k+pad[2]-p:k+pad[2]+p]
                                surround[m, n, p] = surround[m, n, p]+1
                                if np.all(arr_pad[i,j,k] <= surround):
                                    center_list.append([i-pad[0],j-pad[1],k-pad[2]])
                                    counter+=1
                                    # if counter % 100 ==0:
                                    #     print(i-pad[0],j-pad[1],k-pad[2])
                                    #     print(counter)
                                else:
                                    pass
                        except OSError as e:
                            print(e)
            return np.array(center_list)
        else:
            print("Empty input. Detection failed.")
            return np.array([0,0,0])
        
    def remove_close_centers(center_list):
            new_centers = []
            for center in tqdm(center_list, desc="Remove close centers "):
                center_check = True
                for new_center in new_centers[-1000:]:
                    try:
                        if np.abs(new_center[0]-center[0]) <50:
                            distance = np.linalg.norm(center - new_center)
                            if distance > np.sqrt(12) and distance != 0:
                                center_check = center_check and True
                            else:
                                center_check = False
                    except:
                        print("Fail to reduce center counts")
                    
                if center_check == True:
                    new_centers.append(center)
            return np.array(new_centers)

    def remove_centers_close_to_edges(center_list):
        clean_centers = []
        for center in center_list:
            if center.shape != ():
                if center[1] > 2 and center[1] <63 and center [2]>2 and center[2]<63:
                    clean_centers.append(center)
        return np.array(clean_centers)

    def remove_isolated_centers(center_list, lp_data):
            all_check = []
            clean_centers_2 = []
            data_mean, data_std = lp_data.mean(), lp_data.std()
            for center in tqdm(center_list, desc="Remove isolated events "):
                if center[0] > 12:
                    surround = lp_data[center[0]-2:center[0]+3,center[1]-1:center[1]+2, center[2]-1:center[2]+2].copy()
                    surround[:,1,1] = 0
                    presurround = lp_data[center[0]-12:center[0]-7,center[1]-1:center[1]+2, center[2]-1:center[2]+2].copy()
                    presurround[:,1,1] = 0
                    check_surround = (surround.sum()-presurround.sum())/40
                    all_check.append(check_surround)
                    if check_surround < data_mean - 2*data_std: #this is an arbitrary number
                        clean_centers_2.append(center)
            return np.array(clean_centers_2)

    center_list = find_3d_local_min_general(arr, neighbor_size = neighbour_size)
    center_list = remove_close_centers(center_list)
    center_list = remove_centers_close_to_edges(center_list)
    center_list = remove_isolated_centers(center_list, arr)
    return center_list

def clean_cmcr_data(cmcr_file_path,
                    kernel_size = 51,
                    pre_resample_rate = 100,
                    post_resample_rate = 10, neighbour_size = (6,6,6)):
    raw_cmcr_data = load_raw_data(cmcr_file_path)
    acq_rate = get_acquisition_rate(cmcr_file_path)
    pre_resample_rate = int(acq_rate/20_000 * pre_resample_rate)
    post_resample_rate = int(acq_rate/20_000 * post_resample_rate)
    kernel_size = int(acq_rate/20_000 * kernel_size)
    if kernel_size % 2 == 0:
        kernel_size += 1

    lowpass_data = get_lowpass_data(raw_cmcr_data, 
                                    pre_resample_rate=pre_resample_rate, 
                                    post_resample_rate=post_resample_rate, 
                                    kernel_size=kernel_size
                                    )
    bad_lanes = get_bad_lanes(cmcr_file_path)
    clean_data = remove_bad_lanes(lowpass_data, bad_lanes)
    clean_centers = clean_centers_all_process(clean_data, 
                                              neighbour_size = neighbour_size)

    return clean_centers, clean_data


def get_ssvf_center_waveform(lp_data, centers, pre_center_margin = 100, post_center_margin = 800):
    center_waveform = []
    for center in centers:
        if (center[0] > pre_center_margin) and (center[0] < (lp_data.shape[0]-post_center_margin)):
            center_waveform.append(lp_data[(center[0]-pre_center_margin):(center[0]+post_center_margin), center[1], center[2]])
    return np.array(center_waveform)

def ssvf_full_analysis(file_list, 
                       show_plot = True,
                       save_data = True,
                       kernel_size = 51, 
                       pre_resample_rate = 100, 
                       post_resample_rate = 10, 
                       neighbour_size = (6,6,6)):
    for filepath in file_list:
        print(filepath)
        centers, lp_data = clean_cmcr_data(filepath,
                                           kernel_size = kernel_size,
                                           pre_resample_rate = pre_resample_rate,
                                           post_resample_rate = post_resample_rate,
                                           neighbour_size = neighbour_size)
        center_waveform = get_ssvf_center_waveform(lp_data, centers)
        data_dict = {"centers":centers, "lp_data":lp_data, "center_waveform":center_waveform}
        if save_data:
            save_instance(filepath[:-5]+".pkl", data_dict)
        if show_plot:
            plt.plot(center_waveform.mean(axis=0))
            plt.show()



def assign_gID_between_two_files(units_ref, unit_to_assign, search_range=1):

    def find_closest_vector_index(reference_vector, vectors):
        """
        Find the closest vector to the reference vector among a list of vectors.
        """
        min_distance = float('inf')
        closest_vector_index = None
        for i,vector in enumerate(vectors):
            distance = np.linalg.norm(reference_vector - vector)
            if distance < min_distance:
                min_distance = distance
                closest_vector_index = i
        return closest_vector_index
    
    used_IDs = []
    for key in unit_to_assign["units_data"].keys():
        assign_data = unit_to_assign["units_data"][key]
        candidate_list = []
        for ref_key in units_ref["units_data"].keys():          
            ref_unit = units_ref["units_data"][ref_key]
            if abs(assign_data["col"] - ref_unit["col"]) < search_range \
            and abs(assign_data["row"] - ref_unit["row"]) < search_range:
                if ref_unit["unitID"] not in used_IDs:
                    candidate_list.append(units_ref["units_data"][ref_key])
        if candidate_list == []:
            unit_to_assign["units_data"][key]["globalID"] = -1
        else:
            waveform_list = [x["waveform"] for x in candidate_list]
            closest_vector_index = find_closest_vector_index(assign_data["waveform"], waveform_list)
            unit_to_assign["units_data"][key]["globalID"] = candidate_list[closest_vector_index]["unitID"]
            used_IDs.append(unit_to_assign["units_data"][key]["globalID"])
    print(used_IDs)
    return unit_to_assign

def fit_ellipse(points):
    # OpenCV's fitEllipse function expects float32 type
    points = points.astype(np.float32)
    # Fit ellipse to points
    ellipse = cv2.fitEllipse(points)
    # Return ellipse parameters
    # Note: the center coordinates are returned as a tuple (x, y)
    # The axes lengths are returned as a tuple (major_axis, minor_axis)
    # The rotation angle is in degrees
    return ellipse

def xml_to_dict(file_path):
    with open(file_path, 'r') as file:
        xml_string = file.read()
    dict_data = xmltodict.parse(xml_string)
    return dict_data

def rotate_point(point, center, angle):
    """
    Rotate a point counterclockwise by a given angle around a given center.

    Args:
        point (tuple): The original point as (x, y).
        center (tuple): The rotation center as (x, y).
        angle (float): The rotation angle in degrees.

    Returns:
        (new_x, new_y): The rotated point's coordinates.
    """
    angle = angle
    angle = np.deg2rad(angle)  # Convert to radians

    original_x, original_y = point
    center_x, center_y = center

    # Shift the point so that the center of rotation is at the origin
    shifted_x = original_x - center_x
    shifted_y = original_y - center_y

    # Perform the rotation
    new_x = shifted_x * np.cos(angle) - shifted_y * np.sin(angle)
    new_y = shifted_x * np.sin(angle) + shifted_y * np.cos(angle)

    # Shift the point back
    new_x += center_x
    new_y += center_y

    return new_x, new_y


def is_point_in_ellipse(point, center, axes, angle):
    """
    Check if a point is within an ellipse.

    Args:
        point (tuple): The point as (x, y).
        center (tuple): The center of the ellipse as (x, y).
        axes (tuple): The lengths of the major and minor axes as (minor, major).
        angle (float): The rotation angle of the ellipse in degrees.

    Returns:
        bool: True if the point is in the ellipse, False otherwise.
    """
    angle = angle
    angle = np.deg2rad(angle)  # Convert to radians
    #swap major and minor axes
    #axes = (axes[1], axes[0]) # to fit the function requirment of major and minor axes order
    # Shift the point to the origin
    shifted_x = point[0] - center[0]
    shifted_y = point[1] - center[1]

    # Rotate the point to align with the coordinate axes
    rotated_x = shifted_x * np.cos(angle) + shifted_y * np.sin(angle)
    rotated_y = -shifted_x * np.sin(angle) + shifted_y * np.cos(angle)

    # Check if the point is in the ellipse
    return (rotated_x / axes[0]) ** 2 + (rotated_y / axes[1]) ** 2 <= 1


def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)

def calculate_shift(image1, image2):
    # Initialize ORB detector
    orb = cv2.ORB_create()

    # Find keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(image1, None)
    kp2, des2 = orb.detectAndCompute(image2, None)

    # Initialize Brute-Force matcher and exclude outliers using RANSAC
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1,des2)

    # Sort matches based on their distance
    matches = sorted(matches, key = lambda x:x.distance)

    # Choose top good matches - this number could be varied
    good = matches[:10]

    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    # Obtain the homography matrix
    M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,1.0)

    # Translation is at the position (2, 0) and (2, 1) in the Homography matrix
    dx, dy = M[0, 2], M[1, 2]
    return dx, dy

def stitch_images_with_shift(img1, img2, shift_x, shift_y):
    # Calculate dimensions of the output image
    rows = max(img1.shape[0], img2.shape[0] + abs(shift_y))
    cols = max(img1.shape[1], img2.shape[1] + abs(shift_x))

    # Create an empty canvas for the output image
    stitched = np.zeros((rows, cols, img1.shape[2]), dtype=np.uint8)
    print(stitched.shape)

    # Place the first image onto the canvas
    stitched[:img1.shape[0], :img1.shape[1]] = img1

    # Place the second image onto the canvas, shifted by the specified amount
    stitched[shift_y : shift_y + img2.shape[0], shift_x : shift_x + img2.shape[1]] = img2

    return stitched


def array_to_video_old(np_array, filename, frame_rate = 30.0, save_to_avi = True, display_inline = True, color_map = 'jet'):
    """
    Converts a 3D numpy array to a video file and displays it in the notebook.
    :param np_array: 3D numpy array
    :param filename: Name of the video file to be saved
    :param save_to_avi: If True, saves the video to an AVI file
    :param color_map: Color map to be used for the video
    :param frame_rate: Frame rate of the video
    """

    # Ensure the array is 3D
    if len(np_array.shape) != 3:
        raise ValueError("Array must be 3-dimensional")

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter(filename, fourcc, frame_rate, (np_array.shape[2], np_array.shape[1]))

    # Create a figure for the plot
    fig = plt.figure()

    # Function to update figure
    def update_fig(i):
        plt.clf()
        plt.imshow(np_array[i], cmap=color_map, vmin=0, vmax=255)  # Assumes array values are in range 0-255

    # Create an animation
    ani = animation.FuncAnimation(fig, update_fig, frames=range(np_array.shape[0]), repeat=False)

    if display_inline:
        # Convert the animation to HTML video tag and display
        display(HTML(ani.to_html5_video()))

    # Write each frame to video file
    if save_to_avi:
        for i in range(np_array.shape[0]):
            frame = np_array[i].astype('uint8')  # Ensure data type is uint8
            out.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))  # OpenCV uses BGR color space

    # Close the video file
    out.release()


def array_to_video(data, filename, min = 0, max =1, cmap = "jet", save_to_avi = True):
    """
    data: 3D numpy array
    filename: Name of the video file to be saved
    save_to_avi: If True, saves the video to an AVI file
    color_map: Color map to be used for the video
    """
    matplotlib.rcParams['animation.embed_limit'] = 2**128
    
    fig, axs = plt.subplots()
    im0 = axs.imshow(data[0], vmin = min, vmax =max, cmap = cmap )

    def init():
        im0.set_data(data[0])

    def animate(i):
        im0.set_data(data[i])

        return im0

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=data.shape[0], repeat = True)
    if save_to_avi:
        anim.save(filename)
    return HTML(anim.to_jshtml())


class human_erg:

    def plot_individual(data,
                    full_view = False,
                    view_20hz = True,  
                    view_2hz = False):
        y = data[:,1]
        y2= data[:,2]
        x = data[:,0]-data[0,0]
        N = data.shape[0]
        T = 1.0/5000 # sampling rate
        yf = fft(y)
        yf2 = fft(y2)

        yf_plot = 2.0/N * np.abs(yf[0:N//2])
        yf_plot = scipy.signal.medfilt(yf_plot, kernel_size = 101)
        yf_plot2 = 2.0/N * np.abs(yf2[0:N//2])
        yf_plot2 = scipy.signal.medfilt(yf_plot2, kernel_size = 101)
        xf = fftfreq(N, T)[:N//2]
        
        if full_view:
            plt.plot(xf, yf_plot, c="red")
            plt.plot(xf, yf_plot2)
            plt.show()

        if view_20hz: 
            plt.plot(xf, yf_plot, c="red")
            plt.plot(xf, yf_plot2)
            plt.xlim((0,20))
            #plt.ylim(0,100*yf_plot2.std())
            plt.show()
            plt.show()

        if view_2hz:
            plt.plot(xf, yf_plot, c="red")
            plt.plot(xf, yf_plot2)
            plt.xlim((0,2))
            #plt.ylim((0,0.01))
            plt.show()

        return xf, yf_plot, yf_plot2

    def plot_individual_subtraction(data,
                                    sampling_rate = 5000,
                                    full_view = False,
                                    view_20hz = True,  
                                    view_2hz = True):
        y_diff = data[:,2]-data[:,1]
        x_diff = data[:,0]-data[0,0]
    
        N_diff = data.shape[0]
        
        T = 1.0/sampling_rate # sampling rate
        yf = fft(y_diff)
        yf_plot = 2.0/N_diff * np.abs(yf[0:N_diff//2])
        yf_plot = scipy.signal.medfilt(yf_plot, kernel_size = 101)
        xf_diff = fftfreq(N_diff, T)[:N_diff//2]

        if full_view:
            plt.plot(xf_diff, yf_plot, c="red")
            #plt.plot(xf_dark, yf_plot2)
            plt.show()

        if view_20hz: 
            plt.plot(xf_diff, yf_plot, c="red")
            #plt.plot(xf_dark, yf_plot2)
            plt.xlim((0,20))
            #plt.ylim(0,100*yf_plot2.std())
            plt.show()

        if view_2hz:
            plt.plot(xf_diff, yf_plot, c="red")
            #plt.plot(xf_dark, yf_plot2)
            plt.xlim((0,2))
            #plt.ylim((0,0.01))
            plt.show()

        return xf_diff, yf_plot


    def batch_ERG_fft_as_npy(file_name_list):
        for file_name in file_name_list:
            data = pd.read_csv(file_name, sep = ",", header = 9)
            data = data.to_numpy()
            print(file_name)
            xf, yf_plot, yf_plot2 = human_erg.plot_individual(data, full_view = False, view_20hz = True, view_2hz = False)

            freq_data = np.array([xf, yf_plot, yf_plot2])
            np.save(file_name[:-4]+"_freq.npy", freq_data)

    def plot_batch_ERG_freq(file_name_list):
        all_freq_data = []
        for file_name in file_name_list:
            freq_data = np.load(file_name)
            xf = freq_data[0,:]
            yf_plot = freq_data[1,:]
            yf_plot2 = freq_data[2,:]
            all_freq_data.append(yf_plot)
            all_freq_data.append(yf_plot2)
            plt.plot(xf, yf_plot, alpha = 0.2)
            plt.plot(xf, yf_plot2, alpha = 0.2)
            plt.xlim((0,2)) # adjust the range of x axis
        
        return xf, all_freq_data
    
    def normalize_all_freq_data(freq_x_axis, all_freq_data, mode = "mean", range = [1.0, 2.0]):
        all_norm_data = []
        for freq_data in all_freq_data:
            range_mask = (freq_x_axis>range[0]) & (freq_x_axis<[range[1]])
            if mode == "mean":
                norm_freq_data = freq_data/np.mean(freq_data[range_mask])
            elif mode == "max":
                norm_freq_data = freq_data/np.max(freq_data[range_mask])
            else:
                print("mode not recognized, use mean or max")
            all_norm_data.append(norm_freq_data)
        return all_norm_data
    


def find_path(filename, dir):
    """
    Find the path of a file in a directory
    param: filename: name of the file
    param: dir: directory to search
    """
    for root, dirs, files in os.walk(dir):
        if filename in files:
            return os.path.join(root, filename)

def find_neighbour_files(filename, dir, neibour_before = 0, neibour_after = 0, include_self = False):
    """
    Find the neighbour files of a file in a directory
    param: filename: name of the file
    param: dir: directory to search
    param: neibour_before: number of files before the file to include
    param: neibour_after: number of files after the file to include
    param: include_self: whether to include the file itself
    """
    file_path = find_path(filename, dir)
    if file_path is None:
        return None
    else:
        file_dir = os.path.dirname(file_path)
        filename_list = os.listdir(file_dir)
        filename_list.sort()
        index = filename_list.index(filename)
        filename_list = filename_list[index-neibour_before:index+neibour_after+1]
        if include_self == False:
            filename_list.remove(filename)
        return [os.path.join(file_dir, f) for f in filename_list]
    
# explore correlation of features
def plot_correlation_map(df, annot = True, format = ".3f", cmap = "coolwarm", upper_triangle = True, x_rotation = 0, y_rotation = 0):
    corr = df.corr()
    if upper_triangle:
        mask = np.triu(corr)
    else:
        mask = None
    ax, fig = plt.subplots(figsize = (10,5))
    sns.heatmap(corr, mask = mask, annot = annot, fmt=format, cmap = cmap)
    plt.xticks(rotation = x_rotation)
    plt.yticks(rotation = y_rotation)
    plt.show()

        

# plot kernel density estimation for each variable
def kde_df(data, grid, figsize=(10,10), fontsize=10):
	x, y = grid[0], grid[1]
	fig, axes = plt.subplots(x, y, figsize = figsize)
	for i, col in enumerate(data.columns):
		ax = axes[i//y, i%y]
		sns.kdeplot(data=data[col], ax=ax, fill=None)
		ax.axvline(data[col].mean(), color='red')
		fig.suptitle('Density function of each features',y = 0.9, fontsize=fontsize)
    #plt.show()

def plot_pairplot(data, hue = "target", figsize=(10,10), pallette = "viridis", size = 80):
    sns.pairplot(data=data, hue =hue, corner=True, plot_kws={'s':size, 'edgecolor':"white", 'linewidth':2.5}, palette=pallette)
    plt.figure(figsize=(10,10))
    plt.show()

def cross_validation(X, y, model_template, n_splits = 10, random_state = 42, n_repeats = 10):
    '''
    X: the training data # X=train_df.drop('target', axis =1) 
                      or # X=train_df[['calc', 'gravity', 'cond']]
    y: the target        # y=train_df['target']
    model_template: a model template, e.g. XGBClassifier(**xgb_params)
    n_splits: number of folds
    random_state: random state
    n_repeats: number of times to repeat the cross validation

    ReapetedStratifiedKFold is used to keep the same distribution of target in each fold
    '''

    kf = RepeatedStratifiedKFold(n_splits = n_splits, random_state = random_state, n_repeats = n_repeats)
    scores = []

    for train_idx, val_idx in kf.split(X, y):
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]
        
        model = model_template.fit(X_train, y_train)
        
        y_pred = model.predict_proba(X_val)
        
        score = roc_auc_score(y_val, y_pred[:, 1])
        scores.append(score)
    
    print(np.array(scores).mean())
    return scores

def xgb_optuna(X, y,params = {}, n_trials = 2, use_GPU = False, cv_splits = 10, cv_repeats = 2, cv_random_state = 42):
    """
        params = {
                'verbosity': 0,

                'n_estimators': trial.suggest_int('n_estimators', 50, 1500),

                'learning_rate': trial.suggest_float('learning_rate', 1e-7, 1e-1),

                'max_depth': trial.suggest_int('max_depth', 3, 20),

                'colsample_bytree': trial.suggest_float('colsample_bytree', 0.1, 1.0),

                'alpha': trial.suggest_float('alpha', 1e-5, 1e2),

                'lambda': trial.suggest_float('lambda', 1e-5, 1e2),

                'objective': 'binary:logistic',

                'eval_metric': 'auc',

                'booster':trial.suggest_categorical("booster", ["dart", "gbtree",'gblinear']),

                'min_child_weight': trial.suggest_int('min_child_weight', 0, 5),
                
            }
    """

    #Xgb modeling and optuna selection of hyperparameters
    optuna.logging.set_verbosity(optuna.logging.WARNING)

    def objective(trial):
        nonlocal params
        if params == {}:
            params = {
                'verbosity': 0,
                'n_estimators': trial.suggest_int('n_estimators', 50, 1500),
                'learning_rate': trial.suggest_float('learning_rate', 1e-7, 1e-1),
                'max_depth': trial.suggest_int('max_depth', 3, 20),
                'colsample_bytree': trial.suggest_float('colsample_bytree', 0.1, 1.0),
                'alpha': trial.suggest_float('alpha', 1e-5, 1e2),
                'lambda': trial.suggest_float('lambda', 1e-5, 1e2),
                'objective': 'binary:logistic',
                'eval_metric': 'auc',
                'booster':trial.suggest_categorical("booster", ["dart", "gbtree",'gblinear']),
                'min_child_weight': trial.suggest_int('min_child_weight', 0, 5),
            }
        if use_GPU:
            params['tree_method'] = 'gpu_hist'
        
        # n_repeats = 2 bc 10 was too long
        model_template = xgb.XGBClassifier(**params)
        scores = cross_validation(X, y, model_template, n_splits = cv_splits, random_state = cv_random_state, n_repeats = cv_repeats)

        return np.mean(scores)


    study = optuna.create_study(direction='maximize')

    #carraying out the optimization
    study.optimize(objective, n_trials=n_trials)
    #get the best parameters
    return study.best_params


def plot_feature_importance(model, X, y, n_repeats = 1, random_state = 42):
    '''
    model: a fitted model # model = XGBClassifier(**xgb_params)
    X: the training data  # X=train_df.drop('target', axis =1)
    y: the target         # y=train_df['target']
    n_repeats: number of times to repeat the permutation importance calculation, it has to be 1
    '''
    def plot_fi(data,ax = None,title = None):
        fi = pd.Series(data, index = X.columns).sort_values(ascending = True)
        fi.plot(kind = 'barh', ax = ax)
        
    model.fit(X, y)
    r = permutation_importance(model, X, y, n_repeats = n_repeats, random_state = random_state)

    fig, axes = plt.subplots(2, 1, figsize=(8,12))
    if model.__class__.__name__ == 'XGBClassifier' or model.__class__.__name__ == 'RandomForestClassifier':
        plot_fi(model.feature_importances_, ax = axes[0])
        plot_fi(model.feature_importances_, ax = axes[0])
    elif model.__class__.__name__ == 'LogisticRegression':
        plot_fi(r['importances'].reshape(X.shape[1],))
        
    plot_fi(r['importances'].reshape(X.shape[1],), ax = axes[1])

    for i in r.importances_mean.argsort()[::-1]:
        print(f"{X.columns[i]:<30} importance: {r.importances_mean[i]:.5f} +/- {r.importances_std[i]:.5f}")
    return {X.columns[i]:r.importances_mean[i] for i in r.importances_mean.argsort()[::-1]}



def random_forest_optuna(X, y,params = {}, n_trials = 2, use_GPU = False, cv_splits = 10, cv_repeats = 2, cv_random_state = 42):
    """
        params = {
                'n_estimators': trial.suggest_int('n_estimators', 50, 1500),
        
                'max_depth': trial.suggest_int('max_depth', 3, 20),
        
                'max_features': trial.suggest_categorical('max_features', ['sqrt', 'log2', None]),
                
                'min_samples_split': trial.suggest_int('min_samples_split', 2, 10),
                
                'min_samples_leaf': trial.suggest_int('min_samples_leaf', 1, 10),
                
                'bootstrap': trial.suggest_categorical('bootstrap', [True, False]),
                
                'criterion': trial.suggest_categorical('criterion', ['gini', 'entropy']),
                
                'class_weight': trial.suggest_categorical('class_weight', [None, 'balanced']),
                
                'random_state': 42
                
            }

        return: best parameters
    """

    #Xgb modeling and optuna selection of hyperparameters
    optuna.logging.set_verbosity(optuna.logging.WARNING)

    def objective(trial):
        nonlocal params
        if params == {}:
            params = {
                'n_estimators': trial.suggest_int('n_estimators', 50, 1500),
                'max_depth': trial.suggest_int('max_depth', 3, 20),
                'max_features': trial.suggest_categorical('max_features', ['sqrt', 'log2', None]),
                'min_samples_split': trial.suggest_int('min_samples_split', 2, 10),
                'min_samples_leaf': trial.suggest_int('min_samples_leaf', 1, 10),
                'bootstrap': trial.suggest_categorical('bootstrap', [True, False]),
                'criterion': trial.suggest_categorical('criterion', ['gini', 'entropy']),
                'class_weight': trial.suggest_categorical('class_weight', [None, 'balanced']),
                'random_state': 42
            }
        if use_GPU:
            params['tree_method'] = 'gpu_hist'

        model_template = RandomForestClassifier(**params)
        scores = cross_validation(X, y, model_template, n_splits = cv_splits, random_state = cv_random_state, n_repeats = cv_repeats)
        return np.mean(scores)

    study = optuna.create_study(direction='maximize')

    #carraying out the optimization
    study.optimize(objective, n_trials=n_trials)
    #get the best parameters
    return study.best_params

def optimize_logistic_regression(X, y, n_splits = 10, n_repeats = 2, random_state = 42):
    """
    X: the training data # X=train_df.drop('target', axis =1)
    y: the target        # y=train_df['target']
    n_splits: number of folds
    random_state: random state
    n_repeats: number of times to repeat the cross validation
    return: best parameters

    Gridsearch was used because of the smaller hyperparameter range
    """
    
    # Gridsearch was used because of the smaller hyperparameter range
    warnings.filterwarnings("ignore")

    # Define the hyperparameters grid
    params = {
        'penalty': ['l1', 'l2', 'elasticnet'],
        'C': [0.001, 0.01, 0.1, 1, 10, 100],
        'class_weight': [None, 'balanced'],
        'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
        'max_iter': [100, 400, 1000]
    }

    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)

    # Create a logistic regression model
    lr = LogisticRegression()

    # Create a stratified k-fold cross-validator
    skf = RepeatedStratifiedKFold(n_splits=n_splits, n_repeats=n_repeats, random_state=random_state)

    # Perform grid search cross-validation
    grid = GridSearchCV(lr, params, cv=skf, scoring='roc_auc', verbose=1, n_jobs=-1)
    grid.fit(X, y)

    # Print the best hyperparameters and the corresponding score
    print('Best score:', grid.best_score_)
    print('Best hyperparameters:', grid.best_params_)

    return grid.best_params_




def plot_elbow_figure(data, max_cluster_num = 11):
    clusters = []

    for i in range(1, max_cluster_num):
        km = KMeans(n_clusters=i).fit(data)
        clusters.append(km.inertia_)
        
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.lineplot(x=list(range(1, max_cluster_num)), y=clusters, ax=ax)
    ax.set_title('Searching for Elbow')
    ax.set_xlabel('Clusters')
    ax.set_ylabel('Inertia')

def plot_kmeans_cluster(X, n_clusters):
    km = KMeans(n_clusters=n_clusters).fit(X)
    X['Labels'] = km.labels_
    plt.figure(figsize=(12, 8))
    sns.scatterplot(X, x ='Income', y='Score', hue=X['Labels'], 
                    palette=sns.color_palette('hls', n_clusters))

    return km.labels_, km

def plot_agglomerative_cluster(X, n_clusters):
    agglom = AgglomerativeClustering(n_clusters=5, linkage='average').fit(X)

    X['Labels'] = agglom.labels_
    plt.figure(figsize=(12, 8))
    sns.scatterplot(X, x ='Income', y='Score', hue=X['Labels'], 
                    palette=sns.color_palette('hls', n_clusters))
    
    return agglom.labels_, agglom

def plot_dendrogram(X, color_threshold = 200, linkage_mode = "average", figsize=(18, 50),leaf_font_size=12, orientation="right"):
    dist = distance_matrix(X, X)
    Z = hierarchy.linkage(dist, linkage_mode)
    fig = plt.figure(figsize=figsize)
    dendro = hierarchy.dendrogram(Z, leaf_font_size=leaf_font_size, orientation=orientation, color_threshold= color_threshold)
    return dendro

def dendrogram_to_scatter(X, dendrogram, umap_seed=42):
    reducer = umap.UMAP(random_state=umap_seed)
    
    X["Labels"] = [x for _,x in sorted(zip([int(n) for n in dendrogram["ivl"]],dendrogram["leaves_color_list"]))]
    data = X.drop(['Labels'], axis=1).values
    scaled_data = StandardScaler().fit_transform(data)
    embedding = reducer.fit_transform(scaled_data)
    
    plot_data = pd.DataFrame(embedding, columns=['umap1', 'umap2'])
    plot_data['Labels'] = X['Labels'].values
    sns.scatterplot(x='umap1', y='umap2', hue='Labels', data=plot_data)

    return plot_data

# def search_file_in_location(location, keyword1, keyword2 ="", recursive=True):
#     """Search for a file in a given location. 
#     If recursive is True, the search will be recursive.
#     search files that contain both keywords in their name."""
#     if recursive:
#         files = glob.glob(location + '/**/*', recursive=True)
#     else:
#         files = glob.glob(location + '/*', recursive=False)
#     files = [f for f in files if keyword1 in f]
#     if keyword2 != "":
#         files = [f for f in files if keyword2 in f]
#     return files

def search_file_in_location(location, keyword_list=[], exclude_list = [], recursive=True, mode = "all"):
    """Search for a file in a given location. 
    If recursive is True, the search will be recursive.
    search files that contain both keywords in their name."""
    if type(keyword_list) == str:
        keyword_list = [keyword_list]
    if type(exclude_list) == str:
        exclude_list = [exclude_list]
    if recursive:
        files = glob.glob(location + '/**/*', recursive=True)
    else:
        files = glob.glob(location + '/*', recursive=False)
    final_files = []
    for file in files:
        if mode == "all":
            if all(keyword in file for keyword in keyword_list):
                final_files.append(file)
        elif mode == "any":
            if any(keyword in file for keyword in keyword_list):
                final_files.append(file)
        else:
            print("mode not recognized, use all or any")

    for exclude_word in exclude_list:

        final_files = [f for f in final_files if exclude_word not in f]
    return final_files