#!/bin/bash

# This script will directly patch the cv2.findContours line in your code
# to fix the "too many values to unpack (expected 2)" error

# Path to your code file
FILE_PATH="/home/jetson/catkin_ws/ws/src/opencv_detection/scripts/new_main.py"

# Make a backup of the original file
cp "$FILE_PATH" "${FILE_PATH}.backup"

# Use sed to replace the problematic line
# Find the line with "contours ,h= cv2.findContours" and replace it with the corrected version
sed -i 's/contours ,h= cv2.findContours(dilate_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)/contours, _ = cv2.findContours(dilate_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)/' "$FILE_PATH"

echo "Fixed cv2.findContours line in $FILE_PATH"
echo "A backup of the original file was created at ${FILE_PATH}.backup"

