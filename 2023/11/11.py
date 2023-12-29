def distance_between_points(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def run(input: list[str]):
    new_input = []

    # expand "universe" horizontally
    for line in input:
        # if line is full of '.'s, duplicate it
        new_input.append(line)
        if all([c == "." for c in line]):
            new_input.append(line)

    # expand "universe" vertically
    # flip the input
    new_input = ["".join(map(str, row)) for row in zip(*new_input)]

    new_new_input = []
    # expand horizontally again
    for line in new_input:
        new_new_input.append(line)
        if all([c == "." for c in line]):
            new_new_input.append(line)

    # flip the input back
    new_new_input = ["".join(map(str, row)) for row in zip(*new_new_input)]

    # now we have a 3d input
    counter = 0

    # Create a new list with modified strings
    updated_input = []
    for line in new_new_input:
        updated_line = ""
        for char in line:
            if char == "#":
                counter += 1
                updated_line += str(counter)
            else:
                updated_line += char
        updated_input.append(updated_line)

    new_new_input = updated_input

    # print(new_new_input)

    # create pairs of points
    points_coordinates = []
    for y, line in enumerate(new_new_input):
        for x, char in enumerate(line):
            if char != ".":
                points_coordinates.append((x, y))

    # get all the pairs of points
    pairs = []
    # for point in points_coordinates:
    #     for other_point in points_coordinates:
    #         if point != other_point:
    #             pairs.append((point, other_point))

    for i in range(len(points_coordinates)):
        for j in range(i + 1, len(points_coordinates)):
            pairs.append((points_coordinates[i], points_coordinates[j]))

    # print(pairs)

    # create a dict with all the distances
    distances = {}
    for pair in pairs:
        distances[pair] = distance_between_points(pair[0], pair[1])

    # print(distances)

    # sum all the distances
    total_distance = sum(distances.values())

    print(total_distance)
