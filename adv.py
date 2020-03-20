from room import Room
from player import Player
from world import World
from graph import Graph
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


room_dict = {}

# get all rooms
for i in range(len(room_graph)):
    room_dict[i] = room_graph[i][1]
    # print(room_graph[i][1])

stack = Stack()
visited = set()
path = []
neighbors = player.current_room.get_exits()

# start at room 0
stack.push(0)

while len(visited) < len(room_dict):
    # current room id
    current_id = stack.stack[-1]
    visited.add(current_id)
    # print(current_id)

    current_room = room_dict[current_id]
    # rooms that have not been visited
    undiscovered = []

    # store undiscovered rooms that neighbor current
    for direction, room_id in current_room.items():
        if room_id not in visited:
            undiscovered.append(room_id)

    # assign next room
    if len(undiscovered) > 0:
        next_room = undiscovered[0]
        stack.push(next_room)

    # backtracking
    else:
        stack.pop()
        next_room = stack.stack[-1]

    # survey rooms, if next room equals room id, add to path
    for direction, adjacent_id in current_room.items():
        if adjacent_id == next_room:
            traversal_path.append(direction)


#### OLD CODE
# def bfs(starting_room, destination_room):
#     """
#     Return a list containing the shortest path from
#     starting_vertex to destination_vertex in
#     breath-first order.

#     Will go row by row.
#     Everything that's one away, then two away, then three, etc

#     BFS will return the path as a list of room IDs.
#     You will need to convert this to a list of n/s/e/w directions
#     before you can add it to your traversal path.
#     """
#     # Create a queue
#     queue = Queue()
#     # ENQ PATH to starting vertex
#     queue.enqueue([starting_room])
#     # create set to store visited vertices
#     visited = set()
#     # while queue is not empty...
#     while queue.size() > 0:
#         # DQ first PATH
#         path = queue.dequeue()
#         # GRAB VERTEX FROM END OF PATH
#         room = path[-1]
#         # print("ROOM", room)
#         # Check if visited...
#         # If not...
#         # print("ROOOOOOOOOM", room)
#         if room not in visited:
#             print("ROOM ====", room)
#             # Mark as visited and
#             visited.add(room)
#             # CHECK IF IT IS TARGET
#             if room == destination_room:
#                 return path
#             # ENQ PATH to all neighbors by
#             exits = world.rooms[room].get_exits()
#             print("EXITS", exits)
#             for direction in exits:
#                 # MAKING COPY TO PATH
#                 copy = path.copy()
#                 print("ROOM ---->", room)
#                 new_room = world.rooms[room.id].get_room_in_direction(direction)
#                 # print("NEW_ROOM", new_room)
#                 # ENQ COPY
#                 queue.enqueue([*path, new_room])


# """
# Depth First Traversal
# STACK (LIFO)
# """
# stack = Stack()
# visited = []
# # starting at room 0
# stack.push(player.current_room)
# print("CURRENT ROOM", player.current_room)
# # while we haven't visited every room
# while stack.size() > 0:
#     # current room
#     current = stack.pop()
#     print("CURRENT BEFORE IF", current)
#     print("STACK IN WHILE", stack.stack)
#     if current.id not in visited:
#         # append current room if not visited before
#         visited.append(current.id)
#         print("VISITED", visited)
#         # get all possible exits to traverse
#         exits = current.get_exits()
#         for direction in exits:
#             # queue next rooms
#             next_room = current.get_room_in_direction(direction)
#             stack.push(next_room)
#             print("STACK IN FOR", stack.stack)


# ### add traversal path ###
# if player.current_room.id != 0:
#     print("no")
# # 1 less than length because we want to skip first room
# else:
#     for i in range(len(visited) - 1):
#         ## build traversal based on visited
#         direction = player.current_room.next_room(visited[i + 1])
#         print("DIR", direction)
#         if direction is not False:
#             # travel and add the direction
#             player.travel(direction)
#             traversal_path.append(direction)
#         # if neighboring
#         else:
#             # go back
#             path = bfs(player.current_room.id, visited[i + 1])
#             for room in path[1:]:
#                 direction = player.current_room.next_room(room)
#                 player.travel(direction)
#                 traversal_path.append(direction)
# # print("TRAVERSAL_PATH", traversal_path)
# # print("LEN", len(traversal_path))

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
