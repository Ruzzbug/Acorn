from solver import solve
import os

BFS_dict = {
    "board_hard.txt": "sddddsswwdddaassddddsssss",
    "board_super_hard.txt": "sddddssadwwdddaassddddsssss",
    "board_simple.txt": "ss",
    "board_medium.txt": "sddssss"
}

def test_edge():
    print("Testing edge cases")
    results = ""
    for file in os.listdir('test_edge_boards'):
        print("  " + str(file))
        print("    " + str(solve(f'./test_edge_boards/{file}', 'DFS')))
        print("    " + str(solve(f'./test_edge_boards/{file}', 'BFS')) +"\n")
    print("Edge Solver Cases Passed")
    return True

def test_DFS():
    results = ""
    print(f"\nTesting DFS")
    for file in os.listdir('standard_boards'):
        result = solve(f'./standard_boards/{file}', 'DFS')
        assert isinstance(result, str), "No DFS solution found"
        results += "  " + result + "\n"
        print(f"  {file}\n    {result}")
    print("DFS Tests Passed")
    return True

def test_BFS():
    results = ""
    print(f"\nTesting BFS")
    for file in os.listdir('standard_boards'):
        result = solve(f'./standard_boards/{file}', 'BFS')
        assert isinstance(result, str), "No BFS solution found"
        if file in BFS_dict:
            assert BFS_dict.get(file) == result, f"BFS did not find the shortest path for {file}"
        results += "  " + result + "\n"
        print(f"  {file}\n    {result}")
    print("BFS Tests Passed")
    return True


def run_tests():
    print("== SOLVER TESTS ==")
    if test_edge() == True and test_DFS() == True and test_BFS() == True:
        print("\n=========================\n ALL SOLVER TESTS PASSED \n=========================")
        return True
    return False

if __name__ == "__main__":
    run_tests()

