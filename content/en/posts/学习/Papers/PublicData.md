---
title: "Public Datasets"
date: 2024-05-19T15:01:38+08:00
draft: false
categories:
    - 学习
    - work
    - paper
    - LLMs

libraries:
- katex

enableTocContent: true
---



## ImageNet 

https://image-net.org/data/ILSVRC/2012/ILSVRC2012_img_train.tar

https://image-net.org/challenges/LSVRC/2012/2012-downloads.php

```bash
mkdir train && tar -xvf ILSVRC2012_img_train.tar -C train && for x in `ls train/*tar`; do fn=train/`basename $x .tar`; mkdir $fn; tar -xvf $x -C $fn; rm -f $fn.tar; done
```

整理val到分类文件夹

https://raw.githubusercontent.com/soumith/imagenetloader.torch/master/valprep.sh

## MIMIC-CXR

> https://physionet.org/content/mimic-cxr-jpg/2.1.0/

```bash
# https://github.com/baeseongsu/mimic-cxr-vqa/blob/master/download_images.sh
#!/bin/bash

# This script downloads the MIMIC-CXR-VQA dataset images after gathering image paths from JSON files.

# Capture the start time
start_time=$(date +%s)

# Prompt for PhysioNet credentials
echo "Enter your PhysioNet credentials"
read -p "Username: " USERNAME
read -s -p "Password: " PASSWORD
echo

# Base URL for the MIMIC-CXR dataset
MIMIC_CXR_JPG_DIR="https://physionet.org/files/mimic-cxr-jpg/2.0.0"

# wget parameters for downloading files
WGET_PARAMS="-r -N -c -np --user $USERNAME --password $PASSWORD"

# Function to download files
download() {
    local file_url=$1
    wget $WGET_PARAMS "$file_url" || { echo "Error: Failed to download $file_url" >&2; exit 1; }
}

# Function to extract image paths from JSON files
get_image_paths() {
    local json_file=$1
    python -c "import json; f=open('$json_file'); data=json.load(f); print('\n'.join([item['image_path'] for item in data]))"
}

# Gather image paths from JSON dataset files
image_paths_train=$(get_image_paths 'mimiccxrvqa/dataset/train.json')
image_paths_valid=$(get_image_paths 'mimiccxrvqa/dataset/valid.json')
image_paths_test=$(get_image_paths 'mimiccxrvqa/dataset/test.json')

# Combine paths from train, valid, and test
image_paths=$(echo -e "$image_paths_train\n$image_paths_valid\n$image_paths_test")

# Remove duplicates and convert to an array
readarray -t arr <<<"$(echo "$image_paths" | sort -u)"

# Display the total number of unique images
echo "Total number of unique images: ${#arr[@]}"

# Download the images
echo "Downloading images..."
for image_path in "${arr[@]}"; do
    echo "Downloading $image_path"
    download "$MIMIC_CXR_JPG_DIR/files/$image_path"
done
echo "All images have been successfully downloaded."

# Capture the end time and calculate runtime
end_time=$(date +%s)
runtime=$((end_time - start_time))

# Display the script runtime
echo "Script runtime: $runtime seconds"
```

## ChestX-ray14

> https://www.kaggle.com/datasets/nih-chest-xrays/data

```bash
#!/bin/bash
curl -L -o ~/Downloads/data.zip\
  https://www.kaggle.com/api/v1/datasets/download/nih-chest-xrays/data
```

Data ~45G