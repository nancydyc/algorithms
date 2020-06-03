"""
                               Jaden

                  /           /       \       \
                Min         Amelia      Ren     Noam

        /     /    \        /   \    \
    William Jayden Omar Jaden [Adam]  Miguel

    /                \                  \
   ...               ...                ...


"""
# Solution B: Part I -- Use dictionary to track the route reversely
def get_route(visited_paths, recipient):
    reversed_route = []
    current = recipient
    while current:
        # print(current)
        reversed_route.append(current)
        current = visited_paths[current]
        # print('.....................................')

    reversed_route.reverse()

    return reversed_route


def shortest_route(network, sender, recipient):
    """
        Given information about active users on the network, find the shortest
        oute for a message from one user (the sender) to another (the recipient).
        Return a list of users that make up this route.

        For example:
        >>> shortest_route({ 'Min'    : ['William', 'Jayden', 'Omar'], 'William': ['Min', 'Noam'], 'Jayden' : ['Min', 'Amelia', 'Ren', 'Noam'], 'Ren'    : ['Jayden', 'Omar'], 'Amelia' : ['Jayden', 'Adam', 'Miguel'], 'Adam'   : ['Amelia', 'Miguel', 'Sofia', 'Lucas'], 'Miguel' : ['Amelia', 'Adam', 'Liam', 'Nathan'], 'Noam'   : ['Nathan', 'Jayden', 'William'], 'Omar'   : ['Ren', 'Min', 'Scott']}, 'Jayden', 'Adam')
        ['Jayden', 'Amelia', 'Adam']
        >>> shortest_route({ 'Min'    : ['William', 'Jayden', 'Omar'], 'William': ['Min', 'Noam'], 'Jayden' : ['Min', 'Amelia', 'Ren', 'Noam'], 'Ren'    : ['Jayden', 'Omar'], 'Amelia' : ['Jayden', 'Adam', 'Miguel'], 'Adam'   : ['Amelia', 'Miguel', 'Sofia', 'Lucas'], 'Miguel' : ['Amelia', 'Adam', 'Liam', 'Nathan'], 'Noam'   : ['Nathan', 'Jayden', 'William'], 'Omar'   : ['Ren', 'Min', 'Scott']}, 'Jayden', 'Jayden')
        ['Jayden']
        >>> shortest_route({ 'Min'    : ['William', 'Jayden', 'Omar'], 'William': ['Min', 'Noam'], 'Jayden' : ['Min', 'Amelia', 'Ren', 'Noam'], 'Ren'    : ['Jayden', 'Omar'], 'Amelia' : ['Jayden', 'Adam', 'Miguel'], 'Adam'   : ['Amelia', 'Miguel', 'Sofia', 'Lucas'], 'Miguel' : ['Amelia', 'Adam', 'Liam', 'Nathan'], 'Noam'   : ['Nathan', 'Jayden', 'William'], 'Omar'   : ['Ren', 'Min', 'Scott']}, 'Jayden', 'Yichen')
        []
        >>> shortest_route({ 'Min'    : ['William', 'Jayden', 'Omar'], 'William': ['Min', 'Noam'], 'Jayden' : ['Min', 'Amelia', 'Ren', 'Noam'], 'Ren'    : ['Jayden', 'Omar'], 'Amelia' : ['Jayden', 'Adam', 'Miguel'], 'Adam'   : ['Amelia', 'Miguel', 'Sofia', 'Lucas'], 'Miguel' : ['Amelia', 'Adam', 'Liam', 'Nathan'], 'Noam'   : ['Nathan', 'Jayden', 'William'], 'Omar'   : ['Ren', 'Min', 'Scott']}, 'Jayden', 'Scott')
        ['Jayden', 'Min', 'Omar', 'Scott']
        >>> shortest_route({ 'Min'    : ['William', 'Jayden', 'Omar'], 'William': ['Min', 'Noam'], 'Jayden' : ['Min', 'Amelia', 'Ren', 'Noam'], 'Ren'    : ['Jayden', 'Omar'], 'Amelia' : ['Jayden', 'Adam', 'Miguel'], 'Adam'   : ['Amelia', 'Miguel', 'Sofia', 'Lucas'], 'Miguel' : ['Amelia', 'Adam', 'Liam', 'Nathan'], 'Noam'   : ['Nathan', 'Jayden', 'William'], 'Omar'   : ['Ren', 'Min', 'Scott']}, 'Yichen', 'Scott')
        []
    """

    # Solution A:
    # locate the sender in the dictionary
    # if the sender is the recipient, return itself
    # if the sender doesn't exist in this network, return empty route
    if sender not in network:
        return []
        # raise Exception(f'{sender} is not in the network.')

    if sender == recipient:
        return [recipient]

    q = []
    q.append((sender, sender))

    seen = set()
    seen.add(sender)

    while q:
        next_sender, route = q.pop(0)
        # if find the target recipient, add the recipient to the route and return route
        # if not, make it next sender and add to the route as well
        if next_sender == recipient:
            return route.split(',')
        # if reaching an end of the network, network breaks and we can't find the person, return empty route
        if next_sender in network:
            for person in network[next_sender]:
                if person not in seen:
                    seen.add(person)
                    q.append((person, route + ',' + person))
                    # print(q)

    return []

# runtime and space: worst case is traverse the full size of the tree/the whole network
# O(n * m): n is the number of people, m is the connection among them

    # Solution B: Part II
    if sender not in network:
        return []

    q = []
    q.append(sender)

    visited_paths = {sender: None}
    # print(visited_paths)
    while q:
        the_sender = q.pop(0)
        # print(the_sender, q)

        if the_sender == recipient:
            return get_route(visited_paths, recipient)

        if the_sender in network:
            for person in network[the_sender]:
                if person not in visited_paths:
                    visited_paths[person] = the_sender
                    # print(visited_paths)
                    q.append(person)
        # print('---------------------------------------------')
    # if cannot find the recipient in the network, return empty
    return []


############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")
