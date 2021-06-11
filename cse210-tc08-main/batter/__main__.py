import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}
    
    """
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 5)
    position = Point(x, y)
    paddle = Actor()
    paddle.set_text("=" * 11)
    paddle.set_position(position)
    cast["paddle"] = [paddle]
    """
    
    cast["paddle"] = []
    for x in range(31, 56):
        y = 18
        position = Point(x, y)
        paddle = Actor()
        paddle.set_text("=")
        paddle.set_position(position)
        cast["paddle"].append(paddle)

    cast["brick"] = []
    for x in range(5, 75):
        for y in range(3, 7):
            position = Point(x, y)
            brick = Actor()
            brick.set_text("*")
            brick.set_position(position)
            cast["brick"].append(brick)

    x = int(constants.MAX_X / 2 - 10)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y)
    velocity = Point(1, 1)

    ball = Actor()
    ball.set_text("O")
    ball.set_position(position)
    ball.set_velocity(velocity)
    cast["ball"] = [ball]

    trail1 = Actor()
    trail1.set_text("o")
    trail1.set_position(position)
    ball.set_child(trail1)

    trail2 = Actor()
    trail2.set_text(".")
    trail2.set_position(position)
    trail1.set_child(trail2)
    
    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_acition = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_acition]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)