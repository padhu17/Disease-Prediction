### 🧠 Disease Prediction System using Machine Learning

A machine learning-based application that predicts possible diseases based on user-input symptoms. This project aims to assist in early diagnosis by analyzing patterns from a dataset of symptoms and corresponding diseases.

### 🚀 Features

- Predicts disease based on multiple symptom inputs
- Trained with popular ML algorithms: Random Forest, Naive Bayes, and SVM
- Modular structure for training, testing, and inference
- FastAPI-powered backend for real-time prediction API
- Integrated Streamlit-based UI for seamless user interaction (optional HTML/CSS version also included)

### 🎨 User Interface

- Streamlit UI: Clean and responsive symptom input form for live predictions
- Allows users to enter 3 to 7 symptoms and receive a list of most probable diseases with confidence scores

### 📊 Tech Stack

- Python, Pandas, Scikit-learn
- FastAPI for backend API
- Streamlit for UI
- Jupyter Notebooks for model development

### 📁 Dataset

- Based on publicly available medical datasets with symptoms as features and diseases as labels
- [ https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset](url)

### 🛠️ How to Run Locally

Follow these steps to set up and run the Disease Prediction System on your local machine.

1️⃣ Clone the Repository
> git clone https://github.com/padhu17/disease-prediction.git
> cd disease-prediction

2️⃣ Create and Activate Virtual Environment
- Create virtual environment
  > python -m venv venv

- Activate it
  - On Windows:
    > venv\Scripts\activate
  - On macOS/Linux:
    > source venv/bin/activate

3️⃣ Install Required Dependencies
> pip install -r requirements.txt

4️⃣ Train the Model
- There are 2 options to train the model
  - Using Jupyter notebook
    - Directly copy and paste the cells in the jupyter notebook
    - Run the cells
    - A new cleaned and augumented excel file will be created
    - An efficient model will be saved to the pickle files in the model folder.
  - Using the venv 
    > python model.py

5️⃣ Run the Backend API (FastAPI)
- If the uvicorn is not installed at the time of execution of Step 3
  > pip install fastapi uvicorn

- If the uvicorn is installed
  > uvicorn app.main:app --reload
  - The API will be available at: [http://127.0.0.1:8000/docs](url) (Swagger UI for testing endpoints)

<img width="1880" height="741" alt="image" src="https://github.com/user-attachments/assets/a597c217-76f3-4044-9ce2-6bdd5c37b75c" />


6️⃣ Launch the Streamlit UI __(Bonus)__
- Install the library Streamlit
  > pip install streamlit
- Execute and test the app in the browser
  > streamlit run streamlit_app/app.py
  - This will open a user-friendly interface in your browser at [http://localhost:8501](url)

Screenshot


