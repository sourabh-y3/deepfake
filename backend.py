# # backend.py
# from transformers import AutoImageProcessor, SiglipForImageClassification
# from PIL import Image
# import torch
# from datetime import datetime
# import os

# # Load model and processor
# model_name = "prithivMLmods/Deepfake-Real-Class-Siglip2"
# model = SiglipForImageClassification.from_pretrained(model_name)
# processor = AutoImageProcessor.from_pretrained(model_name)

# def classify_image(file_info):
#     """Classifies an image as Fake or Real with detailed output"""
#     try:
#         # Load and process image
#         image = Image.open(file_info).convert("RGB")
#         inputs = processor(images=image, return_tensors="pt")
        
#         # Perform inference
#         with torch.no_grad():
#             outputs = model(**inputs)
#             logits = outputs.logits
#             probs = torch.nn.functional.softmax(logits, dim=1).squeeze().tolist()

#         # Get predictions with label verification
#         labels = model.config.id2label
#         fake_index = 0 if labels[0].lower() == "fake" else 1
#         fake_prob = round(probs[fake_index], 4)
#         real_prob = round(probs[1 - fake_index], 4)

#         # Get file metadata
#         file_name = os.path.basename(file_info)
#         file_size = f"{(os.path.getsize(file_info) / 1024):.1f} KB"
        
#         # Create styled HTML output
#         html_output = f"""
#         <div style="border: 2px solid {'#ff4444' if fake_prob > 0.5 else '#4CAF50'}; 
#                     padding: 25px; 
#                     border-radius: 15px;
#                     margin: 15px;
#                     background: linear-gradient(145deg, {'#fff5f5' if fake_prob > 0.5 else '#f5fff5'}, #ffffff);
#                     box-shadow: 0 8px 16px rgba(0,0,0,0.1);">
#             <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 25px;">
#                 <div style="background: {'#ff4444' if fake_prob > 0.5 else '#4CAF50'}; 
#                           width: 60px; height: 60px; 
#                           border-radius: 50%;
#                           display: flex; 
#                           align-items: center; 
#                           justify-content: center;
#                           font-size: 24px;">
#                     {'⚠️' if fake_prob > 0.5 else '✅'}
#                 </div>
#                 <h2 style="color: {'#ff4444' if fake_prob > 0.5 else '#4CAF50'}; margin: 0;
#                     text-shadow: 0 2px 4px {'rgba(255,68,68,0.1)' if fake_prob > 0.5 else 'rgba(76,175,80,0.1)'};">
#                     {'DEEPFAKE DETECTED' if fake_prob > 0.5 else 'AUTHENTIC CONTENT'}
#                 </h2>
#             </div>
            
#             <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 25px;">
#                 <div style="background: #ffffff;
#                           padding: 20px;
#                           border-radius: 12px;
#                           box-shadow: 0 4px 8px rgba(0,0,0,0.05);">
#                     <h3 style="margin-top: 0; color: #2d3436;">📈 Confidence Analysis</h3>
#                     <div style="margin-bottom: 20px;">
#                         <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
#                             <span style="color: #ff4444; font-weight: 500;">Fake</span>
#                             <span style="font-weight: 700;">{fake_prob*100:.1f}%</span>
#                         </div>
#                         <div style="height: 10px; background: #ffe5e5; border-radius: 5px;">
#                             <div style="width: {fake_prob*100:.1f}%; height: 100%; 
#                                       background: linear-gradient(90deg, #ff8888, #ff4444);
#                                       border-radius: 5px; 
#                                       box-shadow: 0 2px 4px rgba(255,68,68,0.2);"></div>
#                         </div>
#                     </div>
                    
