#leave letter generator

import tkinter as tk
from tkinter import ttk, messagebox

# --- REASONS ---
reasons = [
    "Sick Leave",
    "Personal Work",
    "Family Function",
    "Emergency",
    "Out of Station",
    "Doctor Appointment",
    "Marriage in Family",
    "Urgent Travel",
    "Death in Family",
    "Religious Occasion",
    "Exams Preparation",
    "Household Work",
    "Bad Weather"
]

# --- LETTER TEMPLATES ---
templates = {
    "Sick Leave": (
        "To,\nThe Principal,\n\n"
        "Respected Sir/Madam,\n\n"
        "I am {name}, a student of class {class_}. I am suffering from a health issue and therefore unable to attend school from {from_date} to {to_date}. "
        "I request you to kindly grant me medical leave for the mentioned duration. I assure you I will catch up with all the lessons and assignments missed during this period.\n\n"
        "Thanking you in anticipation.\n\nYours obediently,\n{name}"
    ),
    "Personal Work": (
        "To,\nThe Principal,\n\n"
        "Respected Sir/Madam,\n\n"
        "I am {name} from class {class_}. I kindly request leave from {from_date} to {to_date} due to unavoidable personal work that requires my attention. "
        "I shall ensure that my academic responsibilities are not affected and I will cover up for any missed lessons.\n\n"
        "I hope you will consider my request favorably.\n\nSincerely,\n{name}"
    ),
    "Family Function": (
        "To,\nThe Principal,\n\n"
        "Respected Sir/Madam,\n\n"
        "I, {name}, studying in class {class_}, request leave from {from_date} to {to_date} as I need to attend an important family function. "
        "This function holds personal significance, and my presence is necessary.\n\n"
        "Kindly grant me permission to take leave for the said period.\n\nThank you for your consideration.\n\nRegards,\n{name}"
    ),
    "Emergency": (
        "To,\nThe Principal,\n\n"
        "Respected Sir/Madam,\n\n"
        "I am {name} of class {class_}. Due to an unexpected emergency at home, I am unable to attend school from {from_date} to {to_date}. "
        "I kindly request you to grant me emergency leave.\n\n"
        "Thanking you for your understanding.\n\nYours sincerely,\n{name}"
    ),
    "Out of Station": (
        "To,\nThe Principal,\n\n"
        "Respected Sir/Madam,\n\n"
        "I, {name} from class {class_}, will be travelling out of station due to personal reasons and hence will not be able to attend school from {from_date} to {to_date}. "
        "Kindly grant me leave for the mentioned duration.\n\n"
        "Thank you in advance.\n\nRespectfully,\n{name}"
    ),
    "Doctor Appointment": (
        "To,\nThe Principal,\n\n"
        "Respected Sir/Madam,\n\n"
        "I am {name}, a student of class {class_}. I have a scheduled medical appointment on {from_date}, and therefore, I request you to kindly grant me leave on this date. "
        "I shall resume school promptly and make up for any missed academic work.\n\n"
        "Thank you for your support.\n\nSincerely,\n{name}"
    ),
    "Marriage in Family": (
        "To,\nThe Principal,\n\n"
        "Respected Sir/Madam,\n\n"
        "I, {name} of class {class_}, wish to inform you that I have to attend a family member’s wedding ceremony from {from_date} to {to_date}. "
        "This is a significant event for our family, and I would be grateful if you could grant me leave for the mentioned period.\n\n"
        "Thank you for your kind consideration.\n\nWarm regards,\n{name}"
    ),
    "Urgent Travel": (
        "To,\nThe Principal,\n\n"
        "Respected Sir/Madam,\n\n"
        "I am {name} from class {class_}. Due to an urgent family matter requiring travel, I am unable to attend school from {from_date} to {to_date}. "
        "I kindly request you to consider my situation and grant me leave accordingly.\n\n"
        "I shall ensure to cover any missed syllabus.\n\nSincerely,\n{name}"
    ),
    "Death in Family": (
        "To,\nThe Principal,\n\n"
        "Respected Sir/Madam,\n\n"
        "With due respect, I am {name} from class {class_}. There has been a sad demise of a close family member, and I need to be with my family during this time. "
        "Hence, I request you to kindly grant me leave from {from_date} to {to_date}.\n\n"
        "I hope for your kind understanding and support.\n\nYours sincerely,\n{name}"
    ),
    "Religious Occasion": (
        "To,\nThe Principal,\n\n"
        "Respected Sir/Madam,\n\n"
        "I, {name}, a student of class {class_}, wish to inform you that I will not be able to attend school from {from_date} to {to_date} due to religious observances in my family. "
        "I request you to kindly approve my leave for the mentioned duration.\n\n"
        "Thank you for your consideration.\n\nRegards,\n{name}"
    ),
    "Exams Preparation": (
        "Respected Sir/Madam,\n\n"
        "I am {name} from class {class_}. With upcoming examinations, I would like to request leave from {from_date} to {to_date} for focused preparation.\n\n"
        "This will help me study effectively and perform well in my exams. I hope you will consider my request.\n\n"
        "Sincerely,\n{name}"
    ),
    "Household Work": (
        "Respected Sir/Madam,\n\n"
        "I am {name} of class {class_}. Due to unavoidable household responsibilities that require my involvement, I request leave from {from_date} to {to_date}.\n\n"
        "I assure you that I will resume my studies with the same enthusiasm upon return.\n\n"
        "Thank you for your understanding.\n\nRespectfully,\n{name}"
    ),
    "Bad Weather": (
        "Respected Sir/Madam,\n\n"
        "I am {name}, a student of class {class_}. Due to extreme weather conditions in our area, it is not safe for me to travel to school. "
        "Hence, I request you to kindly grant me leave from {from_date} to {to_date}.\n\n"
        "I will stay updated with lessons and complete any missed work.\n\nYours faithfully,\n{name}"
    )
}

