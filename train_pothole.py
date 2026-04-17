from ultralytics import YOLO

# 1. Pre-trained weights load karo (Nano version)
model = YOLO('yolov8n.pt') 

# 2. Model Train karo
results = model.train(
    data='/home/nilesh/Desktop/job/Projects/pothole_project/archive/data.yaml', 
    epochs=25,        # Kitni baar pura data padhna hai
    imgsz=640,       # Image ka size
    batch=16,        # Ek saath kitni images process hongi
    name='my_pothole_model'
)