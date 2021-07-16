import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)
while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        print("Could not access the camera.")

    results = hands.process(frame)

    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('MediaPipe Hands', frame)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()