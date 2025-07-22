from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def restart_timer():
    global REPS
    REPS = 0
    window.after_cancel(TIMER)
    check.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
    if REPS % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global  TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_mark = ""
        work_sessions = math.floor(REPS/2)
        for n in range(work_sessions):
            check_mark += "✅"
        check.config(text=check_mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width= 200, height= 224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,100, image=tomato_img)
timer_text = canvas.create_text(100,120, text= "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)


timer = Label(text="Timer", font=(FONT_NAME, 50,), fg=GREEN, bg=YELLOW)
timer.grid(row=0, column=1)

start_button = Button(text= "Start", command=start_timer, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

restart_button = Button(text= "Restart", command=restart_timer,  highlightbackground=YELLOW)
restart_button.grid(row=2, column=2)

check = Label(bg=YELLOW)
check.grid(row=3, column=1)

window.mainloop()
