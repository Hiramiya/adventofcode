dataarray = []
with open("02/input") as f:
    for line in f:
        dataarray.append(line.rstrip())

# Part One
game_sum_p1 = 0
cube_max = {}
cube_max['red'] = 12
cube_max['green'] = 13
cube_max['blue'] = 14

for item in dataarray:
    game, game_results = item.split(':', 1)
    game_num = game.split(' ', 1)[1]
    game_is_possible = True
    
    for result in game_results.split(';'):
        for cubes in result.split(','):
            count, colour = cubes.split()
            if int(count) > cube_max[colour]:
                game_is_possible = False
                continue

    if game_is_possible:
        game_sum_p1 += int(game_num)

print(game_sum_p1)

# Part Two

power_sum_p2 = 0

for item in dataarray:
    game, game_results = item.split(':', 1)
    game_num = game.split(' ', 1)[1]
    gamelowest = {}
    
    gamelowest['red'] = 0
    gamelowest['green'] = 0
    gamelowest['blue'] = 0
    
    for result in game_results.split(';'):
        for cubes in result.split(','):
            count, colour = cubes.split()
            gamelowest[colour] = max(int(gamelowest[colour]), int(count))
    
    cube_power = int(gamelowest['red']) * int(gamelowest['green']) * int(gamelowest['blue'])
    power_sum_p2 += cube_power

print(power_sum_p2)
