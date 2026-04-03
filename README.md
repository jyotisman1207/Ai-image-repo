# AI Image Processor

This repository documents my journey in **Computer Vision and Image Processing using Python**.

The goal of this project is to build an **AI-based Image Processor** capable of:
- Image Dehazing
- Image Enhancement
- Image Captioning (planned)

---

## 🚀 Features Implemented

### 📌 Basic Image Processing
- Image loading and inspection
- Image as NumPy array
- Image resizing and grayscale conversion

### 📌 Image Enhancement
- Brightness adjustment
- Contrast adjustment
- Histogram analysis
- Histogram equalization
- Gamma correction
- Contrast stretching
- CLAHE (adaptive contrast enhancement)

### 📌 Noise Reduction
- Gaussian blur
- Median filtering

### 📌 Pixel Operations
- Image inversion
- Pixel manipulation

### 📌 Image Transformations
- Rotation
- Flipping

### 📌 Thresholding Techniques
- Binary thresholding
- Adaptive thresholding

### 📌 Morphological Operations
- Erosion
- Dilation

### 📌 Edge Detection
- Canny edge detection

---

## 🌫 Dehazing Pipeline (Core Project)

Implemented a basic image dehazing system using:

- Dark Channel Prior
- Atmospheric Light Estimation
- Transmission Map
- Image Recovery
- Improved Dehazing (with smoothing)

---

## 🧠 Learning Approach

This project is structured as:
- **experiments/** → practical implementation
- **notes/** → concept understanding

This helps in building both **coding skills and theoretical knowledge**.

---

## 🎯 Future Goals

- Improve dehazing quality
- Add transmission refinement
- Implement deep learning based dehazing
- Build image captioning system (CNN + NLP)
---
## 🔥 Final Integrated Pipeline

The project now includes a complete AI pipeline:  

Input Image
->
Image Dehazing (Dark Channel Prior)
->
Feature Enhancement
->
AI Caption Generation (ViT + GPT-2)
->
Output Image + Caption

This combines classical computer vision with deep learning.
---
## 📊 Output

After running the pipeline:

- Dehazed image is saved as:
  - `final_dehazed.jpg`

- Generated caption is saved as:
  - `final_caption.txt`
---
 
## ⭐ Key Highlights

- Built full image dehazing pipeline from scratch  
- Implemented Dark Channel Prior algorithm  
- Integrated deep learning model for captioning  
- Combined classical CV + AI in one system  
- Structured project with experiments and notes  

---

## 👨‍💻 Author

Jyotisman Sahoo  
Building strong fundamentals in Computer Vision 🚀
