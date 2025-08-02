# app.py
from flask import Flask, render_template, request
from utils import compare_images
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    img1 = request.files['original']
    img2 = request.files['tampered']

    path1 = os.path.join(UPLOAD_FOLDER, 'original.png')
    path2 = os.path.join(UPLOAD_FOLDER, 'tampered.png')

    img1.save(path1)
    img2.save(path2)

    result, score = compare_images(path1, path2)

    return render_template('result.html', result=result, score=round(score, 3), image_path='static/output_diff.png')

if __name__ == '__main__':
    app.run(debug=True)
