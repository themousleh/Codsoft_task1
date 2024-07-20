# Titanic Survival Prediction Project

## Overview

The Titanic Survival Prediction project involves developing a machine learning model to predict whether a passenger survived the Titanic disaster based on various features. The model uses a classification algorithm trained on the Titanic dataset. This project includes a GUI application built with Tkinter that allows users to input passenger details and receive survival predictions.

## Project Structure

- **Data**: The dataset containing Titanic passenger information (`titanic.csv`).
- **Model Training**: Python script (`train_model.py`) to train and save the model.
- **GUI Application**: Python script (`app.py`) that provides a graphical user interface for predicting survival based on user input.
- **Model Files**: Saved model file (`titanic_model.pkl`).
- **Preprocessor Files**: Preprocessing steps saved in a file (`preprocessor.pkl`).

## Objectives

1. [Load and Explore the Dataset](#load-and-explore-the-dataset)
2. [Data Preprocessing](#data-preprocessing)
3. [Train-Test Split](#train-test-split)
4. [Model Training](#model-training)
5. [Model Evaluation](#model-evaluation)
6. [GUI Application](#gui-application)

## Getting Started

### Prerequisites

- Python 3.x
- `pandas`
- `scikit-learn`
- `joblib`
- `tkinter`

You can install the required packages using pip:

```bash
pip install pandas scikit-learn joblib
```

### Training the Model

1. Ensure `titanic.csv` is in the project directory.
2. Run `train_model.py` to train and save the model and preprocessor:

   ```bash
   python train_model.py
   ```

### Running the GUI Application

1. Ensure `titanic_model.pkl` and `preprocessor.pkl` are in the same directory as `app.py`.
2. Run `app.py`:

   ```bash
   python app.py
   ```

   This will open a GUI application where you can input passenger details and get a survival prediction.

## Usage

1. Fill in the details for each passenger, including Pclass, Sex, Age, SibSp, Parch, Fare, and Embarked.
2. Use the radio buttons to specify if the age is known or unknown. If "Unknown" is selected, the age entry field will be hidden and age will be set to 0 automatically.
3. Click "Predict" to see the survival prediction for the passenger.

## Troubleshooting

- **Model or Preprocessor Missing**: Ensure that `titanic_model.pkl` and `preprocessor.pkl` are present in the directory.
- **Input Issues**: Make sure to enter valid numerical values where required. Invalid input will trigger an error message.
- **GUI Display Issues**: Adjust your display settings or window size if the GUI elements do not align correctly.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## Acknowledgments

This project utilizes the Titanic dataset for survival prediction and leverages a machine learning model and Tkinter for GUI development.

## Contact

For questions or feedback, please contact [Issa El Mousleh](mailto:issaelmousleh@outlook.com).
