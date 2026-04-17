# 🛣️ AI Pothole Detection & Reporting System

An end-to-end computer vision web application designed to detect, analyze, and report road potholes in real-time to improve civic infrastructure maintenance. 

### 🚀 Overview
This project bridges advanced machine learning with a robust web backend. It utilizes a custom-trained **YOLOv8** object detection model to identify potholes from images and video feeds, processing the inference through a scalable **Django** backend architecture.

### 🔥 Core Features
- **High-Accuracy Inference:** Leverages Ultralytics YOLOv8 for rapid and precise bounding-box detection of road anomalies.
- **Seamless Web Integration:** A Django-powered interface allowing users to upload media and view processed results instantly.
- **RESTful Architecture:** Clean separation of the inference engine and the web serving layer for potential microservice scaling.
- **Automated Reporting:** Categorizes and logs detection confidence scores into the database for analytics.

### 🛠️ Tech Stack
- **Backend Core:** Python, Django, SQLite/MySQL
- **Computer Vision:** YOLOv8 (Ultralytics), OpenCV, Pandas
- **Frontend:** HTML5, TailwindCSS / Bootstrap
- **Deployment:** Render / Railway (Target Environments)

### ⚙️ Quick Start
```bash
git clone [https://github.com/yourusername/pothole-detection-ai.git](https://github.com/yourusername/pothole-detection-ai.git)
cd pothole-detection-ai
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