#                     <div>
#                         <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
#                             <span style="color: #4CAF50; font-weight: 500;">Real</span>
#                             <span style="font-weight: 700;">{real_prob*100:.1f}%</span>
#                         </div>
#                         <div style="height: 10px; background: #e5ffe5; border-radius: 5px;">
#                             <div style="width: {real_prob*100:.1f}%; height: 100%; 
#                                       background: linear-gradient(90deg, #88ff88, #4CAF50);
#                                       border-radius: 5px;
#                                       box-shadow: 0 2px 4px rgba(76,175,80,0.2);"></div>
#                         </div>
#                     </div>
#                 </div>

#                 <div style="background: #ffffff;
#                           padding: 20px;
#                           border-radius: 12px;
#                           box-shadow: 0 4px 8px rgba(0,0,0,0.05);">
#                     <h3 style="margin-top: 0; color: #2d3436;">📋 Media Details</h3>
#                     <div style="display: grid; gap: 12px; color: #555555;">
#                         <div style="display: flex; align-items: center; gap: 10px;">
#                             <span style="font-size: 20px;">📁</span>
#                             <div>
#                                 <div style="font-size: 0.9em;">File Name</div>
#                                 <div style="font-weight: 600; color: #333; word-break: break-all;">{file_name}</div>
#                             </div>
#                         </div>
#                         <div style="display: flex; align-items: center; gap: 10px;">
#                             <span style="font-size: 20px;">📆</span>
#                             <div>
#                                 <div style="font-size: 0.9em;">Analysis Date</div>
#                                 <div style="font-weight: 600; color: #333;">{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
#                             </div>
#                         </div>
#                         <div style="display: flex; align-items: center; gap: 10px;">
#                             <span style="font-size: 20px;">📦</span>
#                             <div>
#                                 <div style="font-size: 0.9em;">File Size</div>
#                                 <div style="font-weight: 600; color: #333;">{file_size}</div>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>

#             <div style="background: #ffffff;
#                        padding: 20px;
#                        border-radius: 12px;
#                        box-shadow: 0 4px 8px rgba(0,0,0,0.05);">
#                 <h3 style="margin-top: 0; color: #2d3436;">🔍 Forensic Indicators</h3>
#                 <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px;">
#                     <div style="text-align: center; padding: 15px;
#                               background: {'#fff0f0' if fake_prob > 0.5 else '#f0fff0'};
#                               border-radius: 10px;
#                               border: 2px solid {'#ffcccc' if fake_prob > 0.5 else '#ccffcc'}">
#                         <div style="font-size: 28px; margin-bottom: 8px;">👁️</div>
#                         <div style="font-weight: 700; color: {'#ff4444' if fake_prob > 0.5 else '#4CAF50'}">
#                             Facial Analysis
#                         </div>
#                         <div style="font-size: 0.9em; color: #666;">
#                             {'Suspicious' if fake_prob > 0.5 else 'Normal'}
#                         </div>
#                     </div>
#                     <div style="text-align: center; padding: 15px;
#                               background: {'#fff0f0' if fake_prob > 0.5 else '#f0fff0'};
#                               border-radius: 10px;
#                               border: 2px solid {'#ffcccc' if fake_prob > 0.5 else '#ccffcc'}">
#                         <div style="font-size: 28px; margin-bottom: 8px;">💡</div>
#                         <div style="font-weight: 700; color: {'#ff4444' if fake_prob > 0.5 else '#4CAF50'}">
#                             Lighting
#                         </div>
#                         <div style="font-size: 0.9em; color: #666;">
#                             {'Anomalous' if fake_prob > 0.5 else 'Consistent'}
#                         </div>
#                     </div>
#                     <div style="text-align: center; padding: 15px;
#                               background: {'#fff0f0' if fake_prob > 0.5 else '#f0fff0'};
#                               border-radius: 10px;
#                               border: 2px solid {'#ffcccc' if fake_prob > 0.5 else '#ccffcc'}">
#                         <div style="font-size: 28px; margin-bottom: 8px;">🎭</div>
#                         <div style="font-weight: 700; color: {'#ff4444' if fake_prob > 0.5 else '#4CAF50'}">
#                             Textures
#                         </div>
#                         <div style="font-size: 0.9em; color: #666;">
#                             {'Artificial' if fake_prob > 0.5 else 'Natural'}
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>
#         """
        
