import os
import cv2  # OpenCV ka magic!
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from ultralytics import YOLO

# AI Model load karo
model = YOLO('ai_models/best.pt') 

def detector_view(request):
    if request.method == 'POST' and request.FILES.get('road_image'):
        upload = request.FILES['road_image']
        fss = FileSystemStorage()
        
        # 1. User ki photo save karo
        saved_filename = fss.save(upload.name, upload)
        file_path = fss.path(saved_filename)
        
        # 2. YOLO ko chalao par SAVE KARNE SE MANA KAR DO (save=True hata diya)
        results = model.predict(source=file_path)
        
        # 3. YOLO ke dimaag se bounding box wali photo ka array nikal lo
        img_with_boxes = results[0].plot()
        
        # 4. Output file ka naam khud set karo (e.g., ai_abc.jpeg)
        output_filename = "ai_" + saved_filename
        output_path = os.path.join(settings.MEDIA_ROOT, output_filename)
        
        # 5. OpenCV ka use karke khud photo save karo! (100% Bulletproof)
        cv2.imwrite(output_path, img_with_boxes)
        
        # 6. Django ko direct path de do
        output_url = f'/media/{output_filename}'
        
        return render(request, 'dashboard.html', {'result_img': output_url})

    return render(request, 'dashboard.html')