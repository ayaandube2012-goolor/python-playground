from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F8A89D"
RED = "#EF6748"
GREEN = "#379B46"
YELLOW = "#FFF3A7"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_value, text="00:00")
    checkmark_label.config(text="")
    timer_label.config(text="""POMODORO
TIMER""", fg=GREEN)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="BREAK", fg=GREEN)
        count_down(long_break_sec)
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
    elif reps % 2 == 0:
        timer_label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
    else:
        timer_label.config(text="WORK", fg=RED)
        count_down(work_sec)
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes = count // 60
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_value, text=str(f"{minutes}:{seconds}"))
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps // 2):
            mark += "✔"
        checkmark_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="""POMODORO
TIMER""", font=(FONT_NAME, 60, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_value = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', command=start_timer, highlightthickness=0, height=2, width=10)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', command=reset_timer, highlightthickness=0, height=2, width=10)
reset_button.grid(row=2, column=2)

checkmark_label = Label(font=(FONT_NAME, 20, 'normal'), bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)

window.mainloop()