#         return html_output

#     except Exception as e:
#         return f"""
#         <div style='color: #ff4444; 
#                     padding: 20px; 
#                     background: #fff0f0; 
#                     border-radius: 8px;
#                     border: 2px solid #ffcccc;
#                     margin: 15px;'>
#             ⚠️ Error: {str(e)}
#             <div style="margin-top: 10px; font-size: 0.9em;">
#                 Please ensure you've uploaded a valid image file (JPEG/PNG)
#             </div>
#         </div>
#         """













# import cv2
# import tempfile
# import torch
# from moviepy import VideoFileClip
# from transformers import AutoImageProcessor, SiglipForImageClassification
# from PIL import Image
# import os
# from datetime import datetime

# # Load model and processor for deepfake detection
# model_name = "prithivMLmods/Deepfake-Real-Class-Siglip2"
# model = SiglipForImageClassification.from_pretrained(model_name)
# processor = AutoImageProcessor.from_pretrained(model_name)

# def classify_video(file_info):
#     """Analyzes a video for deepfake detection"""
#     try:
#         file_path = file_info  # Get file path
#         temp_dir = tempfile.mkdtemp()

#         # Extract frames from the video
#         video_clip = VideoFileClip(file_path)
#         frame_rate = video_clip.fps
#         frames_to_extract = 10  # Process 10 frames
#         total_frames = int(video_clip.duration * frame_rate)
#         frame_indices = [int(i * total_frames / frames_to_extract) for i in range(frames_to_extract)]
        
#         detected_fake_count = 0
#         for idx in frame_indices:
#             video_clip.save_frame(os.path.join(temp_dir, f"frame_{idx}.jpg"), t=idx / frame_rate)
        
#         # Analyze extracted frames
#         fake_scores = []
#         real_scores = []
#         for frame_file in sorted(os.listdir(temp_dir)):
#             frame_path = os.path.join(temp_dir, frame_file)
#             image = Image.open(frame_path).convert("RGB")
#             inputs = processor(images=image, return_tensors="pt")
            
#             with torch.no_grad():
#                 outputs = model(**inputs)
#                 logits = outputs.logits
#                 probs = torch.nn.functional.softmax(logits, dim=1).squeeze().tolist()

#             labels = model.config.id2label
#             fake_index = 0 if labels[0].lower() == "fake" else 1
#             fake_prob = round(probs[fake_index], 4)
#             real_prob = round(probs[1 - fake_index], 4)

#             fake_scores.append(fake_prob)
#             real_scores.append(real_prob)

#         # Calculate average probabilities
#         avg_fake = sum(fake_scores) / len(fake_scores)
#         avg_real = sum(real_scores) / len(real_scores)

#         # Get file metadata
#         file_name = os.path.basename(file_info)
#         file_size = f"{(os.path.getsize(file_info) / 1024 / 1024):.1f} MB"

#         # Generate HTML output
#         html_output = f"""
#         <div style="border: 2px solid {'#ff4444' if avg_fake > 0.5 else '#4CAF50'}; 
#                     padding: 25px; 
#                     border-radius: 15px;
#                     margin: 15px;
#                     background: linear-gradient(145deg, {'#fff5f5' if avg_fake > 0.5 else '#f5fff5'}, #ffffff);
#                     box-shadow: 0 8px 16px rgba(0,0,0,0.1);">
#             <h2 style="color: {'#ff4444' if avg_fake > 0.5 else '#4CAF50'};">{'DEEPFAKE DETECTED' if avg_fake > 0.5 else 'AUTHENTIC VIDEO'}</h2>
#             <p><strong>Fake Probability:</strong> {avg_fake*100:.1f}%</p>
#             <p><strong>Real Probability:</strong> {avg_real*100:.1f}%</p>
#             <p><strong>File Name:</strong> {file_name}</p>
#             <p><strong>File Size:</strong> {file_size}</p>
#             <p><strong>Analysis Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
#         </div>
#         """

