# 🌍 DisasterVision - AI-Powered Disaster Detection

_DisasterVision_ is an AI-powered web application designed to classify disaster-related images and assist in early disaster management. Leveraging deep learning and an intuitive Gradio interface, this tool aims to support emergency response teams and researchers with quick and accurate disaster detection.

---

## 🚀 Features

- 📸 Upload disaster-related images (earthquakes, floods, fires, etc.)
- 🤖 Real-time image classification using a pre-trained ML model
- 🧠 Built with PyTorch and Gradio for rapid development
- 🌐 Shareable web interface with `demo.launch(share=True)`
- 💡 Easy-to-use and clean UI with custom CSS support

---

## 🛠️ Tech Stack

| Tech       | Purpose                         |
|------------|---------------------------------|
| Python     | Backend scripting               |
| PyTorch    | Deep learning model handling    |
| Gradio     | Frontend UI interface           |
| OpenCV     | Image preprocessing             |
| HTML/CSS   | UI enhancements (Markdown & CSS)|

---

## 📂 Project Structure

├── app.py # Main Gradio app interface
├── backend.py # ML model logic & classification
├── disaster_model.pth # Trained PyTorch model (not included in repo)
├── style.css # Custom CSS for Gradio UI
├── requirements.txt # List of dependencies
└── README.md # You're here!

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/DisasterVision.git
cd DisasterVision
2. Create Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv godel-env
godel-env\Scripts\activate  # On Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add Your Model
Make sure to place your trained model file as:

Copy
Edit
disaster_model.pth
🔒 Note: The model file is not included for security reasons.

5. Run the Application
bash
Copy
Edit
python app.py
The app will launch in your browser. You can also share it using the public Gradio link!

📦 Requirements
shell
Copy
Edit
gradio>=4.0
torch>=1.9
torchvision
opencv-python
Generate it via:

bash
Copy
Edit
pip freeze > requirements.txt
🧪 Sample Output
Upload an image and see the AI classify the disaster type with confidence score in real-time!

📌 Use Cases
Disaster response planning

Data analysis for emergency services

Educational demonstrations for climate/disaster awareness

Research support in environmental AI

📃 License
This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

✨ Credits
Built by Your Sourabh Yadav

Powered by Open Source 💖

📬 Contact
Got questions or suggestions? Reach out via:

📧 your. sourabh3y@gmail.com
