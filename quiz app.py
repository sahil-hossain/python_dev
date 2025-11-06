import tkinter as tk

# Quiz Data
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Who invented Computer?",
        "options": ["Newton", "Charles Babbage", "Einstein", "Edison"],
        "answer": "Charles Babbage"
    },
    {
        "question": "Which planet is red planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    }
]

current_q = 0
score = 0

def load_question():
    global current_q
    q = questions[current_q]
    question_label.config(text=q["question"])

    for i in range(4):
        option_buttons[i].config(text=q["options"][i])


def check_answer(selected_option):
    global current_q, score

    if selected_option == questions[current_q]["answer"]:
        score_label.config(text=f"Score: {score + 1}")
        score += 1

    current_q += 1

    if current_q < len(questions):
        load_question()
    else:
        question_label.config(text="Quiz Finished!")
        for btn in option_buttons:
            btn.config(state="disabled")
        final_label.config(text=f"Your Final Score: {score}/{len(questions)}")


# Window
root = tk.Tk()
root.title("Python Quiz App")
root.geometry("350x350")

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=300)
question_label.pack(pady=20)

option_buttons = []

for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 12), width=25,
                    command=lambda i=i: check_answer(option_buttons[i].cget("text")))
    btn.pack(pady=5)
    option_buttons.append(btn)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
score_label.pack(pady=10)

final_label = tk.Label(root,text="", font =("Arial", 14))
final_label.pack(pady=10)

load_question()
root.mainloop()