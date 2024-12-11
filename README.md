# Air Scrolling System

This project introduces a futuristic approach to user interaction by replacing traditional scrolling mechanisms with hand gesture controls. Using a webcam, computer vision, and machine learning tools, the program allows users to scroll and perform basic actions without touching a mouse or keyboard.

---

## Features

- **Gesture-Driven Scrolling**  
  Detects upward and downward hand movements to scroll seamlessly through content.
  
- **Customizable Sensitivity**  
  Adjust the scroll sensitivity, gesture delay, and detection thresholds to suit your needs.

- **Real-Time Hand Tracking**  
  Visual feedback of hand landmarks ensures accurate gesture recognition.

---

## Current Development

The system is evolving to include more features:
1. **Training Improvements**: Enhanced gesture recognition for accurate scrolling with precise 45-degree upward and downward movements.
2. **Zoom and Tab Switching**: Upcoming features will allow zooming and switching between tabs using gestures.
3. **Full PC Control**: Future updates will integrate full PC navigation and control, enabling a complete hands-free experience.

Stay tuned for regular updates as these features are currently under development!

---

## Why Use This System?

1. **Innovative Interaction**: A step towards intuitive, futuristic user interfaces.
2. **Accessibility**: Ideal for users with limited mobility or who prefer touchless control.
3. **Enhanced Immersion**: Perfect for modern workflows involving AR, VR, or creative tasks.
4. **Convenience**: No need for physical input devices—control your device with gestures.

---
## Requirements 
1. Python 3.7+
2. Webcam
3. Libraries: OpenCV, Mediapipe, PyAutoGUI, NumPy

## Installation

Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/HamzaaAkmal/AirScrollingSystem.git
   cd AirScrollingSystem

## Customization

You can adjust key parameters in the script to modify the behavior:

- **Scroll Sensitivity**: Adjust with `SCROLL_SENSITIVITY` (default: `50`), which determines the intensity of scroll movements.
- **Gesture Delay**: Set using `GESTURE_DELAY` (default: `0.1` seconds) to control the minimum delay between consecutive gestures.
- **Angle Threshold**: Modify via `ANGLE_THRESHOLD` (default: `45` degrees) to define the range of upward or downward gestures.

---

## Future Enhancements

The following features are under development and will be added in future updates:

- **Zoom and Panning Gestures**: Intuitive gestures to zoom in/out and pan across the screen.
- **Multimedia Control**: Hand gestures for play, pause, volume control, and other media actions.
- **Smart Home Integration**: Use hand gestures to interact with smart home devices for a completely touchless experience.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

This project leverages the power of several amazing tools and libraries:

- [OpenCV](https://opencv.org/): Real-time computer vision processing.
- [Mediapipe](https://mediapipe.dev/): Machine learning solutions for hand tracking.
- [PyAutoGUI](https://pyautogui.readthedocs.io/): Screen automation library for Python.
- [NumPy](https://numpy.org/): Essential scientific computing library.

---

Feel free to contribute by submitting issues or pull requests. Let's make interaction more intuitive and futuristic!

