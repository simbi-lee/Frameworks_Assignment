# 📌 Frameworks_Assignment

This project is a beginner-friendly analysis of the **CORD-19 metadata dataset**, focusing on COVID-19 research papers. It includes data cleaning, visualization, and a simple interactive web app built with **Streamlit**.  

---

## 📂 Project Structure
```
Frameworks_Assignment/
│── analysis.py        # Python script for data loading, cleaning & visualization
│── app.py             # Streamlit app for interactive exploration
│── sample.csv         # Sample dataset (subset of metadata.csv)
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation
```

---

## ⚙️ Installation
Make sure you have **Python 3.7+** installed.  

Clone the repo or unzip the project, then install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 1. Run the Analysis Script
This will clean the dataset and generate visualizations.
```bash
python analysis.py
```

👉 Expected outputs:  
- Publications by year (bar chart)  
- Top journals publishing COVID-19 research  
- Word cloud of paper titles  
- Distribution of papers by source  

---

### 2. Run the Streamlit App
To launch the interactive dashboard:
```bash
streamlit run app.py
```

👉 This will open in your browser at:  
`http://localhost:8501`

Features:  
- Select year range with a slider  
- View publication trends  
- Explore top journals  
- See a preview of the dataset  

---

## 📊 Dataset
The project uses the **CORD-19 metadata.csv** file.  
For simplicity, a smaller **sample.csv** is included in this repo.  
The full dataset can be downloaded here:  
[CORD-19 Research Challenge (Kaggle)](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)  

---

## 📝 Deliverables
By completing this project, you’ll have:  
- A Python analysis script with visualizations  
- A Streamlit app for interactive data exploration  
- Experience with basic data science workflows  

---

## 🙌 Author
Assignment prepared for **Frameworks Course** — Beginner Data Analysis & Visualization.  
