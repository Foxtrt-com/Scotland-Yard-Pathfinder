# pathfinder_basic.py

from mrx_class import MrX
from nodes import nodes


def get_choice():
    """
    Gets the user input based on what Mr. X did.
    :return: char move_type
    """

    print("Did Mr. X:\n"
          "move (m)\n"
          "double move (d)\n"
          "use a black ticket (b)?\n")

    move_type = input("> ")

    while move_type.lower() not in ('m', 'd', 'b'):
        print("Invalid Input - Please Enter 'm', 'd' or 'b' ")
        move_type = input("> ")

    return move_type


def get_location(possible_moves, double_move=False):
    """
    Gets the user input on what node Mr. X traveled to.
    :param possible_moves: List of possible moves from the current node.
    :param double_move: boolean to check if Mr. X has used a double move token.
    :return: int location1, int location2 (is 0 if not set)
    """
    location2 = 0

    if double_move:
        print("Where did Mr. X Move on Turn 1/2:")
        location1 = input("> ")
        while int(location1) not in possible_moves:
            print("Invalid Input - Please enter a valid node number")
            location1 = input("> ")

        print("Where did Mr. X Move on Turn 2/2:")
        location2 = input("> ")
        while int(location2) not in possible_moves:
            print("Invalid Input - Please enter a valid node number")
            location2 = input("> ")
    else:
        print("Where did Mr. X Move to:")
        location1 = input("> ")
        while int(location1) not in possible_moves:
            print("Invalid Input - Please enter a valid node number")
            location1 = input("> ")

    return int(location1), int(location2)


def start():
    """
    Main pathfinder loop to run through turns of Mr. X.
    :return: none
    """

    mr_x = MrX(location=82, moves_left=13, double_move_tickets=1, black_tickets=1)

    print("Playing with basic rules:\n"
          "Mr. X starts at 82\n\n"
          "Detectives start at:\n"
          "3 or less Detectives: 41, 46, 124\n"
          "4 Detectives: 41, 46, 124 & 142\n")

    while mr_x.moves_left > 0:
        next_locations = nodes[mr_x.location - 1].taxi_nodes
        for location in nodes[mr_x.location - 1].bus_nodes:
            if location not in next_locations:
                next_locations.append(location)

        # TODO: This only gets the next set of moves. We need ot figure out this (recursive?) enumeration.
        print("Possible next moves:")
        print(next_locations)

        move_type = get_choice()

        location1 = 0
        location2 = 0

        if move_type == 'm':
            while location1 == 0:
                try:
                    location1, location2 = get_location(next_locations)
                except (IndexError, ValueError):
                    print("Invalid Input - Please re-enter with a valid node number")
            mr_x.move(location1)
        elif move_type == 'd' and mr_x.double_move_tickets > 0:
            try:
                while location1 == 0 or location2 == 0:
                    try:
                        location1, location2 = get_location(next_locations, double_move=True)
                    except (IndexError, ValueError):
                        print("Invalid Input - Please re-enter with a valid node number")
                mr_x.double_move(location1, location2)
            except ValueError:
                print("No Double Move Tickets Remaining.")
        elif mr_x.black_tickets > 0:
            try:
                mr_x.use_black_ticket()
            except ValueError:
                print("No Black Tickets Remaining.")
        else:
            print("No Double/Black Tickets, Mr. X can only move normally.")

    print("Game End")
    print("Mr. X took the following moves:")
    print(mr_x.moves_taken)


if __name__ == '__main__':
    start()
