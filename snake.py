from constraints import check_constraints


def number_of_available_different_paths(board, snake, depth):
    check_constraints(board, snake, depth)
    actual_depth = 0
    paths = [snake]
    valid_paths = find_paths(board, depth, actual_depth, paths)
    return valid_paths


def find_paths(board, depth, actual_depth, paths):
    if actual_depth == depth:
        valid_paths = len(paths)
        return valid_paths

    new_movements = []
    for path in paths:
        new_movements.extend(check_movements(board, path))

    paths = new_movements
    actual_depth += 1
    return find_paths(board, depth, actual_depth, paths)


def check_movements(board, previous_path):
    new_paths = []
    check_up_movement(previous_path, new_paths)
    check_down_movement(previous_path, new_paths, board)
    check_left_movement(previous_path, new_paths)
    check_right_movement(previous_path, new_paths, board)
    return new_paths


def check_up_movement(path, new_paths):
    # Check if up movement not crosses board and there is not self-intersection
    new_path = path.copy()
    new_path.pop(-1)
    up_movement = new_path[0][0] - 1
    if 0 <= up_movement and [up_movement, new_path[0][1]] not in new_path:
        new_path.insert(0, [up_movement, new_path[0][1]])
        new_paths.append(new_path)


def check_down_movement(path, new_paths, board):
    # Check if down movement not crosses board and there is not self-intersection
    new_path = path.copy()
    new_path.pop(-1)
    down_movement = new_path[0][0] + 1
    if down_movement < board[0] and [down_movement, new_path[0][1]] not in new_path:
        new_path.insert(0, [down_movement, new_path[0][1]])
        new_paths.append(new_path)


def check_left_movement(path, new_paths):
    # Check if left movement not crosses board and there is not self-intersection
    new_path = path.copy()
    new_path.pop(-1)
    left_movement = new_path[0][1] - 1
    if 0 <= left_movement and [new_path[0][0], left_movement] not in new_path:
        new_path.insert(0, [new_path[0][0], left_movement])
        new_paths.append(new_path)


def check_right_movement(path, new_paths, board):
    # Check if right movement not crosses board and there is not self-intersection
    new_path = path.copy()
    new_path.pop(-1)
    right_movement = new_path[0][1] + 1
    if right_movement < board[1] and [new_path[0][0], right_movement] not in new_path:
        new_path.insert(0, [new_path[0][0], right_movement])
        new_paths.append(new_path)
