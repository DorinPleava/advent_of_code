from math import lcm


def run_p1(input: list[str]):
    instructions = input[0]

    # key_to_reach = "ZZZ"
    # repeat instructions 100 times just in case
    instructions = instructions * 100

    # construct the dict as {key: (left, right)}

    my_dict = {}

    for line in input[2:]:
        my_dict[line[:3]] = (line[7:10], line[12:15])

    # print(my_dict)

    current_point = my_dict["AAA"]

    for index, instruction in enumerate(instructions, start=1):
        if instruction == "L":
            if current_point[0] == "ZZZ":
                print("FOUND at index", index)
                break

            print(f"Going left from {current_point[0]} to {current_point[0]}")
            current_point = my_dict[current_point[0]]
        else:
            if current_point[1] == "ZZZ":
                print("FOUND at index", index)
                break
            print(f"Going right from {current_point[1]} to {current_point[1]}")
            current_point = my_dict[current_point[1]]


def ends_with_z(key: str):
    return key.endswith("Z")


def run(input: list[str]):
    instructions = input[0]

    # key_to_reach = "ZZZ"
    # repeat instructions 100 times just in case
    instructions = instructions * 100

    # construct the dict as {key: (left, right)}

    my_dict = {}

    for line in input[2:]:
        my_dict[line[:3]] = (line[7:10], line[12:15])

    # print(my_dict)

    current_points = list(filter(lambda x: x.endswith("A"), list(my_dict.keys())))

    print(current_points)
    # ['XVA', 'GGA', 'DXA', 'LTA', 'BJA', 'AAA']
    # current_points = ["XVA"] # = 16271
    # current_points = ["GGA"]  # = 24253
    # current_points = ["DXA"]  # = 13201
    # current_points = ["LTA"]  # = 14429
    # current_points = ["BJA"]  # = 18113
    # current_points = ["AAA"]  # = 22411

    lcm_ = lcm(16271, 24253, 13201, 14429, 18113, 22411)

    print(lcm_)

    exit()

    for index, instruction in enumerate(instructions, start=0):
        if instruction == "L":
            if all(ends_with_z(key) for key in current_points):
                print("FOUND at index", index)
                break

            current_points = [my_dict[key][0] for key in current_points]

            # print(f"Going left from {current_points} to {current_points}")
        else:
            if all(ends_with_z(key) for key in current_points):
                print("FOUND at index", index)
                break
            current_points = [my_dict[key][1] for key in current_points]

            # print(f"Going right from {current_points} to {current_points}")
