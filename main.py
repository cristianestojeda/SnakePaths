from snake import number_of_available_different_paths


def test_depth_3():
    board = [4, 3]
    snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
    depth = 3
    valid_paths = number_of_available_different_paths(board, snake, depth)
    assert valid_paths == 7, 'Valid paths should be 7, not ' + str(valid_paths)
    print('Test 1/3 OK. Valid paths should be 7 and there are: ' + str(valid_paths))


def test_depth_10():
    board = [2, 3]
    snake = [[0, 2], [0, 1], [0, 0], [1, 0], [1, 1], [1, 2]]
    depth = 10
    valid_paths = number_of_available_different_paths(board, snake, depth)
    assert valid_paths == 1, 'Valid paths should be 1, not ' + str(valid_paths)
    print('Test 2/3 OK. Valid paths should be 1 and there are: ' + str(valid_paths))


def test_depth_4():
    board = [10, 10]
    snake = [[5, 5], [5, 4], [4, 4], [4, 5]]
    depth = 4
    valid_paths = number_of_available_different_paths(board, snake, depth)
    assert valid_paths == 81, 'Valid paths should be 81, not ' + str(valid_paths)
    print('Test 3/3 OK. Valid paths should be 81 and there are: ' + str(valid_paths))


if __name__ == "__main__":
    test_depth_3()
    test_depth_10()
    test_depth_4()
    print('All tests have passed correctly.')
    exit(0)
