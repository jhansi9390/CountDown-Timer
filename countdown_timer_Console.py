import time

def countdown(seconds):
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end='\r')  # overwrite line
        time.sleep(1)
        seconds -= 1

    print("⏰ Time's up!")

# Main program
try:
    user_input = int(input("Enter time in seconds: "))
    countdown(user_input)
except ValueError:
    print("Please enter a valid number!")
