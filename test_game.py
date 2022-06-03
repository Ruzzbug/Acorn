from game import Game
import os


# def test_errors():
#     print("Testing game error handling:")
#     results = ""
#     for file in os.listdir('test_error_boards'):
#         if Game(f'./test_error_boards/{file}').error != True:
#             print("parse.py error catching is broken")
#             exit()
#     print("Error catching in parse.py is working\n")
#     return True


def test_valid_inputs():
    print("Testing valid inputs")
    moves = 'wWaAsSdD'
    level = Game('./standard_boards/board_medium.txt')
    try:
        for move in moves:
            result = (level.game_move(move))
            if result == 'a' or 'You walked into a wall. Oof!':
                print(" - ",move, 'good')
            else:
                raise ValueError
    except ValueError:
        print("Failed to handle good inputs")
        print("==== GOOD INPUTS TEST FAILED ====")
        return False
    print("Success, good inputs work\n")
    return True


def test_interactables():
    print 
    level = Game('./test_other_boards/board_test_interactive.txt')
    if level.game_move('a') != 'dead':
        print("Fire doesn't kill")
        print("==== FIRE INTERACTION FAILED ====")
        return False
    
    expected_outputs = [
        "Thank the Honourable Furious Forest, you've found a bucket of water!", 
        "You walked into a wall. Oof!", 
        "",
        "With your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!",
        "Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.",
        "win" 
                        ]
        
    
    level = Game('./test_other_boards/board_test_interactive.txt')
    i = 0
    moves = "ddaasa"
    for move in moves:
        result = level.game_move(move)
        assert result == expected_outputs[i], f"Expected output was '{expected_outputs[i]}' but output was '{result}'\n==== INTERACTIONS FAILED ===="
        i += 1
    print("Success, fire(death), water, fire(dousing), wall, teleporter and air all work\n")
    return True

def test_edge():
    print("Testing edge cases:")
    results = ""
    for file in os.listdir('test_edge_boards'):
        if Game(f'./test_edge_boards/{file}').error == True:
             print("Problem handling edge case boards in game.py")
             exit()
    print("Success edge tests passed\n")
    return True


# Tests running into the blank edges at the bottom left and top right of the maze 
def test_boundary_inputs():
    print("Testing blank walls")
    try:
        moves = 'aasedddddddwwwwwd'
        level = Game('./test_edge_boards/board_test_no_edge.txt')
        for move in moves:
            result = (level.game_move(move))
            if result != None and result != "":
                print(f" {move}: {result}")
    except IndexError:
        print("Player was able to get out of boundary")
        print("==== BOUNDARY INPUTS TEST FAILED ====")
        return False
    print("Success, empty edges are walls\n")
    return True
    

def test_bad_inputs():
    print("Testing bad inputs")
    moves = '1@♥☼😂 p[.?'
    level = Game('./standard_boards/board_medium.txt')
    try:
        for move in moves:
            print(" - ",move)
            level.game_move(move)
    except Exception:
        print("Failed to handle the above bad input")
        print("==== BAD INPUTS TEST FAILED ====")
        return False
    print("Success, bad inputs are not passed on to player\n")
    return True


def run_tests():
    print("== GAME AND PLAYER TESTS ==")
    if test_valid_inputs() == True and test_interactables() == True and test_edge() == True and test_boundary_inputs() == True and test_bad_inputs() == True:
        print("=========================\n= ALL GAME TESTS PASSED =\n=========================\n")
        return True
    else:
        return False
if __name__ == '__main__':
    run_tests()