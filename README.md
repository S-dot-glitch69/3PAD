# Shabnam Khan
# 10/08/2026

import tkinter as tk
from tkinter import messagebox
import os

# Colours

pink = "#FFD9E6"
white = "#FFFFFF"
black = "#000000"

# Main window

root = tk.Tk()
root.geometry("900x600")
root.title("Awesome Math Game")
root.configure(bg=pink)

# Variables

username = ""

correct = 0
wrong = 0

current_question = 0
questions = []

question_image = None

# Correct answers

answers = {
    1: "parallelogram",
    2: "62038",
    3: "7",
    4: "3w²+5w+2",
    5: "3x³/5x⁷",
    6: "160",
    7: "509.22",
    8: "50",
    9: "x = -2, -3"
}

# Clear the screen

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


# Login

def login():
    global username

    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "":
        messagebox.showinfo("Login", "Please enter a username.")
        return

    if password == "":
        messagebox.showinfo("Login", "Please enter a password.")
        return

    level_screen()


# Login screen

def login_screen():
    clear_screen()

    heading = tk.Label(
        root,
        text="Welcome to Awesome Math Game",
        font=("Liberation Serif", 40, "bold"),
        bg=pink,
        fg=black
    )

    heading.place(
        relx=0.5,
        y=70,
        anchor="center"
    )

    subtitle = tk.Label(
        root,
        text="Please Login",
        font=("Liberation Serif", 24),
        bg=pink,
        fg=black
    )

    subtitle.place(
        relx=0.5,
        y=125,
        anchor="center"
    )

    # Login box

    login_box = tk.Frame(
        root,
        bg=white,
        bd=3,
        relief="ridge",
        width=450,
        height=300
    )

    login_box.place(
        relx=0.5,
        rely=0.58,
        anchor="center"
    )

    # Username

    username_label = tk.Label(
        login_box,
        text="Username",
        font=("Liberation Serif", 20, "bold"),
        bg=white,
        fg=black
    )

    username_label.place(
        x=70,
        y=40
    )

    global username_entry

    username_entry = tk.Entry(
        login_box,
        font=("Liberation Serif", 18),
        width=20,
        bd=3,
        bg=pink,
        fg=black
    )

    username_entry.place(
        x=70,
        y=75
    )

    # Password

    password_label = tk.Label(
        login_box,
        text="Password",
        font=("Liberation Serif", 20, "bold"),
        bg=white,
        fg=black
    )

    password_label.place(
        x=70,
        y=120
    )

    global password_entry

    password_entry = tk.Entry(
        login_box,
        font=("Liberation Serif", 18),
        width=20,
        bd=3,
        show="*",
        bg=pink,
        fg=black
    )

    password_entry.place(
        x=70,
        y=155
    )

    # Login button

    login_button = tk.Button(
        login_box,
        text="Login",
        font=("Liberation Serif", 18, "bold"),
        width=12,
        bg=pink,
        fg=black,
        bd=3,
        command=login
    )

    login_button.place(
        relx=0.5,
        y=220,
        anchor="center"
    )


# Level screen

def level_screen():
    clear_screen()

    heading = tk.Label(
        root,
        text="Different Levels",
        font=("Liberation Serif", 40, "italic", "bold"),
        bg=pink,
        fg=black
    )

    heading.place(
        relx=0.5,
        y=55,
        anchor="center"
    )

    subtitle = tk.Label(
        root,
        text="Select a Level",
        font=("Liberation Serif", 24),
        bg=pink,
        fg=black
    )

    subtitle.place(
        relx=0.5,
        y=105,
        anchor="center"
    )

    # Main box

    menu_box = tk.Frame(
        root,
        bg=white,
        bd=3,
        relief="ridge",
        width=800,
        height=350
    )

    menu_box.place(
        relx=0.5,
        rely=0.60,
        anchor="center"
    )

    # Welcome username

    welcome = tk.Label(
        menu_box,
        text="Welcome, " + username,
        font=("Liberation Serif", 20, "bold"),
        bg=white,
        fg=black
    )

    welcome.place(
        relx=0.5,
        y=30,
        anchor="center"
    )

    # Easy

    easy_button = tk.Button(
        menu_box,
        text="Easy",
        font=("Liberation Serif", 24, "bold"),
        width=12,
        height=2,
        bg=pink,
        fg=black,
        bd=3,
        command=lambda: start_level("Easy", [1, 2, 3])
    )

    easy_button.place(
        relx=0.20,
        y=150,
        anchor="center"
    )

    # Medium

    medium_button = tk.Button(
        menu_box,
        text="Medium",
        font=("Liberation Serif", 24, "bold"),
        width=12,
        height=2,
        bg=pink,
        fg=black,
        bd=3,
        command=lambda: start_level("Medium", [4, 5, 6, 7])
    )

    medium_button.place(
        relx=0.50,
        y=150,
        anchor="center"
    )

    # Hard

    hard_button = tk.Button(
        menu_box,
        text="Hard",
        font=("Liberation Serif", 24, "bold"),
        width=12,
        height=2,
        bg=pink,
        fg=black,
        bd=3,
        command=lambda: start_level("Hard", [8, 9])
    )

    hard_button.place(
        relx=0.80,
        y=150,
        anchor="center"
    )

    # Scoreboard

    scoreboard_button = tk.Button(
        menu_box,
        text="Scoreboard",
        font=("Liberation Serif", 18, "bold"),
        width=14,
        bg=pink,
        fg=black,
        bd=3,
        command=scoreboard
    )

    scoreboard_button.place(
        relx=0.5,
        y=270,
        anchor="center"
    )

    # Exit

    exit_button = tk.Button(
        menu_box,
        text="Exit",
        font=("Liberation Serif", 16, "bold"),
        width=8,
        bg=white,
        fg=black,
        bd=3,
        command=exit_game
    )

    exit_button.place(
        relx=0.5,
        y=315,
        anchor="center"
    )


