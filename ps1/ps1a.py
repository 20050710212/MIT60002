###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = {}
    with open(filename, 'r') as f1:
        list1 = f1.readlines()
        for item in list1:
            item_list = item.split(',')
            cows[item_list[0]] = int(item_list[1])
    return cows
    #pass

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_sorted = sorted(cows.items(), key  = lambda x:x[1], reverse = True)
    total_trips = 0
    weighs_per_trip = 0
    list_per_trip= []
    total_list = []
    transported = []
    while len(transported) < len(cows):
        for cow in cows_sorted:
            if cow[0] not in transported:
                weight = int(cow[1])
                if(weighs_per_trip + weight <= limit):
                    weighs_per_trip += weight
                    list_per_trip.append(cow[0])
                    transported.append(cow[0])
        total_list.append(list_per_trip)
        weighs_per_trip = 0
        list_per_trip = []
        total_trips += 1
    return total_list
    # TODO: Your code here
    #pass

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    #pass
    cows_name = list(cows.keys())
    valid_allocation = []
    count = 0
    for allocation in get_partitions(cows_name):
        count += 1
        valid = True
        for trip in allocation:
            weighs_per_trip = 0
            for cow in trip:
                weighs_per_trip += cows[cow]
            if weighs_per_trip > limit:
                valid = False
                break
        if valid == True:
            valid_allocation.append(allocation)
    print('the number of allocations is', count)    
    return min(valid_allocation, key=len)

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    
    # TODO: Your code here
    start = time.time()
    greedy_result = greedy_cow_transport(cows)
    end = time.time()
    time_used = end - start
    print("The time used for greedy_cow_transport is", time_used)
    print("The trips used for greedy algorithm is", len(greedy_result))
    print("The reuslt of greedy_cow_transport is", greedy_result)

    start = time.time()
    brute_result = brute_force_cow_transport(cows)
    end = time.time()
    time_used = end - start
    print("The time used for brute_cow_transport is", time_used)
    print("The trips used for brute algorithm is", len(brute_result))
    print("The reuslt of brute_cow_transport is", brute_result)
    
    #pass
if __name__ == '__main__':
    filename = 'ps1_cow_data.txt'
    cows = load_cows(filename)
    compare_cow_transport_algorithms()