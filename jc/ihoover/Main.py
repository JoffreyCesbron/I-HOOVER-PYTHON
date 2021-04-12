from Commands import Commands
from Grid import Grid
from Mover import move_processing
from Ordinal import Ordinal
from VacuumCleaner import VacuumCleaner

if __name__ == '__main__':
    grid = Grid(5, 10)
    vaccum_cleaner = VacuumCleaner(5, 5, Ordinal.N.name)
    commands = Commands("DADADADAA")

    vaccuum_cleaner_position = move_processing(grid, vaccum_cleaner, commands)
