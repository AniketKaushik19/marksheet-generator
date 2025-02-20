import tkinter as tk
from tkinter import messagebox

class MarksheetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Marksheet Application")

        # Create labels and entry fields for student details
        tk.Label(root, text="Student Name" ,fg="brown").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Maths Marks:" , fg="brown").grid(row=1, column=0, padx=10, pady=5)
        self.maths_entry = tk.Entry(root)
        self.maths_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Science Marks:" , fg="brown").grid(row=2, column=0, padx=10, pady=5)
        self.science_entry = tk.Entry(root)
        self.science_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="English Marks:" , fg="brown").grid(row=3, column=0, padx=10, pady=5)
        self.english_entry = tk.Entry(root)
        self.english_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Hindi Marks:" , fg="brown").grid(row=4, column=0, padx=10, pady=5)
        self.hindi_entry = tk.Entry(root)
        self.hindi_entry.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(root, text="Art Marks:" , fg="brown").grid(row=5, column=0, padx=10, pady=5)
        self.art_entry = tk.Entry(root)
        self.art_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(root, text="S.Science Marks:" , fg="brown").grid(row=6, column=0, padx=10, pady=5)
        self.s_science_entry = tk.Entry(root)
        self.s_science_entry.grid(row=6, column=1, padx=10, pady=5)


        # Create a button to calculate and display the result
        calculate_button = tk.Button(root, text="Calculate", fg="brown" , command=self.calculate_marksheet)
        calculate_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Text widget to display the marksheet
        self.result_text = tk.Text(root, height=10, width=40, border=10,  bg="pink")
        self.result_text.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def calculate_marksheet(self):
        try:
            # Retrieve marks from entry fields
            maths_marks = float(self.maths_entry.get())
            science_marks = float(self.science_entry.get())
            english_marks = float(self.english_entry.get())
            hindi_marks = float(self.english_entry.get())
            art_marks = float(self.english_entry.get())
            s_science_marks = float(self.english_entry.get())

            # Calculate total marks and percentage
            total_marks = maths_marks + science_marks + english_marks + hindi_marks + art_marks + s_science_marks
            percentage = (total_marks / 600) * 100

            # Prepare marksheet text
            marksheet = f"Student Name: {self.name_entry.get()}\n"
            marksheet += f"Maths Marks: {maths_marks}\n"
            marksheet += f"Science Marks: {science_marks}\n"
            marksheet += f"English Marks: {english_marks}\n"
            marksheet += f"Hindi Marks: {hindi_marks}\n"
            marksheet += f"Art Marks: {art_marks}\n"
            marksheet += f"S.Science Marks: {s_science_marks}\n"
            marksheet += f"Total Marks: {total_marks}\n"
            marksheet += f"Percentage: {percentage:.2f}%"

            self.name_entry.delete(0, tk.END)
            self.maths_entry.delete(0, tk.END)
            self.science_entry.delete(0, tk.END)
            self.english_entry.delete(0, tk.END)
            self.hindi_entry.delete(0, tk.END)
            self.art_entry.delete(0, tk.END)
            self.s_science_entry.delete(0, tk.END)
  
            # Display marksheet in the text widget
            self.result_text.delete(1.0, tk.END)  # Clear previous content
            self.result_text.insert(tk.END, marksheet)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid marks.")

if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="lightblue")
    app = MarksheetApp(root)
    root.mainloop()
