# Camera Calibration using Checkerboard Pattern - GitHub Repository

## Introduction
This repository contains the code for Task 3, which involves camera calibration using a checkerboard pattern. The calibration process aims to provide the full camera matrix (K matrix) along with the top two distortion parameters (k1 and k2). The code utilizes OpenCV for camera calibration.

## Task 3: Camera Calibration (3pt)
### Code Summary
1. **Import Necessary Libraries:**
   - NumPy: For numerical operations.
   - OpenCV: For computer vision tasks.

2. **Define Checkerboard Pattern Size:**
   - Checkerboard pattern size is set as a tuple (6, 9).

3. **Prepare Object Points:**
   - Object points representing 3D coordinates of checkerboard corners in real-world space are prepared.

4. **Initialize Lists for Points:**
   - Lists to store 3D object points and 2D image points are initialized.

5. **Capture Video from the Camera:**
   - Video is captured from the camera (adjust camera index if necessary).

6. **Loop until 'q' key or Checkerboard Corners are Found:**
   - Enter a loop to read frames and convert them to grayscale for corner detection.
   - Use OpenCV to find checkerboard corners in the grayscale frame.
   - If corners are found, store object and image points, draw corners, and display the frame.
   - Check for 'q' key press to exit the loop.

7. **Camera Calibration:**
   - Release the camera and close OpenCV windows.
   - Proceed to camera calibration using collected points.
   - Print camera calibration results (camera matrix and distortion coefficients).

### Code Location
The code for camera calibration using a checkerboard pattern can be found in the file: `Task3_Camera_Calibration.py`

## Usage
1. Clone this repository.
2. Navigate to the root directory.
3. Run the Python script `Checkerboard callibration.py`.

## Author
- Name: Ashiq Rahman Anwar Batcha
