import cv2
import mediapipe as mp
import time
import controller as cnt  # Import your custom controller module

# Wait for a second before starting to allow the camera to initialize
time.sleep(1.0)

# Initialize mediapipe hands module
mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

# Define the finger tip landmark IDs
tipIds = [4, 8, 12, 16, 20]

# Open the webcam
video = cv2.VideoCapture(0)

# Start hand detection
with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        # Read a frame from the webcam
        ret, image = video.read()

        # Convert the frame to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Process the frame to detect hands
        results = hands.process(image)

        # Make the frame writable again
        image.flags.writeable = True

        # Convert the frame back to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        lmList = []

        # If hands are detected, process each hand
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)

        fingers = []

        # If landmarks are detected, determine finger positions
        if len(lmList) != 0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # Count the number of extended fingers
            total = fingers.count(1)

            # Call the relay function from the controller module with the total count of fingers
            cnt.relay(total)

            # Display the finger count and relay status on the frame
            if total in range(6):
                cv2.rectangle(image, (20, 300), (270, 425), (0, 0, 0), cv2.FILLED)
                cv2.putText(image, str(total), (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
                cv2.putText(image, "relay", (100, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

        # Display the frame
        cv2.imshow("Frame", image)

        # Check for key press to exit the loop
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

# Release the webcam and close all windows
video.release()
cv2.destroyAllWindows()
