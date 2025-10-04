# ❤️ Heart Disease Prediction System

A machine learning-powered web application that predicts the presence of heart disease based on clinical parameters. Built with scikit-learn and deployed using Streamlit.

## 🌐 Live Demo

**Try it now:** [Heart Disease Predictor](https://heart-disease-predictor-k58mj5pwcb52ecylzc2tdb.streamlit.app/)

## 📊 Dataset

- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease)
- **Target Column:** `num`
  - `0`: Less than 50% diameter narrowing (No heart disease)
  - `1`: More than 50% diameter narrowing (Heart disease)
- **Features:** Age, Sex, Chest Pain Type, Blood Pressure, ECG Results, Heart Rate, and more

## 🧠 Model Performance

Multiple machine learning models were tested using cross-validation:

| Model                      | Accuracy  |
|----------------------------|-----------|
| KNeighborsClassifier       | 0.8187    |
| RandomForestClassifier     | 0.8148    |
| LogisticRegression         | 0.7980    |
| GradientBoostingClassifier | 0.7650    |

**Best Model:** KNeighborsClassifier with **81.87% accuracy**

📄 *For detailed scores, refer to `models.txt` file.*

## ✨ Features

- 🎨 **Modern UI** - Clean, medical-themed interface built with Streamlit
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile
- 🔍 **Real-time Predictions** - Instant heart disease risk assessment
- 📊 **Visual Results** - Color-coded predictions with confidence scores
- ℹ️ **Helpful Tooltips** - Guidance for each input parameter
- 📈 **Input Summary** - Review all entered values before prediction

## 🛠️ Technologies Used

### Machine Learning
- Python
- scikit-learn (preprocessing, modeling, evaluation)
- Pandas, NumPy
- Joblib (model serialization)

### Web Application
- Streamlit (UI framework)
- Custom CSS styling
- Responsive layout design

## 🚀 Project Pipeline

1. **Data Processing**
   - Loaded and cleaned the UCI Heart Disease dataset
   - Handled missing values using `SimpleImputer`
   - Feature scaling for optimal model performance

2. **Model Training**
   - Split dataset into training and testing sets
   - Applied cross-validation on multiple classifiers
   - Evaluated using accuracy scores

3. **Model Selection**
   - Compared performance of various algorithms
   - Selected KNeighborsClassifier as the final model

4. **Web Deployment**
   - Created interactive Streamlit interface
   - Integrated trained model for real-time predictions
   - Deployed on Streamlit Cloud

## 📁 Project Structure

```
heart-disease-predictor/
├── app.py                              # Streamlit web application
├── Heart_Disease_Predictor.joblib      # Trained ML model
├── heart_disease_predictor.ipynb       # Model development notebook
├── heart_disease_predictor.py          # Python script version
├── requirements.txt                    # Python dependencies
├── models.txt                          # Model performance comparison
└── README.md                           # Project documentation
```

## 💻 Local Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vedant-Git-dev/heart-disease-predictor.git
   cd heart-disease-predictor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   - The app will automatically open at `http://localhost:8501`

## 📊 Input Features

The model uses the following 11 clinical parameters:

| Feature | Description | Range/Values |
|---------|-------------|--------------|
| **age** | Patient's age | 1-120 years |
| **sex** | Gender | 0: Female, 1: Male |
| **cp** | Chest pain type | 0-3 (Typical angina to Asymptomatic) |
| **trestbps** | Resting blood pressure | 80-200 mm Hg |
| **restecg** | Resting ECG results | 0-2 (Normal to Hypertrophy) |
| **thalach** | Maximum heart rate | 60-220 bpm |
| **exang** | Exercise induced angina | 0: No, 1: Yes |
| **oldpeak** | ST depression | 0.0-10.0 |
| **slope** | ST segment slope | 0-2 (Upsloping to Downsloping) |
| **ca** | Number of major vessels | 0-4 |
| **thal** | Thalassemia | 0-3 (Normal to Unknown) |

## 🎯 Usage Example

1. Visit the [live application](https://heart-disease-predictor-k58mj5pwcb52ecylzc2tdb.streamlit.app/)
2. Enter patient information in the input fields
3. Click "🔍 Predict Heart Disease Risk"
4. View the prediction result and confidence score

## ⚠️ Disclaimer

This application is for **educational and informational purposes only**. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical decisions.

## 🔮 Future Enhancements

- [ ] Add hyperparameter tuning (GridSearchCV/RandomizedSearchCV)
- [ ] Implement SHAP values for model explainability
- [ ] Add data visualization dashboard
- [ ] Include multiple model comparison in UI
- [ ] Add patient history tracking
- [ ] Export prediction reports as PDF

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Fork the repository
- Create a feature branch
- Submit a pull request
- Report bugs or suggest features

## 📝 License

This project is open-source and available for educational purposes.

## 👨‍💻 Developed By

**Vedant Pardeshi**

- 🔗 LinkedIn: [Vedant Pardeshi](https://www.linkedin.com/in/vedant-pardeshi-642937321)
- 💻 GitHub: [Vedant-Git-dev](https://github.com/Vedant-Git-dev)
- 🌐 Live App: [Heart Disease Predictor](https://heart-disease-predictor-k58mj5pwcb52ecylzc2tdb.streamlit.app/)

---

⭐ **If you find this project helpful, please give it a star!** ⭐
