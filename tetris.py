from enum import Enum
import keyword

class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4


def play_tetris():
    # Definimos una matriz 10x10
    screen = [  ["⬛", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
                ["⬛", "⬛", "⬛", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
                ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"] ]
    
    print_screen(screen)
    rotation = 0
    (screen, rotation) = move_piece(Movement.DOWN, screen, rotation)
    (screen, rotation) = move_piece(Movement.RIGHT, screen, rotation)
    (screen, rotation) = move_piece(Movement.RIGHT, screen, rotation)
    (screen, rotation) = move_piece(Movement.LEFT, screen, rotation)
    (screen, rotation) = move_piece(Movement.ROTATE, screen, rotation)
    (screen, rotation) = move_piece(Movement.ROTATE, screen, rotation)
    


def move_piece(move: Movement, screen: list, rotation: int) -> (list, int):
    canvas_screen = [["⬜"]*10 for _ in range(10)]
    new_rotation = rotation
    if move is Movement.ROTATE:
        new_rotation = 0 if rotation == 3 else rotation + 1

    rotation_item = 0
    rotations = [
        [( 1, 1), ( 0, 0), ( -2, 0), ( -1, -1)],
        [( 0, 1), (-1, 0), ( 0, -1), ( 1, -2)],
        [( 0, 2), ( 1, 1), ( -1, 1), ( -2, 0)],
        [( 0, 1), ( 1, 0), ( 2, -1), ( 1, -2)],
        [( 0, 1), ( 1, 0), ( 2, -1), ( 1, -2)]
    ]
    # Buscamos la pieza en la matriz
    for row_index, row in enumerate(screen):
        for col_index, item in enumerate(row):
            if item == "⬛":
                new_row_index = 0
                new_col_index = 0
                match move:
                    case Movement.DOWN:
                        new_row_index = row_index + 1
                        new_col_index = col_index
                    case Movement.RIGHT:
                        new_row_index = row_index
                        new_col_index = col_index + 1
                    case Movement.LEFT:
                        new_row_index = row_index
                        new_col_index = col_index - 1
                    case Movement.ROTATE:
                        new_row_index = row_index + rotations[new_rotation][rotation_item][0]
                        new_col_index = col_index + rotations[new_rotation][rotation_item][1]
                        rotation_item += 1
                if new_row_index > 9 or new_col_index > 9 or new_col_index < 0:
                    print("\nNo se puede mover la pieza")
                    return (screen, rotation)
                else:
                    canvas_screen[new_row_index][new_col_index] = "⬛"
    print_screen(canvas_screen)
    return (canvas_screen, new_rotation)

def print_screen(screen: list):
    print("\n ----Tetris---- \n")
    try:
        for row in screen:
            print("".join(map(str, row)))
    except UnicodeEncodeError as e:
        # Handle the exception
        print(e)

play_tetris()