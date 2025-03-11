
# # app.py
# import gradio as gr
# from backend import classify_image

# # Create custom Gradio interface
# with gr.Blocks(title="DeepForensic - Deepfake Detection", theme=gr.themes.Soft()) as demo:
#     gr.Markdown("""
#     <div style="text-align: center; padding: 20px;">
#         <h1 style="margin-bottom: 10px;">🔍 DeepForensic - Deepfake Detection System</h1>
#         <p style="color: #666;">Upload an image to analyze its authenticity using advanced AI detection models</p>
#     </div>
#     """)
    
#     with gr.Row():
#         with gr.Column(scale=1):
#             # Enhanced Upload Section
#             gr.Markdown("""
#             <div style="text-align: center; margin-bottom: 20px;">
#                 <h3 style="color: #4CAF50;">📤 Upload Image</h3>
#                 <p style="color: #666; font-size: 0.9em;">Drag & drop or click to upload an image</p>
#             </div>
#             """)
#             file_input = gr.File(
#                 label="", 
#                 file_types=["image"],
#                 type="filepath",
#                 elem_classes="custom-upload"
#             )
#             upload_button = gr.Button(
#                 "Analyze Now ▶️", 
#                 variant="primary", 
#                 elem_classes="custom-button"
#             )
        
#         with gr.Column(scale=2):
#             output_html = gr.HTML(label="Analysis Report")

#     # Load custom CSS
#     with open("style.css", "r") as f:
#         custom_css = f.read()
#     demo.css = custom_css

#     # Connect components
#     upload_button.click(
#         fn=classify_image,
#         inputs=file_input,
#         outputs=output_html
#     )

# # Launch the app
# if __name__ == "__main__":
#     demo.launch(share=True)











# app.py
import gradio as gr
from backend import classify_image, classify_video

# Create custom Gradio interface
with gr.Blocks(title="DeepForensic - Deepfake Detection", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    <div style="text-align: center; padding: 20px;">
        <h1 style="margin-bottom: 10px;">🔍 DeepForensic - Deepfake Detection System</h1>
        <p style="color: #666;">Upload an image or video to analyze its authenticity using advanced AI detection models</p>
    </div>
    """)

    with gr.Tabs():
        # Image Deepfake Detection Section
        with gr.Tab("🖼️ Image Detection"):
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("""
                    <div style="text-align: center; margin-bottom: 20px;">
                        <h3 style="color: #4CAF50;">📤 Upload Image</h3>
                        <p style="color: #666; font-size: 0.9em;">Drag & drop or click to upload an image</p>
                    </div>
                    """)
                    image_input = gr.File(
                        label="Upload Image",
                        file_types=["image"],
                        type="filepath",
                        elem_classes="custom-upload"
                    )
                    image_button = gr.Button(
                        "Analyze Image ▶️",
                        variant="primary",
                        elem_classes="custom-button"
                    )
                
                with gr.Column(scale=2):
                    image_output = gr.HTML(label="Image Analysis Report")

        # Video Deepfake Detection Section
        with gr.Tab("🎥 Video Detection"):
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("""
                    <div style="text-align: center; margin-bottom: 20px;">
                        <h3 style="color: #FF9800;">📤 Upload Video</h3>
                        <p style="color: #666; font-size: 0.9em;">Drag & drop or click to upload a video</p>
                    </div>
                    """)
                    video_input = gr.File(
                        label="Upload Video",
                        file_types=["video"],
                        type="filepath",
                        elem_classes="custom-upload"
                    )
                    video_button = gr.Button(
                        "Analyze Video ▶️",
                        variant="primary",
                        elem_classes="custom-button"
                    )

                with gr.Column(scale=2):
                    video_output = gr.HTML(label="Video Analysis Report")

    # Load custom CSS
    with open("style.css", "r") as f:
        custom_css = f.read()
    demo.css = custom_css

    # Connect components
    image_button.click(
        fn=classify_image,
        inputs=image_input,
        outputs=image_output
    )

    video_button.click(
        fn=classify_video,
        inputs=video_input,
        outputs=video_output
    )

# Launch the app
if __name__ == "__main__":
    demo.launch(share=True)
