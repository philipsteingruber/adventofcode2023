import math


def part1_2(games):
    valid_games = []
    minimum_powers = []

    for game in games:
        game_id, sets = game.split(': ')
        sets = sets.split('; ')
        game_id = game_id.split(' ')[1]
        maximums = {'red': 0, 'green': 0, 'blue': 0}
        minimums = {'red': None, 'green': None, 'blue': None}

        for cube_set in sets:
            cube_groups = cube_set.split(', ')
            for cube_group in cube_groups:
                amount, color = cube_group.split(' ')
                maximums[color] = max(maximums[color], int(amount))
                if not minimums[color]:
                    minimums[color] = int(amount)
                minimums[color] = max(minimums[color], int(amount))

        minimum_powers.append(math.prod(minimums.values()))
        if maximums['red'] <= 12 and maximums['green'] <= 13 and maximums['blue'] <= 14:
            valid_games.append(int(game_id))

    return sum(valid_games), sum(minimum_powers)


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = list(map(str.strip, file.readlines()))

    result = part1_2(input_data)
    print('Part 1:', result[0])
    print('Part 2:', result[1])