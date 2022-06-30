from snake import number_of_available_different_paths


def test_depth_3():
    board = [4, 3]
    snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
    depth = 3
    valid_paths = number_of_available_different_paths(board, snake, depth)
    assert valid_paths == 7, 'Valid paths should be 7 and there are: ' + str(valid_paths)
    print('Test 1/3 OK. Valid paths should be 7 and there are: ' + str(valid_paths))


if __name__ == "__main__":
    test_depth_3()