#         return html_output

#     except Exception as e:
#         return f"""
#         <div style='color: #ff4444; 
#                     padding: 20px; 
#                     background: #fff0f0; 
#                     border-radius: 8px;
#                     border: 2px solid #ffcccc;
#                     margin: 15px;'>
#             ⚠️ Error: {str(e)}
#             <div style="margin-top: 10px; font-size: 0.9em;">
#                 Please ensure you've uploaded a valid video file (MP4/AVI)
#             </div>
#         </div>
#         """







import cv2
import tempfile
import torch
from transformers import AutoImageProcessor, SiglipForImageClassification
from PIL import Image
import os
from datetime import datetime

# Load model and processor
model_name = "prithivMLmods/Deepfake-Real-Class-Siglip2"
model = SiglipForImageClassification.from_pretrained(model_name)
processor = AutoImageProcessor.from_pretrained(model_name)

def extract_frames_opencv(video_path, num_frames=10):
    """Extracts frames from a video using OpenCV."""
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    frame_indices = [int(i * total_frames / num_frames) for i in range(num_frames)]
    frames = []
    
    for idx in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            temp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
            cv2.imwrite(temp_file.name, frame)
            frames.append(temp_file.name)
    
    cap.release()
    return frames

def classify_video(file_path):
    """Analyzes a video for deepfake detection"""
    try:
        frame_paths = extract_frames_opencv(file_path, num_frames=10)
        fake_scores, real_scores = [], []
        
        for frame_path in frame_paths:
            image = Image.open(frame_path).convert("RGB")
            inputs = processor(images=image, return_tensors="pt")
            
            with torch.no_grad():
                outputs = model(**inputs)
                logits = outputs.logits
                probs = torch.nn.functional.softmax(logits, dim=1).squeeze().tolist()

            labels = model.config.id2label
            fake_index = 0 if labels[0].lower() == "fake" else 1
            fake_prob = round(probs[fake_index], 4)
            real_prob = round(probs[1 - fake_index], 4)

            fake_scores.append(fake_prob)
            real_scores.append(real_prob)

        avg_fake = sum(fake_scores) / len(fake_scores)
        avg_real = sum(real_scores) / len(real_scores)

        file_name = os.path.basename(file_path)
        file_size = f"{(os.path.getsize(file_path) / 1024 / 1024):.1f} MB"

        return f"""
        <div style="border: 2px solid {'#ff4444' if avg_fake > 0.5 else '#4CAF50'}; 
                    padding: 25px; 
                    border-radius: 15px;
                    margin: 15px;
                    background: linear-gradient(145deg, {'#fff5f5' if avg_fake > 0.5 else '#f5fff5'}, #ffffff);
                    box-shadow: 0 8px 16px rgba(0,0,0,0.1);">
            <h2 style="color: {'#ff4444' if avg_fake > 0.5 else '#4CAF50'};">{'DEEPFAKE DETECTED' if avg_fake > 0.5 else 'AUTHENTIC VIDEO'}</h2>
            <p><strong>Fake Probability:</strong> {avg_fake*100:.1f}%</p>
            <p><strong>Real Probability:</strong> {avg_real*100:.1f}%</p>
            <p><strong>File Name:</strong> {file_name}</p>
            <p><strong>File Size:</strong> {file_size}</p>
            <p><strong>Analysis Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        """

    except Exception as e:
        return f"""
        <div style='color: #ff4444; padding: 20px; background: #fff0f0; border-radius: 8px;
                    border: 2px solid #ffcccc; margin: 15px;'>
            ⚠️ Error: {str(e)}
            <div style="margin-top: 10px; font-size: 0.9em;">
                Please ensure you've uploaded a valid video file (MP4/AVI)
            </div>
        </div>
        """

