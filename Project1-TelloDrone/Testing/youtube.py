import tello

tello.start()
power = tello.get_battery()
print(f'Battery: {power}%')
tello.takeoff()
tello.land()