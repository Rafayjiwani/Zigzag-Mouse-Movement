# Zigzag Mouse Movement

## Overview
This Python script enables the generation of zigzag mouse movement patterns on the screen. It utilizes the PyAutoGUI library to control the mouse cursor and creates zigzag movements based on specified parameters.

## Features
- Generates zigzag mouse movement patterns on the screen.
- Customizable parameters such as zigzag height, width, and speed.
- Can be used for testing, demonstration, or fun purposes.

## Installation
1. Ensure you have Python installed on your system.
2. Install the required dependencies:
    ```
    pip install pyautogui
    ```
3. Clone this repository or download the `zigzag_mouse_movement.py` file.

## Usage
1. Import the `zigzag_move_mouse` function from `zigzag_mouse_movement.py`.
2. Call the `zigzag_move_mouse` function with the desired count parameter.
3. Adjust parameters as needed for different zigzag movement patterns.

Example:
```python
from zigzag_mouse_movement import zigzag_move_mouse

# Generate a zigzag mouse movement with a count of 5
zigzag_move_mouse(5)
