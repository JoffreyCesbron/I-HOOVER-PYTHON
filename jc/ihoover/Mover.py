from Commands import Commands
from Grid import Grid
from Ordinal import Ordinal
from VacuumCleaner import VacuumCleaner


def orientate_to_the_right(vacuum_cleaner: VacuumCleaner):
    old_vacuum_cleaner_orientation = vacuum_cleaner.orientation
    if old_vacuum_cleaner_orientation == Ordinal.N.name: new_orientation = Ordinal.E.name
    if old_vacuum_cleaner_orientation == Ordinal.E.name: new_orientation = Ordinal.S.name
    if old_vacuum_cleaner_orientation == Ordinal.S.name: new_orientation = Ordinal.W.name
    if old_vacuum_cleaner_orientation == Ordinal.W.name: new_orientation = Ordinal.N.name

    new_vacuum_cleaner = VacuumCleaner(vacuum_cleaner.x, vacuum_cleaner.y, new_orientation)
    print_position_after(new_vacuum_cleaner)
    return new_vacuum_cleaner


def orientate_to_the_left(vacuum_cleaner: VacuumCleaner):
    old_vacuum_cleaner_orientation = vacuum_cleaner.orientation
    if old_vacuum_cleaner_orientation == Ordinal.N.name: new_orientation = Ordinal.W.name
    if old_vacuum_cleaner_orientation == Ordinal.W.name: new_orientation = Ordinal.S.name
    if old_vacuum_cleaner_orientation == Ordinal.S.name: new_orientation = Ordinal.E.name
    if old_vacuum_cleaner_orientation == Ordinal.E.name: new_orientation = Ordinal.N.name

    new_vacuum_cleaner = VacuumCleaner(vacuum_cleaner.x, vacuum_cleaner.y, new_orientation)
    print_position_after(new_vacuum_cleaner)
    return new_vacuum_cleaner


def try_to_move_forward(vacuum_cleaner: VacuumCleaner, grid: Grid):
    orientation = vacuum_cleaner.orientation
    maybe_new_x = vacuum_cleaner.x
    maybe_new_y = vacuum_cleaner.y

    max_x = grid.max_x
    max_y = grid.max_y

    if orientation == 'N':
        if vacuum_cleaner.y + 1 > max_y:
            print(f"The robot cannot go further than y={max_y}")
        else:
            maybe_new_y = vacuum_cleaner.y + 1

    if orientation == 'W':
        if vacuum_cleaner.x < 1:
            print(f"The robot cannot go further than x= 0")
        else:
            maybe_new_x = vacuum_cleaner.x - 1

    if orientation == 'S':
        if vacuum_cleaner.y < 1:
            print(f"The robot cannot go further than y= 0")
        else:
            maybe_new_y = vacuum_cleaner.y - 1

    if orientation == 'E':
        if vacuum_cleaner.x + 1 > max_x:
            print(f"The robot cannot go further than y={max_x}")
        else:
            maybe_new_x = vacuum_cleaner.x + 1

    new_vacuum_cleaner = VacuumCleaner(maybe_new_x, maybe_new_y, orientation)
    print_position_after(new_vacuum_cleaner)
    return new_vacuum_cleaner


def move_processing(grid: Grid, vaccuum_cleaner: VacuumCleaner, commands: Commands):
    printPositionBefore(vaccuum_cleaner, commands)

    for command in commands.values:
        if command == 'A': vaccuum_cleaner = try_to_move_forward(vaccuum_cleaner, grid)
        if command == 'D': vaccuum_cleaner = orientate_to_the_right(vaccuum_cleaner)
        if command == 'G': vaccuum_cleaner = orientate_to_the_left(vaccuum_cleaner)

    return vaccuum_cleaner


def print_position_after(vaccuum_cleaner: VacuumCleaner):
    print(f"=> result x={vaccuum_cleaner.x}, y={vaccuum_cleaner.y}, orientation={vaccuum_cleaner.orientation}")
    print("")


def printPositionBefore(vaccuum_cleaner: VacuumCleaner, commands: Commands):
    print(f"before doing [{commands.values[1]}] and remaining [{commands.values[1:]}]:")
    print(f"x={vaccuum_cleaner.x}, y={vaccuum_cleaner.y}, orientation={vaccuum_cleaner.orientation} ")
    print("")
