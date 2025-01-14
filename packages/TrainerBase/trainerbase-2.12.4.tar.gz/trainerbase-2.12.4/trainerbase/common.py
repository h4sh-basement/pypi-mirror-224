from operator import mul, add
from itertools import starmap, repeat
from math import sqrt

from pymem.exception import MemoryReadError

from trainerbase.gameobject import GameInt, GameFloat
from trainerbase.scriptengine import Script


GameNumber = GameInt | GameFloat
Number = int | float
Coords = tuple[Number, Number, Number]


class Vector3:
    def __init__(self, x: Number, y: Number, z: Number):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __abs__(self):
        return sqrt(sum(d * d for d in self))

    def __mul__(self, other):
        return self.__apply_binary_function(other, mul)

    def __add__(self, other):
        return self.__apply_binary_function(other, add)

    def __apply_binary_function(self, other, function):
        if isinstance(other, (float, int)):
            other = repeat(other, 3)
        elif not isinstance(other, self.__class__):
            raise TypeError(f"Can't apply function {function}. Wrong type: {type(other)}")

        return self.__class__(*starmap(function, zip(self, other)))

    @classmethod
    def from_coords(cls, x1, y1, z1, x2, y2, z2):
        return cls(x2 - x1, y2 - y1, z2 - z1)

    def get_normalized(self):
        length = abs(self)
        return self.__class__(*(d / length for d in self))


class Teleport:
    def __init__(
        self,
        player_x: GameNumber,
        player_y: GameNumber,
        player_z: GameNumber,
        labels: dict[str, Coords] = None,
        dash_coefficients: Vector3 = None,
        minimal_movement_vector_length: float = 0.1,
    ):
        self.player_x = player_x
        self.player_y = player_y
        self.player_z = player_z
        self.labels = {} if labels is None else labels

        self.saved_position = None

        self.dash_coefficients = Vector3(5, 5, 5) if dash_coefficients is None else dash_coefficients
        self.previous_position = None
        self.current_position = None
        self.movement_vector = Vector3(0, 0, 0)
        self.minimal_movement_vector_length = minimal_movement_vector_length
        self.movement_vector_updater_script = None

    def set_coords(self, x: Number, y: Number, z: Number = 100):
        self.player_x.value = x
        self.player_y.value = y
        self.player_z.value = z

    def get_coords(self):
        return self.player_x.value, self.player_y.value, self.player_z.value

    def goto(self, label: str):
        self.set_coords(*self.labels[label])

    def save_position(self):
        self.saved_position = self.get_coords()

    def restore_saved_position(self) -> bool:
        """
        Returns False if position is not saved else True
        """

        if self.saved_position is None:
            return False

        self.set_coords(*self.saved_position)
        return True

    def update_movement_vector(self):
        try:
            self.current_position = self.get_coords()
        except MemoryReadError:
            return

        if self.previous_position is None:
            self.previous_position = self.current_position
            return

        movement_vector = Vector3.from_coords(*self.previous_position, *self.current_position)

        if abs(movement_vector) < self.minimal_movement_vector_length:
            return

        self.movement_vector = movement_vector.get_normalized()
        self.previous_position = self.current_position

    def dash(self):
        dash_movement_vector = self.movement_vector * self.dash_coefficients
        new_coords = Vector3(*self.get_coords()) + dash_movement_vector
        self.set_coords(*new_coords)

    def create_movement_vector_updater_script(self):
        if self.movement_vector_updater_script is None:
            self.movement_vector_updater_script = Script(self.update_movement_vector, enabled=True)

        return self.movement_vector_updater_script


def regenerate(current_value: GameNumber, max_value: GameNumber, percent: Number, min_value: Number = 1):
    if current_value.value < max_value.value:
        current_value.value += max(round(max_value.value * percent / 100), min_value)
