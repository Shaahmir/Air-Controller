# Air-Controller - A Gesture Detection System (Python)

A real-time **hand gesture detection system** built using **Python**, **OpenCV**, and **MediaPipe**.  
This project recognizes predefined hand gestures and maps them to system/media actions such as volume control, play/pause, scrolling, and screenshots.

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

### Gesture Dictionary

```python
gesture_dictionary = {
    "volume_up":    [0, 1, 1, 0, 0],
    "volume_down":  [0, 0, 0, 1, 1],
    "play":         [0, 0, 0, 0, 0],
    "pause":        [1, 1, 1, 1, 1],
    "skip":         [0, 0, 0, 0, 1],
    "previous":     [1, 1, 1, 1, 0],
    "screenshot":   [0, 1, 1, 1, 0],
    "scroll":       [0, 1, 0, 0, 0],
    "brightness_up" : [1, 1, 0, 0, 0],
    "brightness_down" : [1, 0, 1, 1, 1]
}
```

## Installation & Run

Install all required dependencies:

```bash
pip install opencv-python mediapipe pyautogui screen-brightness-control
```

## Run the Project

```bash
python Air-Controller.py
```
