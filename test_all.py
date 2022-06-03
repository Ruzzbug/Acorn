"""
grid and cells don't need tests because the functions that call them handle any bad inputs

the tests for player are in test_game because player needs a Game state to function
"""

import subprocess
import os
from test_game import run_tests as test_game
from test_parser import run_tests as test_parser
from test_solver import run_tests as test_solver

print("###########################")
print("Running unit and e2e tests!")
print("###########################")

if test_parser() == True and test_game() == True and test_solver() == True:
    print("\n###########################")
    print("#### ALL TESTS PASSED! ####")
    print("###########################\n")
else:
    print("\n###########################")
    print("### THERE WAS AN ERROR! ###")
    print("###########################\n")
    exit()

subprocess.call(['./test_e2e.sh'])






