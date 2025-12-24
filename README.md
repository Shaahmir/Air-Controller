# Air-Controller - A Gesture Detection System (Python)

A Real-Time **Hand Gesture Control System** – A cutting-edge Python project leveraging **OpenCV** and **MediaPipe** to bring intuitive, touch-free control to your computer. This system recognizes a variety of predefined hand gestures and seamlessly maps them to practical actions, including **volume adjustment**, **brightness control**, **media playback (play/pause, next/previous)**, **scrolling**, **screenshots**, and even precise **cursor control with left and right clicks**. Transform your hand movements into a powerful, natural interface and experience the next level of interactive computing.

---

## Features

- Real-time hand tracking using webcam
- Finger-based gesture recognition
- Media & system control using gestures
- Lightweight and beginner-friendly logic
- Easily extendable gesture dictionary

---

## Gesture Logic

Each gesture is represented using a **5-element binary list** corresponding to finger states:

- `1` → Finger is **up**
- `0` → Finger is **down**

---

## Air Mouse Controller

Activate the **Air Mouse Controller** by pressing **Spacebar**. Once activated, your cursor will track the movement of your **index finger**.

### Gestures
- **Left Click:** Open your **thumb** while keeping the **index finger upright**, and close the remaining fingers.  
- **Right Click:** Raise your **middle finger** while keeping the **index finger upright**, and close the other fingers.  

### Exit
To exit **Air Mouse Controller** mode, either press **ESC** or make a **fist**.

---

### Gesture Dictionary

```python
gesture_dictionary = {
    "volume_up": [0, 1, 1, 0, 0],
    "volume_down": [0, 0, 0, 1, 1],
    "play": [0, 0, 0, 0, 0],
    "pause": [1, 1, 1, 1, 1],
    "skip": [0, 0, 0, 0, 1],
    "previous": [1, 1, 1, 1, 0],
    "screenshot": [0, 1, 1, 1, 0],
    "scroll": [0, 1, 0, 0, 0],
    "brightness_up" : [1, 1, 0, 0, 0],
    "brightness_down" : [1, 0, 1, 1, 1]
}
```
### Cursor Controller Dictionary

```python
cursor_controller = {
    "move_cursor": [0, 1, 0, 0, 0],
    "left_click": [1, 1, 0, 0, 0],
    "right_click": [0, 1, 1, 0, 0],
    "stop": [0, 0, 0, 0, 0]
}
```

---

## Libraries / Requirements

This project uses the following Python libraries:

- [`cv2`](https://pypi.org/project/opencv-python/): OpenCV library for real-time computer vision.  
- [`mediapipe`](https://pypi.org/project/mediapipe/): For hand tracking and gesture recognition.  
- [`pyautogui`](https://pypi.org/project/PyAutoGUI/): To control mouse movements and clicks.  
- [`screen_brightness_control`](https://pypi.org/project/screen-brightness-control/): To adjust screen brightness programmatically.  
- [`time`](https://docs.python.org/3/library/time.html) (Python built-in library): For timing and delays.

---


## Installation & Run

Install all required dependencies:

```bash
pip install opencv-python mediapipe pyautogui screen-brightness-control
```

## Run the Project

```bash
python Air-Controller.py
```
---
