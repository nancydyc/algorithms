"""

You are given a list of airplane tickets, in which each ticket is represented as
a pair of (from, to). You want to create an itinerary such that it visists all
the airplane tickets.

If there are multiple valid itinearies, you should return the itineary with the
smallest lexical order

The itinerary must start with SFO

We can assume that there will exist as least 1 valid itineary. Each ticket can
only be used once. Every ticket must be used.


Input1: [["NYC", "SEA"],["SFO", "NYC"], ["SEA", "LAX"]]
Output1: ["SFO", "NYC", "SEA", "LAX"]

Input2: [["NYC", "SEA"],["SFO", "NYC"], ["SEA", "LAX"], ["LAX", "MIA"],["SFO", "MIA"], ["MIA", "SFO"]]
Output2: ["SFO", "MIA", "SFO", "NYC", "SEA", "LAX", "MIA"]

["SFO", "NYC", "SEA", "LAX", "MIA", "SFO", "MIA"]
["SFO", "MIA", "SFO", "NYC", "SEA", "LAX", "MIA"]

                        SFO           ["SFO", "MIA"]
                      /    \\         ["MIA", "SFO"]
                     NYC   MIA        ["SFO", "NYC"]
                     /    /           ["NYC", "SEA"]
                   SEA   /            ["SEA", "LAX"]
                   /    /             ["LAX", "MIA"]
                   LAX

  SFO: ["NYC", "MIA"]
  NYC: ["SEA"]
  SEA: ["LAX"]
  LAX: ["SEA"]
  MIA: ["SFO"]

  SFO: ["NYC"]
  NYC: ["SEA"]
  SEA: ["LAX"]
  LAX: ["SEA"]
  MIA: ["SFO"]

  SFO: []
  NYC: []
  SEA: []
  LAX: []
  MIA: []

1. travel from SFO till all the tickets are used
  - put all the departure city in a dictionary
  - visit the destinatoins of departure city, SFO
    - to choose the smaller lexical order destination city:
    - sort the list in reverse order
    - save the destiniaton in the track list
    - pop the last destination city
  - put the destination city in visit order list
  - if all the destinations have been visited, cross the city off
  - destination becomes departure city
  - repeat until all the cities are crossed off
  - return the visit order

"""

def create_itinerary(tickets, departure_city):
  tickets_dict = {}
  for ticket in tickets:
    if ticket[0] not in tickets_dict:
      tickets_dict[ticket[0]] = [ticket[1]]
    else:
      tickets_dict[ticket[0]].append(ticket[1])

  visit_order = []
  visit_order.append(departure_city)

  while tickets_dict:
    tickets_dict[departure_city].sort(reverse=True)
    destination = tickets_dict[departure_city].pop()
    # print(destination)
    visit_order.append(destination)

    if tickets_dict[departure_city] == []:
      del tickets_dict[departure_city]

    departure_city = destination
    # print('------------------------------------------')

  return visit_order

itineraryA = create_itinerary([["NYC", "SEA"],["SFO", "NYC"], ["SEA", "LAX"], ["LAX", "MIA"],["SFO", "MIA"], ["MIA", "SFO"]], 'SFO')
print(itineraryA)

itineraryB = create_itinerary([["NYC", "SEA"],["SFO", "NYC"], ["SEA", "LAX"]], 'SFO')
print(itineraryB)