# --- FUNCTION TO GENERATE LETTER ---
def generate_letter(name, class_, from_date, to_date, reason):
    template = templates.get(reason)
    if not template:
        return "Sorry, no template available for selected reason."
    return template.format(name=name, class_=class_, from_date=from_date, to_date=to_date)

# --- GUI ---
def on_generate():
    name = name_entry.get().strip()
    class_ = class_entry.get().strip()
    from_date = from_date_entry.get().strip()
    to_date = to_date_entry.get().strip()
    reason = reason_var.get()

    if not (name and class_ and from_date and to_date and reason):
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    letter = generate_letter(name, class_, from_date, to_date, reason)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, letter)

# --- GUI SETUP ---
root = tk.Tk()
root.title("Leave Letter Generator")
root.geometry("720x600")
root.resizable(False, False)

# Input Fields
tk.Label(root, text="Your Name:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
name_entry = tk.Entry(root, width=50)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Class/Section:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
class_entry = tk.Entry(root, width=50)
class_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="From Date (DD-MM-YYYY):").grid(row=2, column=0, sticky="w", padx=10, pady=5)
from_date_entry = tk.Entry(root, width=50)
from_date_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="To Date (DD-MM-YYYY):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
to_date_entry = tk.Entry(root, width=50)
to_date_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Reason for Leave:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
reason_var = tk.StringVar()
reason_dropdown = ttk.Combobox(root, textvariable=reason_var, values=reasons, state="readonly", width=47)
reason_dropdown.grid(row=4, column=1, padx=10, pady=5)

generate_btn = tk.Button(root, text="Generate Letter", command=on_generate, width=20, bg="#4CAF50", fg="white")
generate_btn.grid(row=5, column=0, columnspan=2, pady=15)

tk.Label(root, text="Generated Letter:").grid(row=6, column=0, sticky="nw", padx=10)
output_text = tk.Text(root, width=85, height=15, wrap="word")
output_text.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()