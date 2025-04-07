sprite = game.create_sprite(2, 2)
food = game.create_sprite(randint(1, 3), randint(1, 3))

def on_forever():
    global sprite
    if sprite.is_touching_edge():
        if sprite.get(LedSpriteProperty.Y) == 0 and sprite.get(LedSpriteProperty.X) != 0 and sprite.get(LedSpriteProperty.X) != 4 and sprite.get(LedSpriteProperty.DIRECTION) == 0:
            sprite.set_y(4)
        elif sprite.get(LedSpriteProperty.Y) == 4 and sprite.get(LedSpriteProperty.X) != 0 and sprite.get(LedSpriteProperty.X) != 4 and sprite.get(LedSpriteProperty.DIRECTION) == 180:
            sprite.set_y(0)
        elif sprite.get(LedSpriteProperty.X) == 0 and sprite.get(LedSpriteProperty.Y) != 0 and sprite.get(LedSpriteProperty.Y) != 4 and sprite.get(LedSpriteProperty.DIRECTION) == -90:
            sprite.set_x(4)
        elif sprite.get(LedSpriteProperty.X) == 4 and sprite.get(LedSpriteProperty.Y) != 0 and sprite.get(LedSpriteProperty.Y) != 4 and sprite.get(LedSpriteProperty.DIRECTION) == 90:
            sprite.set_x(0)
        elif sprite.get(LedSpriteProperty.X) == 4 and sprite.get(LedSpriteProperty.Y) == 4 and sprite.get(LedSpriteProperty.DIRECTION) == 90:
            sprite.set_x(0)
        elif sprite.get(LedSpriteProperty.X) == 4 and sprite.get(LedSpriteProperty.Y) == 4 and sprite.get(LedSpriteProperty.DIRECTION) == 180:
            sprite.set_y(0)
        elif sprite.get(LedSpriteProperty.X) == 0 and sprite.get(LedSpriteProperty.Y) == 4 and sprite.get(LedSpriteProperty.DIRECTION) == -90:
            sprite.set_x(4)
        elif sprite.get(LedSpriteProperty.X) == 0 and sprite.get(LedSpriteProperty.Y) == 4 and sprite.get(LedSpriteProperty.DIRECTION) == 180:
            sprite.set_y(0)
        elif sprite.get(LedSpriteProperty.X) == 0 and sprite.get(LedSpriteProperty.Y) == 0 and sprite.get(LedSpriteProperty.DIRECTION) == -90:
            sprite.set_x(0)
        elif sprite.get(LedSpriteProperty.X) == 0 and sprite.get(LedSpriteProperty.Y) == 0 and sprite.get(LedSpriteProperty.DIRECTION) == 0:
            sprite.set_y(4)
        elif sprite.get(LedSpriteProperty.X) == 4 and sprite.get(LedSpriteProperty.Y) == 0 and sprite.get(LedSpriteProperty.DIRECTION) == 90:
            sprite.set_x(0)
        elif sprite.get(LedSpriteProperty.X) == 4 and sprite.get(LedSpriteProperty.Y) == 0 and sprite.get(LedSpriteProperty.DIRECTION) == 0:
            sprite.set_y(4)
        else:
            sprite.move(1)
    else:
        sprite.move(1)
    basic.pause(1000)
basic.forever(on_forever)

def foodLogic():
    global sprite, food
    if sprite.is_touching(food):
        game.add_score(1)
        food.set_x(randint(1, 3))
        food.set_y(randint(1, 3))
basic.forever(foodLogic)

def A():
    global sprite
    sprite.turn(Direction.LEFT, 90)
input.on_button_pressed(Button.A, A)

def B():
    global sprite
    sprite.turn(Direction.RIGHT, 90)
input.on_button_pressed(Button.B, B)

def on_logo_event_pressed():
    game.game_over()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)