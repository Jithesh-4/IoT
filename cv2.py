import cv2

cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read a frame.")
        break

    ##### SENSOR 1 #####
    x1, y1, w1, h1 = 50, 200, 200, 300
    cv2.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
    text = "Sensor 1 : 234 C"
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, (x1, y1 - 10), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

    ##### SENSOR 2 #####
    x2, y2, w2, h2 = 400, 200, 200, 300
    cv2.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)
    text = "Sensor 2 : 234 C"
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, (x2, y2 - 10), font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

    ##### SENSOR 3 #####
    x3, y3, w3, h3 = 750, 200, 200, 300
    cv2.rectangle(frame, (x3, y3), (x3 + w3, y3 + h3), (0, 0, 255), 2)
    text = "Sensor 3 : 234 C"
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, (x3, y3 - 10), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)


    cv2.imshow('Webcam', frame)

    # Press 'q' to exit the loop and close the webcam window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


change this code for three sensors to five sensors
