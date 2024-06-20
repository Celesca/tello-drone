package main

import (
	"fmt"
	"log"
	"time"

	"github.com/eiannone/keyboard"
	"gobot.io/x/gobot"
	"gobot.io/x/gobot/platforms/dji/tello"
)

func main() {
	drone := tello.NewDriver("8888")

	work := func() {
		drone.On(tello.ConnectedEvent, func(data interface{}) {
			fmt.Println("Connected to drone!")
		})

		drone.On(tello.FlightDataEvent, func(data interface{}) {
			fmt.Println("Flight Data:", data)
		})

		// Start the keyboard listener
		err := keyboard.Open()
		if err != nil {
			log.Fatalf("Failed to open keyboard: %v", err)
		}
		defer keyboard.Close()

		fmt.Println("Press ESC to quit")

		// Pause to give time for admin permissions confirmation
		time.Sleep(10 * time.Second) // Adjust the duration as needed

		go func() {
			for {
				char, key, err := keyboard.GetKey()
				if err != nil {
					log.Fatalf("Failed to get key: %v", err)
				}
				if key == keyboard.KeyEsc {
					fmt.Println("Exiting...")
					drone.Land()
					time.Sleep(2 * time.Second)
					break
				}
				switch char {
				case 'w':
					fmt.Println("Forward")
					drone.Forward(20)
				case 's':
					fmt.Println("Backward")
					drone.Backward(20)
				case 'a':
					fmt.Println("Left")
					drone.Left(20)
				case 'd':
					fmt.Println("Right")
					drone.Right(20)
				case ' ':
					fmt.Println("Takeoff")
					drone.TakeOff()
				case 'l':
					fmt.Println("Land")
					drone.Land()
				case 'i':
					fmt.Println("Up")
					drone.Up(20)
				case 'k':
					fmt.Println("Down")
					drone.Down(20)
				case 'j':
					fmt.Println("Counter Clockwise")
					drone.CounterClockwise(20)
				case 'h':
					fmt.Println("Clockwise")
					drone.Clockwise(20)
				}
			}
		}()
	}

	robot := gobot.NewRobot("tello",
		[]gobot.Connection{},
		[]gobot.Device{drone},
		work,
	)

	robot.Start()
}
