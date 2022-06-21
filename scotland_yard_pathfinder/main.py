# main.py
import pathfinder_basic as pfb
import pathfinder_standard as pfs


def catch_input():
    """
    Gets and validates user input for which game version to use.
    :return: int game_version
    """

    game_version = input("> ")

    while game_version not in ['1', '2']:
        print("Invalid Input - Please Enter 1 or 2...")
        game_version = input("> ")

    return int(game_version)


def main():
    print("############################################################\n"
          "#                 Scotland Yard Pathfinder                 #\n"
          "#  https://github.com/Foxtrt-com/Scotland-Yard-Pathfinder  #\n"
          "#                                                          #\n"
          "#  Please select the game version:                         #\n"
          "#    1. Basic                                              #\n"
          "#    2. Standard                                           #\n"
          "############################################################\n")

    # Get user input
    game_version = catch_input()

    if game_version == 1:
        # Run pfb (Pathfinder Basic)
        pfb.start()
    else:
        # Run pfs (Pathfinder Standard)
        pfs.start()

    # After a game, repeat if user wants to
    if input("Would you like to play again? Y/N\n> ").lower() == 'y':
        main()
    else:
        exit()


if __name__ == '__main__':
    main()
