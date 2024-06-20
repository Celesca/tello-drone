package main

import (
	"fmt"
	"time"

	"gobot.io/x/gobot"
	"gobot.io/x/gobot/platforms/dji/tello"
)

func main() {
	drone := tello.NewDriver("8888")

	work := func() {
		drone.On(tello.ConnectedEvent, func(data interface{}) {
			fmt.Println("Connected to drone!")
			drone.TakeOff()
			time.Sleep(5 * time.Second)
			drone.Forward(20)
			time.Sleep(2 * time.Second)
			drone.Clockwise(90)
			time.Sleep(2 * time.Second)
			drone.Land()
		})

		drone.On(tello.FlightDataEvent, func(data interface{}) {
			fmt.Println("Flight Data:", data)
		})
	}

	robot := gobot.NewRobot("tello",
		[]gobot.Connection{},
		[]gobot.Device{drone},
		work,
	)

	robot.Start()
}
