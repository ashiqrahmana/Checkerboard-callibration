# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 10:40:24 2023

@author: techv
"""

import numpy as np
import cv2

# Define the size of the checkerboard (number of inner corners)
pattern_size = (6, 9)  # Change this to match your checkerboard pattern

# Prepare object points: (0,0,0), (1,0,0), (2,0,0), ..., (5,4,0)
objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)

# Arrays to store object points and image points
obj_points = []  # 3D points in real-world space
img_points = []  # 2D points in image plane

# Capture video from your camera (you may need to adjust the camera index)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)

    # If found, add object points and image points
    if ret:
        obj_points.append(objp)
        img_points.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(frame, pattern_size, corners, ret)
        cv2.imshow('Chessboard', frame)
        cv2.waitKey(0)
        break
    cv2.imshow('Chessboard', frame)
    # cv2.imshow('Chessboard gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()

# Calibrate the camera
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

# Print the camera calibration results
print("Camera Matrix (Intrinsic Parameters):")
print(mtx)
print("\nDistortion Coefficients:")
print(dist)

# Optionally, save the calibration results
np.savez("calibration_data.npz", mtx=mtx, dist=dist)

