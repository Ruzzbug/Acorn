#Testing of erroneous maze files can be found in test_game.py

import os
from game_parser import(parse)
from game_parser import(read_lines)

ls = [" FW\n", "1X1\n", "Y *"]

def test_parse():
    print("Testing good parse input")
    result = (parse(ls))
    for i in range(len(result)):
        for x in range(len(result[i])):
            if ls[i][x] != result[i][x].display:
                print("Problem with parse")
                return False
    print("Success, valid inputs working on parse\n")
    return True

def test_errors():
    print("Testing parser error handling:")
    results = ""
    for file in os.listdir('test_error_boards'):
        if read_lines(f'./test_error_boards/{file}') == True:
            print("parser error catching is broken")
            return False
    print("Success, error catching in parse.py is working\n")
    return True

def run_tests():
    print("== PARSER TESTS ==")
    if test_parse() == True and test_errors() == True:
        print("=========================\n ALL PARSER TESTS PASSED \n=========================")
        return True
    return False

if __name__ == "__main__":
    run_tests()