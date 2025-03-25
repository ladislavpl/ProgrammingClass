speed = 1000
points = 0
gameover = 0
eggposition = [randint(0, 4), 0]
wolfposition = 2

def on_button_pressed_a():
    global wolfposition
    if wolfposition > 0 and gameover == 0:
        wolfposition += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global wolfposition
    if wolfposition < 4 and gameover == 0:
        wolfposition += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def render():
    global gameover, eggposition, points
    if gameover == 0:
        basic.clear_screen()
        led.plot(wolfposition, 4)
        led.plot(eggposition[0], eggposition[1])
        basic.pause(50)
    else:
        basic.clear_screen()
        basic.show_string("GAME OVER", 150)
        basic.pause(50)
        basic.show_string(str(points) + " POINTS", interval = 150)
basic.forever(render)

def logic():
    global gameover, eggposition, points, speed
    if gameover == 0:
        for i in range(4):
            eggposition[1] = i
            basic.pause(speed)
        if led.point(eggposition[0], 4):
            music.play(music.tone_playable(1000, 100), music.PlaybackMode.IN_BACKGROUND)
            points += 1
        else:
            gameover = 1
        eggposition = [randint(0, 4), 0]
basic.forever(logic)

def onEvery_interval():
    global speed
    if gameover == 0:
        speed -= 20
loops.every_interval(30000, onEvery_interval)