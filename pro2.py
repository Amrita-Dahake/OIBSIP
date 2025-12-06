from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("BMI CALCULATOR")
root.geometry("700x500")
root.config(bg="#f0f7ff")   # Light blue background




# Heading
label1 = Label(root, text="OASIS INFOBYTE - BMI CALCULATOR",
               font=("Times", 22, "bold"), bg="#f0f7ff", fg="#003366")
label1.pack(pady=10)

label2 = Label(root, text="Enter your Weight (kg) & Height (cm) below:",
               font=("Times", 16), bg="#f0f7ff", fg="#003366")
label2.pack(pady=5)

frame = Frame(root, bg="#f0f7ff")
frame.pack(pady=20)

# Weight
Label(frame, text="Weight (kg):", font=("Times", 14),
      bg="#f0f7ff").grid(row=0, column=0, padx=10, pady=10)
n_txtbx = Entry(frame, font=("Times", 14))
n_txtbx.grid(row=0, column=1)

# Height
Label(frame, text="Height (cm):", font=("Times", 14),
      bg="#f0f7ff").grid(row=1, column=0, padx=10, pady=10)
m_txtbx = Entry(frame, font=("Times", 14))
m_txtbx.grid(row=1, column=1)

# RESULT BOX
Label(root, text="Your BMI:", font=("Times", 16),
      bg="#f0f7ff").pack()
result_txtbx = Entry(root, font=("Times", 16), justify="center")
result_txtbx.pack(pady=5)

# CATEGORY TEXT
category_label = Label(root, text="", font=("Times", 18, "bold"),
                       bg="#f0f7ff", fg="#002244")
category_label.pack(pady=10)


# BMI FUNCTION
def calculate_bmi():
    try:
        weight = float(n_txtbx.get())
        height = float(m_txtbx.get()) / 100
        bmi_value = weight / (height * height)

        result_txtbx.delete(0, END)
        result_txtbx.insert(0, round(bmi_value, 2))

        # BMI CATEGORY
        if bmi_value < 18.5:
            category_label.config(text="UNDERWEIGHT", fg="#ff9933")
        elif 18.5 <= bmi_value <= 24.9:
            category_label.config(text="HEALTHY WEIGHT", fg="#33aa33")
        elif 25.0 <= bmi_value <= 29.9:
            category_label.config(text="OVERWEIGHT", fg="#cc6600")
        else:
            category_label.config(text="OBESITY", fg="#cc0000")

    except:
        messagebox.showerror("Error", "Please enter valid numbers!")


# RESET FUNCTION
def reset():
    n_txtbx.delete(0, END)
    m_txtbx.delete(0, END)
    result_txtbx.delete(0, END)
    category_label.config(text="")


# BUTTONS
btn_frame = Frame(root, bg="#f0f7ff")
btn_frame.pack(pady=15)

calc_btn = Button(btn_frame, text="CALCULATE BMI", command=calculate_bmi,
                  font=("Times", 14, "bold"), bg="#99ccff", fg="black",
                  padx=20, pady=5)
calc_btn.grid(row=0, column=0, padx=10)

reset_btn = Button(btn_frame, text="RESET", command=reset,
                   font=("Times", 14, "bold"), bg="#ffcccc", fg="black",
                   padx=20, pady=5)
reset_btn.grid(row=0, column=1, padx=10)

root.mainloop()

