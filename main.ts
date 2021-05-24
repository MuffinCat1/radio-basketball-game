//for the first MicroBit Put These Code
radio.setGroup(1)

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

//for the Second MicroBit Put These Code
/*
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
})*/