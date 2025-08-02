# utils.py
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def compare_images(img1_path, img2_path, output_path='static/output_diff.png'):
    imageA = cv2.imread(img1_path)
    imageB = cv2.imread(img2_path)
    
    imageA_gray = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    imageB_gray = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # Resize both images to same size
    imageB_gray = cv2.resize(imageB_gray, (imageA_gray.shape[1], imageA_gray.shape[0]))

    score, diff = ssim(imageA_gray, imageB_gray, full=True)
    diff = (diff * 255).astype("uint8")

    # Threshold the difference image
    thresh = cv2.threshold(diff, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # Find contours of the differences
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes on the second image
    for c in contours:
        area = cv2.contourArea(c)
        if area > 100:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imwrite(output_path, imageB)

    if score < 0.95:
        return "Tampering Detected", score
    else:
        return "No Tampering Detected", score
