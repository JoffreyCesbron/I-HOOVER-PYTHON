from Ordinal import Ordinal


class VacuumCleaner:

    def __init__(self, x, y, orientation):

        self.x = x
        self.y = y
        self.orientation = orientation

        if x < 0:
            raise ValueError(f"x must be greater than 0")
        if y < 0:
            raise ValueError(f"y must be greater than 0")
        if orientation not in Ordinal._member_names_:
            raise ValueError(f"Orientation must be 'N','E','S' or 'W'")
