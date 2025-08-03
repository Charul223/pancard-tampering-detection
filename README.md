# PAN Card Tampering Detection Using SSIM and Flask
This project detects tampering in PAN card images using image processing techniques. It compares an original and a possibly tampered image using the Structural Similarity Index (SSIM), highlights the differences, and visualizes the tampered regions. A Flask web app is also included for users to upload and check PAN cards via a browser.

## Features:
- Compares two PAN card images using SSIM.
- Highlights tampered areas using bounding boxes.
- Visualizes: SSIM Score, Difference Image, Threshold Image
- **Flask Web App interface for easy interaction.**

## Technology Stack
- Python (OpenCV, skimage, PIL)
- Structural Similarity Index (SSIM)
- Flask for web interface
- imutils for contour handling

## Workflow:
Step 1: Image Preprocessing
- Download images from URLs or upload via Flask.
- Resize both images to the same dimensions (250x160) for consistency.
- Convert images to grayscale (SSIM works on single-channel).

### Step 2: Image Comparison using SSIM
- Compute SSIM score and generate difference map.
- Higher SSIM (close to 1) = similar images. Lower score = differences.

### Step 3: Highlight Tampered Regions
- Apply thresholding on the difference image.
- Detect contours and draw bounding rectangles around differing areas.

### Step 4: Display Results
- Display original, tampered, diff, and threshold images.
- Flask app visualizes these for user-uploaded images.

##  Running the App Locally
1. Clone the repo:
```bash
git clone https://github.com/your-username/pan-card-tampering.git
cd pan-card-tampering```

2. Install dependencies
```bash
pip install -r requirements.txt

3. Run the app
```bash
python app.py


## Limitations & Future Work
- Works best on aligned images of the same size.
- Could be enhanced using deep learning (e.g., CNN-based forgery detection).
- Add image alignment and noise handling.


