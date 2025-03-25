def turnOnLED():
    if input.button_is_pressed(Button.A):
        for y in range(5):
            for x in range(5):
                led.plot(x, y)
                basic.pause(100)
    if input.button_is_pressed(Button.B):
        for y in range(4, -1, -1):
            for x in range(4, -1, -1):
                led.plot(x, y)
                basic.pause(100)
basic.forever(turnOnLED)

def turnOffLED():
    if input.button_is_pressed(Button.A):
        basic.pause(200)
        for y2 in range(5):
            for x2 in range(5):
                led.unplot(x2, y2)
                basic.pause(100)
    if input.button_is_pressed(Button.B):
        basic.pause(200)
        for y2 in range(4, -1, -1):
            for x2 in range(4, -1, -1):
                led.unplot(x2, y2)
                basic.pause(100)
basic.forever(turnOffLED)