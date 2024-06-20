from djitellopy import Tello
import cv2

# Create a Tello object
tello = Tello()

# Connect to the Tello drone
tello.connect()

# Start the video stream
tello.streamon()

# Get the video stream frame reader
frame_read = tello.get_frame_read()

while True:
    # Get the current frame
    frame = frame_read.frame

    # Display the frame
    cv2.imshow("Tello Video Stream", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream
tello.streamoff()

# Close all OpenCV windows
cv2.destroyAllWindows()

# End the connection
tello.end()
