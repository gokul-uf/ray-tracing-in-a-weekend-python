from vec3 import Vec3

class Ray:
    def __init__(self, origin = None, direction = None):
        self.origin = origin if origin is not None else Vec3()
        self.direction = direction if direction is not None else Vec3()

    def at(self, t):
        return self.origin + t * self.direction
