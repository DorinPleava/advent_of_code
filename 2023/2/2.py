# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

# You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

# For example, the record of a few games might look like this:

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

# In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.


# Consider your entire calibration document. What is the sum of all of the calibration values?

# only 12 red cubes, 13 green cubes, and 14 blue cubes


from math import prod


def run_p1(input: list[str]):
    max_game_hand = {"red": 12, "green": 13, "blue": 14}
    total_sum_working_games = 0
    for line in input:
        game_nr, game_sets = line.split(":")
        game_nr_to_save = game_nr[5:]
        print(game_nr_to_save)

        game_possible = None

        for game_set in game_sets.split(';'):
            print(f"game_set: {game_set}")
            for game_hand in game_set.strip().split(','):
                game_hand_nr, game_hand_colour = game_hand.strip().split(" ")
                if int(game_hand_nr) > max_game_hand[game_hand_colour]:
                    print(
                        f'because {game_hand_nr} > {max_game_hand[game_hand_colour]} {game_hand_colour} game {game_nr_to_save} is not possible'
                    )
                    game_possible = False
                    break
                else:
                    print("Game {} is possible".format(game_nr_to_save))
                    game_possible = True
            if not game_possible:
                break

        if game_possible:
            total_sum_working_games += int(game_nr_to_save)
    print(total_sum_working_games)


def run(input: list[str]):
    min_game_cubes = {}
    for line in input:
        game_nr, game_sets = line.split(":")
        game_nr_to_save = game_nr[5:]
        print(game_nr_to_save)

        max_game_hand = {}
        for game_set in game_sets.split(';'):
            # print(f"game_set: {game_set}")
            for game_hand in game_set.strip().split(','):
                game_hand_nr, game_hand_colour = game_hand.strip().split(" ")

                if game_hand_colour not in max_game_hand:
                    max_game_hand[game_hand_colour] = int(game_hand_nr)
                else:
                    max_game_hand[game_hand_colour] = max(max_game_hand[game_hand_colour], int(game_hand_nr))

        min_game_cubes[game_nr_to_save] = max_game_hand

    print(min_game_cubes["1"])

    # sum of all the min cubes
    total_sum = 0
    for game_nr, game_sets in min_game_cubes.items():
        print(game_nr, game_sets)
        print(prod(game_sets.values()))
        total_sum += prod(game_sets.values())

    print(total_sum)
