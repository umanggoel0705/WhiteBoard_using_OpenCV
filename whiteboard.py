import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

mp_model = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.6)

cap = cv2.VideoCapture(0)

while cv2.waitKey(1) != 27:
    flag, img = cap.read()
    if not flag:
        break
    img = cv2.flip(img, 1)
    res = mp_model.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if res.multi_hand_landmarks:
        for hand_landmark in res.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS,
                                      mp_drawing_styles.get_default_hand_landmarks_style(),
                                      mp_drawing_styles.get_default_hand_connections_style())
    cv2.imshow("WhiteBoard", img)