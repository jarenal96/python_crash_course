import os
import glob
from datetime import datetime

def get_latest_file(base_path):
    # Search for the latest subfolder
    subfolders = [f.path for f in os.scandir(base_path) if f.is_dir()]
    latest_folder=max(subfolders,key=os.path.getmtime)

    #Find the latest file in the folder
    files= glob.glob(f"{latest_folder}/*.xlsx")
    latest_file= max(files,key=os.path.getmtime)
    return latest_file

# Example usage
base_path="C:\Documents\Broadway\Project"
latest_file= get_latest_file(base_path)
print(f"Latest file: {latest_file}")

import pandas as pd
def extract_kpi_data(file_path):
    # Read the Excel file (adjust sheet name as needed)
    df = pd.read_excel(latest_file)