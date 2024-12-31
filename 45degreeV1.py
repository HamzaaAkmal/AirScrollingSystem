import cv2
import mediapipe as mp
import pyautogui
import time
import numpy as np

# Initialize mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

# Global variables
running = True
last_action_time = time.time()
last_y = None  # To calculate hand movement direction
SCROLL_SENSITIVITY = 50  # Sensitivity for scrolling (higher = more sensitive)
GESTURE_DELAY = 0.1  # Minimum delay between gestures
HAND_MOVEMENT_THRESHOLD = 0.02  # Threshold for detecting significant hand movement
ANGLE_THRESHOLD = 45  # Angle threshold for detecting upward/downward gestures
HOLD_THRESHOLD = 1  # Time in seconds for holding the gesture

def calculate_velocity(current_y, last_y):
    """Calculate the change in vertical position for smooth scrolling"""
    if last_y is None:
        return 0
    return current_y - last_y

def calculate_angle(landmark1, landmark2, landmark3):
    """Calculate the angle between three points (landmarks)"""
    v1 = np.array([landmark1.x - landmark2.x, landmark1.y - landmark2.y])
    v2 = np.array([landmark3.x - landmark2.x, landmark3.y - landmark2.y])
    angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
    return np.degrees(angle)

def process_hand_gesture(landmarks):
    """
    Detect gestures based on the hand landmarks.
    - Scroll up/down: Based on hand angle (45-degree angle up or down).
    - Zoom in/out: Pinch gesture.
    - Reset zoom: Wide pinch gesture.
    """
    global last_action_time, last_y
    current_time = time.time()

    if landmarks and (current_time - last_action_time) > GESTURE_DELAY:
        try:
            # Get the positions of the wrist, index, and middle fingers
            wrist = landmarks[mp_hands.HandLandmark.WRIST]
            index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            # Calculate the angle of the hand
            angle = calculate_angle(wrist, index_tip, middle_tip)

            # Scroll up/down based on the hand angle
            if angle > ANGLE_THRESHOLD and angle < 135:  # Between 45 and 135 degrees
                # If the hand is pointing upwards (scroll up)
                if index_tip.y < wrist.y:  # Hand pointing upwards
                    pyautogui.scroll(-SCROLL_SENSITIVITY)
                # If the hand is pointing downwards (scroll down)
                elif index_tip.y > wrist.y:  # Hand pointing downwards
                    pyautogui.scroll(SCROLL_SENSITIVITY)

            last_action_time = current_time

        except Exception as e:
            print(f"Error processing gesture: {e}")

def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened() and running:
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Convert the BGR image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Process the image and detect hands
        results = hands.process(image)

        # Draw the hand annotations on the image
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                process_hand_gesture(hand_landmarks.landmark)

        # Display the image
        cv2.imshow('Hand Gesture Control', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

## Soon Gonna work on buidling its gui version later 2025