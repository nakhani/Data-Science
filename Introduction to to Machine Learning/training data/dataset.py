import os
import numpy as np
import pandas as pd
from PIL import Image

# Directory containing the dataset
dataset_dir = 'Dataset'

# List to store image data and labels
data = []
labels = []

# Loop through each subfolder (0, 1, 2, ..., 9)
for label in range(10):
    label_dir = os.path.join(dataset_dir, str(label))
    for filename in os.listdir(label_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(label_dir, filename)
            image = Image.open(image_path).convert('L')  # Convert to grayscale
            image = image.resize((64, 64))  # Resize image to 64x64 pixels
            image_array = np.array(image).flatten()  # Flatten image to a 1D array
            data.append(image_array)
            labels.append(label)

# Convert lists to NumPy arrays
data = np.array(data)
labels = np.array(labels).reshape(-1, 1)

# Concatenate data and labels
dataset = np.hstack((data, labels))

# Create a DataFrame
df = pd.DataFrame(dataset)
column_names = [f'pixel_{i}' for i in range(data.shape[1])] + ['label']
df.columns = column_names

# Save to CSV
csv_path = 'dataset.csv'
df.to_csv(csv_path, index=False)
print(f"Dataset saved to {csv_path}")
