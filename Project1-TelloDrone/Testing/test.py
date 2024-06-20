from djitellopy import Tello
import time

tello = Tello()

# Connect to the Tello drone
tello.connect()

# Print the battery percentage
print(f'Battery: {tello.get_battery()}%')

# Take off
tello.takeoff()

# Move up by 50 cm
tello.move_up(50)
time.sleep(2)  # Hover for 2 seconds

# Rotate 360 degrees clockwise
tello.rotate_clockwise(360)
time.sleep(2)  # Hover for 2 seconds

# Land
tello.land()

tello.end()