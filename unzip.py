import zipfile
import os

# Define paths
zip_path = '/GSMArenaDataset.zip'
extract_to = os.path.splitext(zip_path)[0]  # removes '.zip' to get folder name

# Create the output directory if it doesn't exist
os.makedirs(extract_to, exist_ok=True)

# Extract ZIP
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print(f"Unzipped to: {extract_to}")
