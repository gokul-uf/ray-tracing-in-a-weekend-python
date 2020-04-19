from vec3 import Vec3
from vec3 import unit_vector

class Ray:
    def __init__(self, origin = None, direction = None):
        self.origin = origin if origin is not None else Vec3()
        self.direction = direction if direction is not None else Vec3()

    def at(self, t):
        return self.origin + t * self.direction

def ray_color(r, start_color = None, end_color = None):
    # This implements the linear interpolation discussed in the notes.
    # change the start and end vectors for different gradients

    if not isinstance(r, Ray):
        raise TypeError("Expected 'Ray' object, got {}".format(type(r)))
    unit_direction = unit_vector(r.direction)

    if not start_color:
        start_color = Vec3(1, 1, 1) # White

    if not end_color:
        end_color = Vec3(0.5, 0.7, 1.0) # Blue

    # scale [-1, 1] to [0, 1]
    t = 0.5*(unit_direction.y + 1.0)

    # do the linear interpolation from start to end color
    return (1. - t)*start_color + t*end_color
