import tkinter as tk
from tkinter import messagebox, Toplevel, Label
from tkinter import ttk
import pandas as pd
import joblib

# Load the pre-trained model and preprocessor
model = joblib.load('titanic_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

# Define the features for the GUI
features = {
    'Pclass': ['First Class', 'Second Class', 'Third Class'],
    'Sex': ['Male', 'Female'],
    'Age': ['Unknown'] + list(range(0, 101)),  # 'Unknown' and age range
    'SibSp': 0,  # Default value
    'Parch': 0,  # Default value
    'Fare': 0.0,  # Default value
    'Embarked': ['Southampton', 'Queenstown', 'Cherbourg'],
}

def show_tooltip(widget, text):
    def enter(event):
        tooltip = Toplevel(root)
        tooltip.wm_overrideredirect(True)
        tooltip.wm_geometry(f"+{root.winfo_pointerx()}+{root.winfo_pointery() + 20}")
        label = Label(tooltip, text=text, background="lightyellow", relief="solid", padx=5, pady=5)
        label.pack()
        widget.tooltip = tooltip

    def leave(event):
        if hasattr(widget, 'tooltip'):
            widget.tooltip.destroy()
            del widget.tooltip

    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)

def toggle_age_entry():
    if age_known_var.get() == 'known':
        age_entry.grid(row=4, column=1, padx=20, pady=5, sticky='ew')
        age_entry.focus_set()
    else:
        age_entry.grid_forget()
        age_var.set('0')  # Automatically set age to 0 when unknown is selected

def validate_age_input(char):
    return char.isdigit() or char == ''

def predict_survival():
    try:
        # Retrieve the input values from the GUI
        passenger_data = {
            'Pclass': pclass_var.get(),
            'Sex': sex_var.get(),
            'Age': int(age_var.get()) if age_known_var.get() == 'known' else 0,  # Set age to 0 if unknown
            'SibSp': int(sibsp_var.get()),
            'Parch': int(parch_var.get()),
            'Fare': float(fare_var.get()),
            'Embarked': embarked_var.get(),
            'FamilySize': int(sibsp_var.get()) + int(parch_var.get()) + 1
        }

        # Convert to DataFrame
        new_data = pd.DataFrame([passenger_data])

        # Preprocess and predict
        new_data_preprocessed = preprocessor.transform(new_data)
        prediction = model.predict(new_data_preprocessed)

        # Show the result
        result = 'Survived' if prediction[0] == 'Yes' else 'Did not survive'
        messagebox.showinfo("Prediction Result", f"The passenger {result}.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Titanic Survival Prediction")
root.geometry("400x500")  # Adjusted window size
root.configure(bg="#f0f0f0")

# Define font and colors
font = ("Arial", 12)
highlight_color = "#4a90e2"
button_color = "#009688"

# Center the window on the screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

# Create and place the widgets using grid
tk.Label(root, text="Titanic Survival Prediction", font=("Arial", 16, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10, padx=20)

# Pclass
tk.Label(root, text="Pclass", font=font, bg="#f0f0f0").grid(row=1, column=0, padx=20, pady=5, sticky='w')
pclass_var = tk.StringVar(value=features['Pclass'][2])  # Default to Third Class
pclass_menu = ttk.Combobox(root, textvariable=pclass_var, values=features['Pclass'], state="readonly")
pclass_menu.grid(row=1, column=1, padx=20, pady=5, sticky='ew')
show_tooltip(pclass_menu, "Ticket class of the passenger: First Class, Second Class, or Third Class.")

# Sex
tk.Label(root, text="Sex", font=font, bg="#f0f0f0").grid(row=2, column=0, padx=20, pady=5, sticky='w')
sex_var = tk.StringVar(value=features['Sex'][0])  # Default to Male
sex_menu = ttk.Combobox(root, textvariable=sex_var, values=features['Sex'], state="readonly")
sex_menu.grid(row=2, column=1, padx=20, pady=5, sticky='ew')
show_tooltip(sex_menu, "Gender of the passenger.")

# Age input
tk.Label(root, text="Age", font=font, bg="#f0f0f0").grid(row=3, column=0, padx=20, pady=5, sticky='w')

age_frame = tk.Frame(root, bg="#f0f0f0")
age_frame.grid(row=3, column=1, padx=20, pady=5, sticky='ew')

age_known_var = tk.StringVar(value='unknown')
age_known_rb = tk.Radiobutton(age_frame, text="Known", variable=age_known_var, value='known', bg="#f0f0f0", font=font, command=toggle_age_entry)
age_unknown_rb = tk.Radiobutton(age_frame, text="Unknown", variable=age_known_var, value='unknown', bg="#f0f0f0", font=font, command=toggle_age_entry)

age_known_rb.pack(side='left', padx=5)
age_unknown_rb.pack(side='left', padx=5)

age_var = tk.StringVar(value='0')
age_entry = tk.Entry(root, textvariable=age_var, font=font, validate='key', width=20)
age_entry.configure(validatecommand=(root.register(validate_age_input), '%S'))

# Other entries
tk.Label(root, text="SibSp", font=font, bg="#f0f0f0").grid(row=5, column=0, padx=20, pady=5, sticky='w')
sibsp_var = tk.StringVar(value=str(features['SibSp']))
sibsp_entry = tk.Entry(root, textvariable=sibsp_var, font=font)
sibsp_entry.grid(row=5, column=1, padx=20, pady=5, sticky='ew')
show_tooltip(sibsp_entry, "Number of siblings or spouses aboard the Titanic.")

tk.Label(root, text="Parch", font=font, bg="#f0f0f0").grid(row=6, column=0, padx=20, pady=5, sticky='w')
parch_var = tk.StringVar(value=str(features['Parch']))
parch_entry = tk.Entry(root, textvariable=parch_var, font=font)
parch_entry.grid(row=6, column=1, padx=20, pady=5, sticky='ew')
show_tooltip(parch_entry, "Number of parents or children aboard the Titanic.")

tk.Label(root, text="Fare", font=font, bg="#f0f0f0").grid(row=7, column=0, padx=20, pady=5, sticky='w')
fare_var = tk.StringVar(value=str(features['Fare']))
fare_entry = tk.Entry(root, textvariable=fare_var, font=font)
fare_entry.grid(row=7, column=1, padx=20, pady=5, sticky='ew')
show_tooltip(fare_entry, "Amount of money the passenger paid for the ticket.")

tk.Label(root, text="Embarked", font=font, bg="#f0f0f0").grid(row=8, column=0, padx=20, pady=5, sticky='w')
embarked_var = tk.StringVar(value=features['Embarked'][0])  # Default to Southampton
embarked_menu = ttk.Combobox(root, textvariable=embarked_var, values=features['Embarked'], state="readonly")
embarked_menu.grid(row=8, column=1, padx=20, pady=5, sticky='ew')
show_tooltip(embarked_menu, "Port of Embarkation: Southampton, Queenstown, or Cherbourg.")

tk.Button(root, text="Predict", command=predict_survival, bg=button_color, fg="white", font=font).grid(row=9, column=0, columnspan=2, pady=20)

# Start the GUI event loop
root.mainloop()
