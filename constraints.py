def check_constraints(board, snake, depth):
    check_board_constraints(board)
    check_snake_constraints(board, snake)
    check_depth(depth)
    return 0


def check_board_constraints(board):
    # Check number of board axes
    assert len(board) == 2, 'Board must have 2 axes'

    # Check board sizes
    for i in range(len(board)):
        assert 1 <= board[i] <= 10, 'Board axis ' + str(i) + ' must be higher/equal to 1 and lower/equal to 10, ' \
                                                             'your board axis ' + str(i) + ' is ' + str(board[i])
    return 0


def check_snake_constraints(board, snake):
    # Check Snake's length
    assert 3 <= len(snake) <= 7, 'The Snake\'s length must be higher/equal to 3 and lower/equal to 7, ' \
                                 'your Snake\'s length is ' + str(len(snake))

    # Check Snake's coordinates
    for position, coordinates in enumerate(snake):
        assert len(coordinates) == 2, 'There must be a total of 2 coordinates in the Snake\'s position ' \
                                      + str(position) + ', you have ' + str(len(coordinates))
        for idx, (coordinate, axis) in enumerate(zip(coordinates, board)):
            assert 0 <= coordinate <= axis, 'Coordinate ' + str(idx) + ' in Snake\'s position ' + \
                                            str(position) + ' is out of the board. Your coordinates are ' + \
                                            str(coordinates) + ' and the board size is ' + str(board)

    # Check Snake's connection (only horizontal and vertical connections allowed)
    for position in range(len(snake) - 1):
        # Up/Down/Right/Left connections respectively
        assert (snake[position + 1][1] == snake[position][1] and snake[position + 1][0] == snake[position][0] - 1) or \
               (snake[position + 1][1] == snake[position][1] and snake[position + 1][0] == snake[position][0] + 1) or \
               (snake[position + 1][0] == snake[position][0] and snake[position + 1][1] == snake[position][1] + 1) or \
               (snake[position + 1][0] == snake[position][0] and snake[position + 1][1] == snake[position][1] - 1), \
            'Snake\'s position ' + str(position + 1) + ' is not connected to previous position'
    return 0


def check_depth(depth):
    # Check path depth
    assert 1 <= depth <= 20, 'Paths depth must be higher/equal to 1 and lower/equal to 20, your depth is ' + str(depth)
    return 0
