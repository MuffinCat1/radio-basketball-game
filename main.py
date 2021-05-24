"""

for the Second MicroBit Put These Code

"""

def on_received_number(receivedNumber):
    basic.show_leds("""
        . # # # .
        # # # # #
        # # # # #
        # # # # #
        . # # # .
        """)
radio.on_received_number(on_received_number)

def on_gesture_shake():
    radio.send_number(0)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

"""

radio.setGroup(1)

basic.showLeds(`

. # # # .

# # # # #

# # # # #

# # # # #

. # # # .

`)

input.onGesture(Gesture.Shake, function () {

radio.sendNumber(0)

basic.clearScreen()

})

radio.onReceivedNumber(function (receivedNumber: number) {

basic.showLeds(`

. # # # .

# # # # #

# # # # #

# # # # #

. # # # .

`)

})

"""
# for the first MicroBit Put These Code
radio.set_group(1)