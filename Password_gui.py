import tkinter as tk
from Password_Checker import (
    calculate_score,
    check_length,
    check_upper,
    check_lower,
    check_number,
    check_special,
    generate_password
)
current_score = 0
def update_progress_bar():
    if current_score <= 2:
        color = "red"
    elif current_score <= 4:
        color = "yellow"
    else:
        color = "green"
    progress_fill.config(bg=color)
    progress_fill.place_configure(
        relwidth=current_score / 5
    )
def check_password():
    global current_score
    password = password_entry.get()
    score = calculate_score(password)
    current_score = score
    if score <= 2:
        strength = "WEAK 🔴"
        result_color = "red"
    elif score <= 4:
        strength = "MEDIUM 🟡"
        result_color = "orange"
    else:
        strength = "STRONG 🟢"
        result_color = "green"
    suggestions = []
    if not check_length(password):
        suggestions.append("Use at least 8 characters")
    if not check_upper(password):
        suggestions.append("Add an uppercase letter")
    if not check_lower(password):
        suggestions.append("Add a lowercase letter")
    if not check_number(password):
        suggestions.append("Add a number")
    if not check_special(password):
        suggestions.append("Add a special character")
    if suggestions:
        suggestions_text = "💡 Suggestions:\n"
        for suggestion in suggestions:
            suggestions_text += "❌ " + suggestion + "\n"
    else:
        suggestions_text = "🎉 Excellent! Your password meets all requirements."
    result_label.config(
        text=f"Score: {score}/5   Strength: {strength}",
        fg=result_color
    )
    strength_meter_label.config(
        text=f"Password Strength: {strength}",
        fg=result_color
    )
    suggestion_label.config(
        text=suggestions_text
    )
    update_progress_bar()
def update_password_length(event=None):
    length = len(password_entry.get())
    length_label.config(
        text=f"Characters: {length}"
    )
def update_requirements(event=None):
    password = password_entry.get()
    length = "✓" if check_length(password) else "❌"
    upper = "✓" if check_upper(password) else "❌"
    lower = "✓" if check_lower(password) else "❌"
    number = "✓" if check_number(password) else "❌"
    special = "✓" if check_special(password) else "❌"
    requirements_status.config(
        text=(
            f"{length} 8+ characters    "
            f"{upper} Uppercase    "
            f"{lower} Lowercase    "
            f"{number} Number    "
            f"{special} Special character"
        )
    )
def copy_password():
    password = password_entry.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        window.update()
        copy_button.config(
            text="✓ Copied!"
        )
        window.after(
            1500,
            lambda: copy_button.config(text="📋 Copy Password")
        )
def generate_new_password():
    new_password = generate_password()
    password_entry.config(show="")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, new_password)
    show_button.config(
        text="🔒 Hide Password"
    )
    copy_button.config(
        text="📋 Copy Password"
    )
    update_requirements()
    update_password_length()
    check_password()
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_button.config(
            text="🔒 Hide Password"
        )
    else:
        password_entry.config(show="*")
        show_button.config(
            text="👁 Show Password"
        )
def clear_all():
    global current_score
    password_entry.delete(0, tk.END)
    password_entry.config(show="*")
    result_label.config(
        text="",
        fg="black"
    )
    suggestion_label.config(
        text=""
    )
    strength_meter_label.config(
        text="Password Strength",
        fg="black"
    )
    requirements_status.config(
        text="❌ 8+ characters    ❌ Uppercase    ❌ Lowercase    ❌ Number    ❌ Special character"
    )
    length_label.config(
        text="Characters: 0"
    )
    show_button.config(
        text="👁 Show Password"
    )
    copy_button.config(
        text="📋 Copy Password"
    )
    current_score = 0
    update_progress_bar()
