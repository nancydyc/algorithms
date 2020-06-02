"""
                               Jaden

                  /           /       \       \
                Min         Amelia      Ren     Noam

        /     /    \        /   \    \
    William Jayden Omar Jaden [Adam]  Miguel

    /                \                  \
   ...               ...                ...


"""

def shortest_route(network, sender, recipient):
    """
        Given information about active users on the network, find the shortest
        oute for a message from one user (the sender) to another (the recipient).
        Return a list of users that make up this route.

        For example:
        >>> shortest_route({ 'Min'    : ['William', 'Jayden', 'Omar'], 'William': ['Min', 'Noam'], 'Jayden' : ['Min', 'Amelia', 'Ren', 'Noam'], 'Ren'    : ['Jayden', 'Omar'], 'Amelia' : ['Jayden', 'Adam', 'Miguel'], 'Adam'   : ['Amelia', 'Miguel', 'Sofia', 'Lucas'], 'Miguel' : ['Amelia', 'Adam', 'Liam', 'Nathan'], 'Noam'   : ['Nathan', 'Jayden', 'William'], 'Omar'   : ['Ren', 'Min', 'Scott']}, 'Jayden', 'Adam')
        ['Jayden', 'Amelia', 'Adam']

    """

    # locate the sender in the dictionary
    # when there is a recipient list, move to the next step
    # otherwise, return empty route list
    if sender not in network:
        return route

    # route = []
    q = []
    q.append((sender, sender))

    seen = set()
    seen.add(sender)

    while q:
        next_sender, route = q.pop(0)

        # if match, add the recipient to the route list and return route
        # if not, make it next sender
        for person in network[next_sender]:
            if person not in seen:
                seen.add(person)

                if person == recipient:
                    route += recipient
                    return route.split(',')

                q.append((person, route + ',' + person + ','))

    return route


############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")
