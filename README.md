# Hello App 🧮

Hello App is a **simple calculator** built using [Streamlit](https://streamlit.io/).  
It performs basic arithmetic operations like addition, subtraction, multiplication, and division — all through a clean and interactive web interface.

---

## 🚀 Features

- User-friendly Streamlit web interface
- Supports:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Runs locally in your browser with a single command

---

## 📁 Project Structure


Hello app/
│
├── app.py # Main Streamlit app file
├── requirements.txt # List of required Python packages
└── README.md # This file



---

## 🛠️ Installation & Setup

Follow these steps to run the Hello App on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/ZR792/hello-app.git
cd hello-app

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
pip install streamlit

# ▶️ How to Run the App
streamlit run app.py


