from vec3 import Vec3
from vec3 import unit_vector

from sphere_utils import hit_sphere

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

    start_color = start_color if start_color is not None else Vec3(1, 1, 1) # White
    end_color = end_color if end_color is not None else Vec3(0.5, 0.7, 1.) # Blue

    unit_direction = unit_vector(r.direction)

    # scale [-1, 1] to [0, 1]
    t = 0.5*(unit_direction.y + 1.0)

    # do the linear interpolation from start to end color
    return (1. - t)*start_color + t*end_color

def ray_color_sphere(r, start_color = None, end_color = None, 
        sphere_center = None, radius = 0.5, hit_color=None):
    # This checks if the ray hits a sphere at center `c` and radius `radius` or not.
    # If it does, output `hit_color`, if not just display background gradient.
    # The defaults for radius and sphere_center are as per notes/4-sphere.md

    if not isinstance(r, Ray):
        raise TypeError("Expected 'Ray' object, got {}".format(type(r)))

    sphere_center = sphere_center if sphere_center is not None else Vec3(0, 0, -1)
    hit_color = hit_color if hit_color is not None else Vec3(1, 0, 0) # Red

    if hit_sphere(sphere_center, radius, r): # It's a hit!
        return hit_color

    return ray_color(r, start_color, end_color)
