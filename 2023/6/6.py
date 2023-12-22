from math import prod


def run_p1(input: list[str]):

    good_charge_durations = []

    filterd_times = filter(lambda x: x != '', input[0].split(':')[1].strip().split(" "))
    race_duration = list(filterd_times)

    filtered_distances = filter(lambda x: x!= '', input[1].split(':')[1].strip().split(" "))
    distances_to_travel = list(filtered_distances)
    
    time_with_distances = zip(race_duration, distances_to_travel)


    for race_duration, distance_to_travel in time_with_distances:

        winning_charges = 0
        for charge_duration in range(0, int(race_duration)):
            
            distance_traveled = (int(race_duration)-charge_duration) * charge_duration
            
            if distance_traveled > int(distance_to_travel):
                print(f"holding charge for {charge_duration} seconds traveled {distance_traveled} meters")
                winning_charges += 1
        
        good_charge_durations.append(winning_charges)

    print(prod(good_charge_durations))


def run(input: list[str]):

    good_charge_durations = []

    filterd_times = filter(lambda x: x != '', input[0].split(':')[1].strip().split(" "))
    race_duration = ''.join(list(filterd_times))

    filtered_distances = filter(lambda x: x!= '', input[1].split(':')[1].strip().split(" "))
    distance_to_travel = ''.join(list(filtered_distances))
    
    # time_with_distances = zip(race_duration, distances_to_travel)


    print(f"race duration: {race_duration}")
    print(f"distances to travel: {distance_to_travel}")

    # for race_duration, distance_to_travel in time_with_distances:

    winning_charges = 0
    for charge_duration in range(0, int(race_duration)):
            
        distance_traveled = (int(race_duration)-charge_duration) * charge_duration
            
        if distance_traveled > int(distance_to_travel):
            # print(f"holding charge for {charge_duration} seconds traveled {distance_traveled} meters")
            winning_charges += 1
        
    good_charge_durations.append(winning_charges)

    print(prod(good_charge_durations))

