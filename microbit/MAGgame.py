game.set_life(2)
player = game.create_sprite(0, 0)
point = game.create_sprite(4, randint(0, 4))

def render():
    if game.is_paused() == False:
        if input.magnetic_force(Dimension.X) >= 500:
            player.set(LedSpriteProperty.Y, 0)
        elif input.magnetic_force(Dimension.X) >= 350:
            player.set(LedSpriteProperty.Y, 1)
        elif input.magnetic_force(Dimension.X) >= 200:
            player.set(LedSpriteProperty.Y, 2)
        elif input.magnetic_force(Dimension.X) >= 50:
            player.set(LedSpriteProperty.Y, 3)
        else:
            player.set(LedSpriteProperty.Y, 4)
basic.forever(render)

def pointLogic():
    if game.is_paused() == False:
        if point.x() == 1 and point.y() == player.y():
            game.add_score(1)
            point.go_to(4, randint(0, 4))
        elif point.x() == 1 and point.y() != player.y():
            game.remove_life(1)
            point.go_to(4, randint(0, 4))
        point.set_direction(-90)
        point.move(1)
        basic.pause(800)
basic.forever(pointLogic)

def on_button_pressed_a():
    if game.is_paused():
        game.resume()
    else:
        game.pause()
input.on_button_pressed(Button.A, on_button_pressed_a)