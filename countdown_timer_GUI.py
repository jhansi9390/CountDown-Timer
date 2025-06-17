import tkinter as tk
import time
import threading

# Global flags
stop_flag = False

def start_timer():
    global stop_flag
    stop_flag = False
    try:
        total_time = int(entry.get())
        countdown(total_time)
    except ValueError:
        label.config(text="Enter a valid number")

def countdown(total_time):
    global stop_flag
    while total_time > 0 and not stop_flag:
        mins = total_time // 60
        secs = total_time % 60
        timer_text = f"{mins:02d}:{secs:02d}"
        label.config(text=timer_text)
        root.update()
        time.sleep(1)
        total_time -= 1
    if not stop_flag:
        label.config(text="⏰ Time's up!")

def stop_timer():
    global stop_flag
    stop_flag = True
    label.config(text="🛑 Stopped")

def restart_timer():
    stop_timer()                      # Stop current countdown
    entry.delete(0, tk.END)          # Clear input field
    label.config(text="00:00")       # Reset the timer label

# GUI setup
root = tk.Tk()
root.title("Countdown Timer ⏳")
root.geometry("320x250")
root.resizable(False, False)

entry_label = tk.Label(root, text="Enter time in seconds:", font=("Arial", 12))
entry_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

label = tk.Label(root, text="00:00", font=("Arial", 28), fg="blue")
label.pack(pady=15)

# Button Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

start_btn = tk.Button(btn_frame, text="Start", font=("Arial", 12), width=8,
                      command=lambda: threading.Thread(target=start_timer).start())
start_btn.grid(row=0, column=0, padx=5)

stop_btn = tk.Button(btn_frame, text="Stop", font=("Arial", 12), width=8, command=stop_timer)
stop_btn.grid(row=0, column=1, padx=5)

restart_btn = tk.Button(btn_frame, text="Restart", font=("Arial", 12), width=8, command=restart_timer)
restart_btn.grid(row=0, column=2, padx=5)

root.mainloop()
