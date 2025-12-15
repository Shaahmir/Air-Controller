import cv2
import mediapipe as mp
import pyautogui
import time

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode = False,
    model_complexity = 1,
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.7,
    max_num_hands = 1
)

def main ():
    cap = cv2.VideoCapture(0)
    try:

        while cap.isOpened():

            ret, frame = cap.read()

            if not ret:
                break

            frame = cv2.flip(frame, 1)
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            processed = hands.process(frameRGB)
            landmarks_list = []

            if processed.multi_hand_landmarks:
                print(processed.multi_hand_landmarks)

            cv2.imshow("Window", frame)

            if (cv2.waitKey(1) & 0xFF) == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()