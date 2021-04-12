import re


class Commands:

    def __init__(self, values):
        self.values = values

        if not re.sub(r"[^GDA]", "", values):
            raise ValueError(f"commands must be G,D or A")
