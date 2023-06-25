# python version 3.11.2 
# Libraries

import pandas as pd
import numpy as np
import glob
import re
import os

### probability matrix creater ###
def prob_mat(batch):
    # Create a new DataFrame to store the probabilities
    df = pd.DataFrame({'ranges': ['<25', '<50', '<75', '<100', '<125', '<150', '<175', '<200', 
                                '<225', '<250', '<275', '<300']})
    
    file_name = 1
    df_columns = []
    # Loop through the CSV files and calculate the probabilities for each range
    for csv_file in batch:
        # Read the CSV file into a DataFrame
        df1 = pd.read_csv(csv_file)

        bins=[25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300]
        freq = []
        for i in bins:
            # Perform conditional filtering to get values less than the threshold
            filtered_values = df1[df1['Gas Price(Gwei)'] < i]

            # Get the count of filtered values
            count = len(filtered_values)
            freq.append(count)

        # Create a new DataFrame with the column
        new_column = pd.DataFrame({file_name*15: freq})

        # Append the new column to the list
        df_columns.append(new_column)

        # increase the file name by 1
        file_name += 1

    # concatenate the list of columns
    df = pd.concat([df] + df_columns, axis=1)

    # Iterate over the rows of the DataFrame
    for i in range(len(df)):
        for j in range(len(df.columns)):
            if j in [0, 1] : 
                continue
            else:
                # Add previous row's value to the current value
                df.iloc[i, j] += df.iloc[i, j-1]

    # calculate probabilities
    # Iterate over the rows of the DataFrame
    for col in df.columns:
        if col == 'ranges': continue
        # Define the lambda function to divide each value by the last value of the column
        divide_by_last = lambda x: x / df[col].iloc[-1]
        df[col] = df[col].apply(divide_by_last)

    return df

### batch csv reader for training ###
def dt_prep_train(path):
    batch_size = 240

    # Get a list of all CSV files in a directory
    csv_files = glob.glob(path)

    # Sort the list of files based on their modification time in descending order (latest files first)
    sorted_files = sorted(csv_files, key=os.path.getmtime, reverse=True)

    # Select the latest files for last 6 hours
    csv_files = sorted_files[:240*8]

    # sorted list of file names
    csv_files = sorted(csv_files, key=lambda x: (int(re.sub('\D', '', x)), x))

    output_mat = []
    input_mat = []

    # Iterate over the CSV files in batches
    for i in range(0, len(csv_files), 4*15):
        if len(csv_files) < i + batch_size*3:
            break
        # Get the current batch of file paths
        batch_t = csv_files[i:i+batch_size]
        batch_t1 = csv_files[i+batch_size:i+batch_size*2]
        batch_t2 = csv_files[i+batch_size*2:i+batch_size*3]
        df_t = prob_mat(batch_t)
        df_t1 = prob_mat(batch_t1)
        df_t2 = prob_mat(batch_t2)

        # add metrics to input dataset
        input_mat.append([df_t[df_t.columns[1:]].values.T,
                          df_t1[df_t1.columns[1:]].values.T])
        
        # add metrix to output dataset
        output_mat.append(df_t2[df_t2.columns[1:]].values.T)
        
    input_mat = np.array(input_mat) # shape example: (2, 2, 3, 3)
    output_mat = np.array(output_mat) # shape example: (2, 3, 3)

    return input_mat, output_mat


### batch csv reader for predicting ###
def dt_prep_pred(path):
    batch_size = 240
    # Get a list of all CSV files in a directory
    csv_files = glob.glob(path)

    # Sort the list of files based on their modification time in descending order (latest files first)
    sorted_files = sorted(csv_files, key=os.path.getmtime, reverse=True)

    # Select the latest files for last hour
    csv_files = sorted_files[:240*2]

    # sorted list of file names
    csv_files = sorted(csv_files, key=lambda x: (int(re.sub('\D', '', x)), x))

    # probability matrices for last 2 hours
    batch_t = csv_files[0:batch_size]
    batch_t1 = csv_files[batch_size:batch_size*2]
    df_t = prob_mat(batch_t)
    df_t1 = prob_mat(batch_t1)
    pred_input = np.array([df_t[df_t.columns[1:]].values.T,
                           df_t1[df_t1.columns[1:]].values.T])
    return pred_input
