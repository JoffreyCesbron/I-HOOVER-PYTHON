class Grid:


    def __init__(self, max_x, max_y):

        self.max_x = max_x
        self.max_y = max_y

        if max_x < 1:
            raise ValueError(f"max_x must be greater than 0")
        if max_y < 1:
            raise ValueError(f"max_y must be greater than 0")