# Play a level

def start_level(level_name, level_questions):
    global questions
    global current_question
    global correct
    global wrong

    questions = level_questions
    current_question = 0

    correct = 0
    wrong = 0

    show_question(level_name)


# Show question

def show_question(level_name):
    global question_image
    global User_answer

    clear_screen()

    question_number = questions[current_question]

    # Back button

    back_button = tk.Button(
        root,
        text="Back",
        font=("Liberation Serif", 18, "bold"),
        width=8,
        bg=white,
        fg=black,
        bd=3,
        command=level_screen
    )

    back_button.place(
        x=20,
        y=20
    )

    # Level name

    level_label = tk.Label(
        root,
        text=level_name + " Level",
        font=("Liberation Serif", 26, "bold"),
        bg=pink,
        fg=black
    )

    level_label.place(
        relx=0.5,
        y=35,
        anchor="center"
    )

    # Score

    score_label = tk.Label(
        root,
        text="Score: " + str(correct),
        font=("Liberation Serif", 20, "bold"),
        bg=pink,
        fg=black
    )

    score_label.place(
        x=760,
        y=25
    )

    # Question image

    image_path = "Question " + str(question_number) + ".png"

    if os.path.exists(image_path):

        question_image = tk.PhotoImage(file=image_path)

        question_image = question_image.subsample(2, 2)

        question = tk.Label(
            root,
            image=question_image,
            bg=pink
        )

        question.place(
            x=40,
            y=110
        )

    else:

        question = tk.Label(
            root,
            text="Question " + str(question_number),
            font=("Liberation Serif", 28, "bold"),
            bg=white,
            fg=black,
            width=18,
            height=8,
            bd=3,
            relief="ridge"
        )

        question.place(
            x=40,
            y=110
        )

    # Question number

    number = tk.Label(
        root,
        text="Question "
        + str(current_question + 1)
        + " of "
        + str(len(questions)),
        font=("Liberation Serif", 18, "bold"),
        bg=pink,
        fg=black
    )

    number.place(
        x=500,
        y=105
    )

    # Answer label

    answer_label = tk.Label(
        root,
        text="Answer",
        font=("Liberation Serif", 20, "bold"),
        bg=pink,
        fg=black
    )

    answer_label.place(
        x=510,
        y=155
    )

    # Answer box

    User_answer = tk.Entry(
        root,
        font=("Liberation Serif", 18),
        width=13,
        bd=3,
        bg=white,
        fg=black
    )

    User_answer.place(
        x=490,
        y=195
    )

    User_answer.focus()

    # Submit

    submit_button = tk.Button(
        root,
        text="Submit",
        font=("Liberation Serif", 18, "bold"),
        width=11,
        bg=white,
        fg=black,
        bd=3,
        command=lambda: check_answer(level_name)
    )

    submit_button.place(
        x=500,
        y=250
    )

    # Exit

    exit_button = tk.Button(
        root,
        text="Exit",
        font=("Liberation Serif", 18, "bold"),
        width=8,
        bg=white,
        fg=black,
        bd=3,
        command=exit_game
    )

    exit_button.place(
        x=520,
        y=320
    )


# Check answer

def check_answer(level_name):
    global current_question
    global correct
    global wrong

    answer = User_answer.get().strip().lower()

    question_number = questions[current_question]

    correct_answer = answers[question_number].strip().lower()

    if answer == "":
        messagebox.showinfo(
            "Answer",
            "Please enter an answer."
        )
        return

    if answer == correct_answer:
        correct = correct + 1

        messagebox.showinfo(
            "Correct",
            "Correct answer!"
        )

    else:
        wrong = wrong + 1

        messagebox.showinfo(
            "Incorrect",
            "Incorrect answer!"
        )

    current_question = current_question + 1

    if current_question == len(questions):
        level_finished(level_name)
    else:
        show_question(level_name)


# Level finished