window = tk.Tk()
window.title("Password Strength Checker")
window.config(bg="#f4f6f8")
main_frame = tk.Frame(
    window,
    bg="#f4f6f8",
    padx=25,
    pady=15
)
main_frame.pack(
    fill="both",
    expand=True
)
title_label = tk.Label(
    main_frame,
    text="🔐 Password Strength Checker",
    font=("Times New Roman", 16, "bold"),
    bg="#f4f6f8"
)
title_label.pack(pady=13)
password_frame = tk.LabelFrame(
    main_frame,
    text="🔐 Password",
    font=("Times New Roman", 12, "bold"),
    bg="#ffffff",
    padx=10,
    pady=7
)
password_frame.pack(
    fill="x",
    pady=7
)
action_frame = tk.LabelFrame(
    main_frame,
    text="⚙ Actions",
    font=("Times New Roman", 12, "bold"),
    bg="#ffffff",
    padx=7,
    pady=5
)
action_frame.pack(
    fill="x",
    pady=5
)
password_label = tk.Label(
    password_frame,
    text="Enter your password:",
    font=("Times New Roman", 12),
    bg="#ffffff"
)
password_label.pack()
password_entry = tk.Entry(
    password_frame,
    width=40,
    show="*",
    font=("Times New Roman", 13),
    relief="solid",
    bd=1
)
password_entry.pack(pady=10)
length_label = tk.Label(
    password_frame,
    text="Characters: 0",
    font=("Times New Roman", 9),
    bg="#ffffff",
    anchor="e"
)
length_label.pack(
    fill="x"
)
requirements_label = tk.Label(
    password_frame,
    text="Password must contain:",
    font=("Times New Roman", 10, "bold"),
    bg="#ffffff",
    anchor="w"
)
requirements_label.pack(
    fill="x",
    pady=(5, 2)
)
requirements_status = tk.Label(
    password_frame,
    text="❌ 8+ characters    ❌ Uppercase    ❌ Lowercase    ❌ Number    ❌ Special character",
    font=("Times New Roman", 9),
    bg="#ffffff",
    anchor="w",
    justify="left"
)
requirements_status.pack(
    fill="x",
    pady=(0, 5)
)
password_entry.bind(
    "<KeyRelease>",
    update_requirements
)
password_entry.bind(
    "<KeyRelease>",
    update_password_length,
    add="+"
)
show_button = tk.Button(
    password_frame,
    text="👁 Show Password",
    font=("Times New Roman", 10, "bold"),
    width=18,
    command=toggle_password
)
show_button.pack(
    pady=5
)
check_button = tk.Button(
    action_frame,
    text="🔍 Check Password",
    font=("Times New Roman", 10, "bold"),
    width=20,
    command=check_password
)
check_button.pack(
    pady=8
)
result_frame = tk.LabelFrame(
    main_frame,
    text="📊 Result",
    font=("Times New Roman", 12, "bold"),
    bg="#ffffff",
    padx=15,
    pady=10
)
result_frame.pack(
    fill="x",
    pady=10
)
result_label = tk.Label(
    result_frame,
    text="",
    font=("Times New Roman", 12, "bold"),
    bg="#ffffff",
    fg="black",
    anchor="w",
    justify="left"
)
result_label.pack(
    fill="x",
    pady=5
)
suggestion_label = tk.Label(
    result_frame,
    text="",
    font=("Times New Roman", 9, "bold"),
    bg="#ffffff",
    anchor="nw",
    justify="left"
)
suggestion_label.pack(
    fill="x",
    pady=3
)
strength_meter_label = tk.Label(
    result_frame,
    text="Password Strength",
    font=("Times New Roman", 10, "bold"),
    bg="#ffffff",
    anchor="w"
)
strength_meter_label.pack(
    fill="x",
    pady=(5, 0)
)
progress_frame = tk.Frame(
    result_frame,
    bg="white",
    height=18,
    highlightbackground="black",
    highlightthickness=1
)
progress_frame.pack(
    fill="x",
    pady=5
)
progress_frame.pack_propagate(False)
progress_fill = tk.Frame(
    progress_frame,
    bg="red",
    height=18
)
progress_fill.place(
    x=0,
    y=0,
    relheight=1,
    relwidth=0
)
generate_button = tk.Button(
    action_frame,
    text="🔑 Generate Strong Password",
    font=("Times New Roman", 10, "bold"),
    width=25,
    command=generate_new_password
)
generate_button.pack(
    pady=6
)
copy_button = tk.Button(
    action_frame,
    text="📋 Copy Password",
    font=("Times New Roman", 8, "bold"),
    width=20,
    command=copy_password
)
copy_button.pack(
    pady=5
)
clear_button = tk.Button(
    action_frame,
    text="🔄 Clear",
    font=("Times New Roman", 8, "bold"),
    width=15,
    command=clear_all
)
clear_button.pack(
    pady=5
)
update_progress_bar()
if __name__ == "__main__":
    window.mainloop()