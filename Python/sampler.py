# Packages
import serial
import time
import os
import pandas as pd

# Configuration
port = 'COM3'
csv_file = 'data_log.csv'
log_time = 10
n_samples = 100



# Open the serial port
ser = serial.Serial(port, 9600, timeout=1)

# Initialize an empty list to store the data
data = []

# Start time
start_time = time.time()

# Collect data
for i in range(n_samples):
    # Read a line from the serial port
    line = ser.readline()
    # Decode the line from bytes to string
    value = line.decode('utf-8').strip()
    data.append(value)
    time.sleep( log_time / n_samples ) # Wait for set time between samples

# Close the serial port
ser.close()



# Check if the file exists
if os.path.isfile(csv_file): # File exists
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    df_length = df.shape[1]
    column_index_str = str(df_length + 1)

else: # File does not exist
    df = pd.DataFrame()
    column_index_str = "1"

# Add new data set

df[column_index_str] = data

# Write the DataFrame back to the CSV file
df.to_csv(csv_file, index=False)

# Report
print("-------------------------------------------------------------------")
print("Data entry " + column_index_str + " logged and saved to " + csv_file + " with log time {} seconds and {} samples.".format(log_time, n_samples))
print("-------------------------------------------------------------------")