# mrx_class.py

class MrX:
    def __init__(self, location, moves_left, double_move_tickets, black_tickets):
        self.location = location
        self.moves_left = moves_left
        self.double_move_tickets = double_move_tickets
        self.black_tickets = black_tickets
        self.moves_taken = []

    def move(self, location):
        """
        Moves Mr. X to the supplied location.
        :param location: where to move
        :return: none
        """

        self.location = location
        self.moves_taken.append(location)
        self.moves_left -= 1

    def double_move(self, location1, location2):
        """
        Moves Mr. X 2 spaces by using a black ticket.
        :param location1: first move
        :param location2: second move
        :return: none
        """

        if self.double_move_tickets > 0:
            self.move(location1)
            self.location = location2
            self.moves_taken.append(location2)
            self.double_move_tickets -= 1
        else:
            raise ValueError

    def use_black_ticket(self):
        """
        Mr. X uses a black ticket.
        :return: none
        """

        if self.black_tickets > 0:
            self.black_tickets -= 1
        else:
            raise ValueError
