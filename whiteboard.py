import cv2
import mediapipe as mp
import numpy as np
import pyautogui

mp_hands = mp.solutions.hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)

_, img = cap.read()
img = cv2.resize(img, (screen_width, screen_height))
img_height, img_width, c = img.shape
output_img = np.ones((img_height,img_width,3))

prev_x = 0
prev_y = 0

while cv2.waitKey(1) != 27:
    _, img = cap.read()

    if not _:
        break
    img = cv2.resize(img, (screen_width, screen_height))
    img = cv2.flip(img, 1)
    res = mp_hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if res.multi_hand_landmarks:
        for hand_landmark in res.multi_hand_landmarks:
            landmarks = hand_landmark.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * img_width)
                y = int(landmark.y * img_height)
                if id == 4:
                    cv2.circle(img, (x,y), 3, (0,0,255), 10)
                    thumb_y = y
                    thumb_x = x
                if id == 8:
                    cv2.circle(img, (x,y), 3, (0,255,0), 10)
                    index_y = y
                    index_x = x
                    if abs(index_y - thumb_y) < 60 and abs(index_x - thumb_x) < 60:
                        if(prev_x == 0 and prev_y == 0):
                            cv2.circle(output_img, (x,y), 2, (0,255,0))
                        else:
                            cv2.line(output_img, (prev_x, prev_y), (x,y), (0,255,0), 5)
                    prev_x = x
                    prev_y = y
                    pyautogui.moveTo(x+10,y+30)

                # if id == 12:
                #     cv2.circle(img, (x,y), 3, (255,0,0), 10)
                        
    cv2.imshow("WhiteBoard", img)
    cv2.imshow("Output", output_img)