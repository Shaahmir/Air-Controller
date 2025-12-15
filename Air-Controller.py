import cv2
import mediapipe as mp #importing with a nickname/variable mp
import pyautogui
import time #python default library

#making and configuring hand model

mpHands = mp.solutions.hands
hands = mpHands.Hands (
    static_image_mode = False, #for video capture
    model_complexity = 1, #moderate details
    min_detection_confidence = 0.7, #detect on 70% surety
    min_tracking_confidence = 0.7, #track on 70% surity
    max_num_hands = 1 #maximum numbers of hands to detect and track
)

#create a gesture recognize dictionary:

gesture_dictionary = {
    "volume_up": [0, 1, 1, 0, 0],
    "volume_down": [0, 0, 0, 1, 1],
    "play": [0, 0, 0, 0, 0],
    "pause": [1, 1, 1, 1, 1],
    "skip": [0, 0, 0, 0, 1],
    "previous": [1, 1, 1, 1, 0],
    "screenshot": [0, 1, 1, 1, 0],
    "scroll": [0, 1, 0, 0, 0]
}
    
#finger detection function:

def finger_detection(landmarks_list,fingers):

    #========== for thumb: ===========

    if landmarks_list[4][0] < landmarks_list[3][0]:
        fingers.append(1)
    else:
        fingers.append(0)

    #=========== for index finger: ===========

    if landmarks_list[8][1] < landmarks_list[6][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    #=========== for middle finger: ===========

    if landmarks_list[12][1] < landmarks_list[10][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    #=========== for ring finger: ===========

    if landmarks_list[16][1] < landmarks_list[14][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    #=========== for pinky finger: ===========

    if landmarks_list[20][1] < landmarks_list[18][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    print("Detected Fingers: ", fingers)

#Volume controller function:

def volume_control(fingers,frame):
 
 #=========== for volume up: ===========

 if fingers== gesture_dictionary["volume_up"]:
    pyautogui.press("volumeup")
    cv2.putText(
      frame, #frame to put text on
      "GESTURE: VOLUME UP", #string to show
      (10,50), #where to show on screen
      cv2.FONT_HERSHEY_SIMPLEX, #font type
      1, #scaling of text
      (255,255,255), #colour of text
      2 #thickness of text
    )

#=========== for volume down: ===========
  
 elif fingers== gesture_dictionary["volume_down"]:
    pyautogui.press("volumedown")
    cv2.putText(
        frame, #frame to put text on
        "GESTURE: VOLUME DOWN", #string to show
        (10,50), #where to show on screen
        cv2.FONT_HERSHEY_SIMPLEX, #font type
        1, #scaling of text
        (255,255,255), #colour of text
        2 #thickness of text
    )

#hands action function:

def action(fingers,frame, prev_fingers):
  
  #call volume control function:
  volume_control(fingers, frame)

  if fingers != prev_fingers:

    #=========== for screenshot: ===========

    if fingers == gesture_dictionary["screenshot"]:
      screenshot=pyautogui.screenshot()
      screenshot.save(f"Screenshot {(int(time.time() * 1000 ))}")
      cv2.putText(
        frame, #frame to put text on
        "GESTURE: SCREENSHOT", #string to show
        (10,50), #where to show on screen
        cv2.FONT_HERSHEY_SIMPLEX, #font type
        1, #scaling of text
        (255,255,255), #colour of text
        2 #thickness of text
    )

    #=========== for scroll: ===========

    elif fingers==gesture_dictionary["scroll"]:
        pyautogui.press("pagedown")
        cv2.putText(
            frame, #frame to put text on
            "GESTURE: SCROLL", #string to show
            (10,50), #where to show on screen
            cv2.FONT_HERSHEY_SIMPLEX, #font type
            1, #scaling of text
            (255,255,255), #colour of text
            2 #thickness of text
        )
        
    #=========== for previous video: ===========
        
    elif fingers == gesture_dictionary["previous"]:
         pyautogui.hotkey("shift","p")
         cv2.putText(
             frame, #frame to put text on
            "GESTURE: PREVIOUS VIDEO", #string to show
            (10,50), #where to show on screen
            cv2.FONT_HERSHEY_SIMPLEX, #font type
            1, #scaling of text
            (255,255,255), #colour of text
            2 #thickness of text
        )
         
    #=========== for pause: ===========
         
    elif fingers == gesture_dictionary["pause"]:
         pyautogui.press("space")
         cv2.putText(
            frame, #frame to put text on
            "GESTURE: PAUSE", #string to show
            (10,50), #where to show on screen
            cv2.FONT_HERSHEY_SIMPLEX, #font type
            1, #scaling of text
            (255,255,255), #colour of text
            2 #thickness of text
        )
         
    #=========== for play: ===========
         
    elif fingers == gesture_dictionary["play"]:
         pyautogui.press("space")
         cv2.putText(
            frame, #frame to put text on
            "GESTURE: PLAY", #string to show
            (10,50), #where to show on screen
            cv2.FONT_HERSHEY_SIMPLEX, #font type
            1, #scaling of text
            (255,255,255), #colour of text
            2 #thickness of text
        )
         
    #=========== for skip: ===========
         
    elif fingers == gesture_dictionary["skip"]:
         pyautogui.press("shift","n")
         cv2.putText(
            frame, #frame to put text on
            "GESTURE: SKIP", #string to show
            (10,50), #where to show on screen
            cv2.FONT_HERSHEY_SIMPLEX, #font type
            1, #scaling of text
            (255,255,255), #colour of text
            2 #thickness of text
        )

def main ():

    cap = cv2.VideoCapture(0) #capture from primary camera

    try:
        prev_fingers = None #to keep track of previous gesture

        #loop to capture each frame
        while cap.isOpened():

            ret, frame = cap.read() #unpacking of list

            if not ret: #break in case frame is not receiving
                break

            frame = cv2.flip(frame, 1) #flip camera horizontally
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #changing format because mediapipe requires Rgb format

            draw = mp.solutions.drawing_utils #variable shortcut

            processed = hands.process(frameRGB) #processing hand from each frame
            landmarks_list = [] #empty landmarks list

            if processed.multi_hand_landmarks:
                hand_landmarks = processed.multi_hand_landmarks[0] #first detected hand
                draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS) #drawing connections on hand
                
                for lm in hand_landmarks.landmark: #loop to get each landmark
                    landmarks_list.append((lm.x, lm.y)) #appending it to landmarks list

                fingers = [] #empty fingers list
                finger_detection(landmarks_list, fingers) #detecting which finger is open and which one is closed
                action(fingers, frame, prev_fingers ) #detecting which action to perform

                prev_fingers = fingers.copy() #copying fingers to prev finger

            cv2.imshow("Air controller", frame) #showing the frame

            if (cv2.waitKey(1) & 0xFF) == ord('q'): #check if q is pressed
                break #if yes then break

    finally:
        cap.release() #release the camera
        cv2.destroyAllWindows() #destroy all open cvs window

if __name__ == "__main__": #check if am i running or am i being import
    main()