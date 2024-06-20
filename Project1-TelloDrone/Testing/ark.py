from djitellopy import Tello
import cv2

# Initialize the Tello object
me = Tello()
me.connect()

# Start the video stream
me.streamoff()
me.streamon()

# Load the face detection model from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Get the frame from the Tello drone
    img = me.get_frame_read().frame
    img = cv2.resize(img, (640, 480))

    # Convert the frame to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw bounding boxes around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the frame with bounding boxes
    cv2.imshow("Tello Video Stream", img)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close OpenCV windows
me.streamoff()
cv2.destroyAllWindows()
me.end()