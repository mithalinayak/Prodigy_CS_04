# Keylogger with GUI

This project is a simple keylogger application with a graphical user interface (GUI) built using Python's `tkinter` library. The application logs keystrokes to a file and displays them in real-time within the GUI.

## Features

- **Real-Time Key Logging**: Captures and logs every key pressed on the keyboard.
- **GUI Display**: A `tkinter`-based text box displays the logged keys in real-time.
- **Logging to File**: All keystrokes are saved in a `keylog.txt` file with timestamps.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Requirements

- Python 3.x
- The following Python packages are required:
  - `tkinter`
  - `pynput`
  - `logging` (part of Python standard library)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/keylogger-gui.git
   cd keylogger-gui
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     myenv\Scripts\activate
     ```
   - **Linux/MacOS**:
     ```bash
     source myenv/bin/activate
     ```

4. **Install the required packages**:
   ```bash
   pip install pynput
   ```

5. **Run the application**:
   ```bash
   python keylogger_gui.py
   ```

## Usage

1. **Start Logging**: Run the application to start logging keystrokes.
2. **View Logs in Real-Time**: The GUI will display each key press as it is logged.
3. **Save Logs**: All key presses are automatically saved to `keylog.txt` in the same directory.
4. **Exit the Application**: Press the `ESC` key to stop the keylogger and exit the application.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the `pynput` library to capture keyboard events.
- The GUI is created with Python's `tkinter` library.
