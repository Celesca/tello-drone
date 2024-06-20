from djitellopy import Tello
import pygame
import time

# Initialize Pygame
pygame.init()

# Initialize the Tello drone
tello = Tello()

# Connect to the Tello drone
tello.connect()

# Print the battery percentage
print(f'Battery: {tello.get_battery()}%')

# Take off
tello.takeoff()

# Define constants for movement speeds
SPEED = 50  # Movement speed in cm/s

# Function to handle keyboard events
def handle_events():
    global SPEED

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                tello.move_forward(SPEED)
            elif event.key == pygame.K_s:
                tello.move_back(SPEED)
            elif event.key == pygame.K_a:
                tello.move_left(SPEED)
            elif event.key == pygame.K_d:
                tello.move_right(SPEED)
            elif event.key == pygame.K_q:
                tello.rotate_counter_clockwise(90)  # Rotate 90 degrees counter-clockwise
            elif event.key == pygame.K_e:
                tello.rotate_clockwise(90)  # Rotate 90 degrees clockwise
            elif event.key == pygame.K_UP:
                tello.move_up(SPEED)
            elif event.key == pygame.K_DOWN:
                tello.move_down(SPEED)
            elif event.key == pygame.K_SPACE:
                tello.land()

        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d,
                             pygame.K_UP, pygame.K_DOWN]:
                tello.send_rc_control(0, 0, 0, 0)  # Stop movement

# Main loop
running = True
while running:
    handle_events()

    # Get frame from the drone's camera (optional, for display purposes)
    frame = tello.get_frame_read().frame

    # Display the frame (optional, requires additional setup for Pygame window)
    # For simplicity, this example doesn't include displaying the camera feed.
    # You can integrate it as needed using Pygame's surface blitting.

    # Limit the loop to 30 frames per second (FPS)
    pygame.time.Clock().tick(30)

# Land and end the Tello connection
tello.land()
tello.end()