def level_finished(level_name):
    clear_screen()

    heading = tk.Label(
        root,
        text=level_name + " Level Complete!",
        font=("Liberation Serif", 36, "bold"),
        bg=pink,
        fg=black
    )

    heading.place(
        relx=0.5,
        y=70,
        anchor="center"
    )

    # Results box

    result_box = tk.Frame(
        root,
        bg=white,
        bd=3,
        relief="ridge",
        width=400,
        height=270
    )

    result_box.place(
        relx=0.5,
        rely=0.55,
        anchor="center"
    )

    # Username

    result_username = tk.Label(
        result_box,
        text="Username: " + username,
        font=("Liberation Serif", 20, "bold"),
        bg=white,
        fg=black
    )

    result_username.place(
        relx=0.5,
        y=35,
        anchor="center"
    )

    # Score

    result_score = tk.Label(
        result_box,
        text="Score: "
        + str(correct)
        + " / "
        + str(len(questions)),
        font=("Liberation Serif", 22, "bold"),
        bg=white,
        fg=black
    )

    result_score.place(
        relx=0.5,
        y=80,
        anchor="center"
    )

    # Correct answers

    correct_label = tk.Label(
        result_box,
        text="Correct: " + str(correct),
        font=("Liberation Serif", 20),
        bg=white,
        fg=black
    )

    correct_label.place(
        relx=0.5,
        y=125,
        anchor="center"
    )

    # Wrong answers

    wrong_label = tk.Label(
        result_box,
        text="Wrong: " + str(wrong),
        font=("Liberation Serif", 20),
        bg=white,
        fg=black
    )

    wrong_label.place(
        relx=0.5,
        y=160,
        anchor="center"
    )

    # Back to levels

    back_button = tk.Button(
        result_box,
        text="Back to Levels",
        font=("Liberation Serif", 17, "bold"),
        width=14,
        bg=pink,
        fg=black,
        bd=3,
        command=level_screen
    )

    back_button.place(
        relx=0.5,
        y=215,
        anchor="center"
    )


# Scoreboard

def scoreboard():
    clear_screen()

    title = tk.Label(
        root,
        text="SCOREBOARD",
        font=("Liberation Serif", 36, "bold"),
        bg=pink,
        fg=black
    )

    title.pack(pady=25)

    scoreboard_box = tk.Frame(
        root,
        bg=white,
        bd=3,
        relief="ridge",
        width=650,
        height=280
    )

    scoreboard_box.place(
        relx=0.5,
        rely=0.55,
        anchor="center"
    )

    # Headings

    username_title = tk.Label(
        scoreboard_box,
        text="USERNAME",
        font=("Liberation Serif", 18, "bold"),
        bg=white,
        fg=black
    )

    username_title.place(
        x=50,
        y=30
    )

    score_title = tk.Label(
        scoreboard_box,
        text="SCORE",
        font=("Liberation Serif", 18, "bold"),
        bg=white,
        fg=black
    )

    score_title.place(
        x=280,
        y=30
    )

    correct_title = tk.Label(
        scoreboard_box,
        text="RIGHT",
        font=("Liberation Serif", 18, "bold"),
        bg=white,
        fg=black
    )

    correct_title.place(
        x=390,
        y=30
    )

    wrong_title = tk.Label(
        scoreboard_box,
        text="WRONG",
        font=("Liberation Serif", 18, "bold"),
        bg=white,
        fg=black
    )

    wrong_title.place(
        x=510,
        y=30
    )

    # Player information

    player_name = tk.Label(
        scoreboard_box,
        text=username,
        font=("Liberation Serif", 18, "bold"),
        bg=pink,
        fg=black,
        width=15
    )

    player_name.place(
        x=25,
        y=85
    )

    player_score = tk.Label(
        scoreboard_box,
        text=str(correct),
        font=("Liberation Serif", 18, "bold"),
        bg=pink,
        fg=black,
        width=6
    )

    player_score.place(
        x=270,
        y=85
    )

    player_correct = tk.Label(
        scoreboard_box,
        text=str(correct),
        font=("Liberation Serif", 18, "bold"),
        bg=pink,
        fg=black,
        width=6
    )

    player_correct.place(
        x=375,
        y=85
    )

    player_wrong = tk.Label(
        scoreboard_box,
        text=str(wrong),
        font=("Liberation Serif", 18, "bold"),
        bg=pink,
        fg=black,
        width=6
    )

    player_wrong.place(
        x=495,
        y=85
    )

    # Back button

    back_button = tk.Button(
        root,
        text="Back",
        font=("Liberation Serif", 18, "bold"),
        width=10,
        bg=white,
        fg=black,
        bd=3,
        command=level_screen
    )

    back_button.place(
        relx=0.5,
        y=530,
        anchor="center"
    )


# Exit

def exit_game():
    answer = messagebox.askyesno(
        "Exit",
        "Are you sure you want to exit?"
    )

    if answer:
        root.destroy()


# Start the program

login_screen()

root.mainloop()
