# Part 1: Greedy Cow Transport
# 20.0/20.0 points (graded)
# One way of transporting cows is to always pick the heaviest cow that will fit onto the spaceship first. This is an example of a greedy
# algorithm. So if there are only 2 tons of free space on your spaceship, with one cow that's 3 tons and another that's 1 ton, the 1 ton
# cow will get put onto the spaceship.

# Implement a greedy algorithm for transporting the cows back across space in the function greedy_cow_transport. The function returns a
# list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

# Note: Make sure not to mutate the dictionary of cows that is passed in!

# Assumptions:
# The order of the list of trips does not matter. That is, [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent lists of trips.
# All the cows are between 0 and 100 tons in weight.
# All the cows have unique names.
# If multiple cows weigh the same amount, break ties arbitrarily.

# The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.

# Example:
# Suppose the spaceship has a weight limit of 10 tons and the set of cows to transport is
# {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}.
# The greedy algorithm will first pick Jesse as the heaviest cow for the first trip. There is still space for 4 tons on the trip. Since
# Maggie will not fit on this trip, the greedy algorithm picks Maybel, the heaviest cow that will still fit. Now there is only 1 ton of
# space left, and none of the cows can fit in that space, so the first trip is [Jesse, Maybel].
# For the second trip, the greedy algorithm first picks Maggie as the heaviest remaining cow, and then picks Callie as the last cow.
# Since they will both fit, this makes the second trip [[Maggie], [Callie]].
# The final result then is [["Jesse", "Maybel"], ["Maggie", "Callie"]].


# Enter your code for the Greedy Cow Transport here 
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
    # TODO: Your code here
    overall_trips = []
    copy_cows = cows.copy()
    cows_tuple = list(copy_cows.items())

    cows_tuple.sort(key=lambda x:x[1], reverse=True)
    list_in_use = cows_tuple[:]

    while cows_tuple:
        trip = []
        limit_in_use = limit

        for cow, weight in list_in_use:
            if weight <= limit_in_use:
                trip.append(cow)
                cows_tuple.remove((cow, weight))
                limit_in_use -= weight

        overall_trips.append(trip)
        list_in_use = cows_tuple[:]

    return overall_trips
    
p1t1 = {'Clover': 5, 'Lotus': 10, 'Muscles': 65, 'Patches': 60, 'Polaris': 20, 'Milkshake': 75, 'MooMoo': 85, 'Horns': 50, 'Miss Bella': 15, 'Louis': 45}
p1t2 = {'Abby': 38, 'Coco': 10, 'Buttercup': 72, 'Rose': 50, 'Patches': 12, 'Willow': 35, 'Betsy': 65, 'Lilly': 24, 'Daisy': 50, 'Dottie': 85}
p1t3 = {'Starlight': 54, 'Abby': 28, 'Buttercup': 11, 'Rose': 42, 'Coco': 59, 'Luna': 41, 'Willow': 59, 'Betsy': 39}

print(greedy_cow_transport(p1t1, limit))
print(greedy_cow_transport(p1t2, limit))
print(greedy_cow_transport(p1t3, 120))
