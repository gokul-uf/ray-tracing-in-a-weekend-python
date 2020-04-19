"""
This is a python implementation of the Vec3 class.
In the interest of fewer lines of code, I've not added getters and setters.
Hence, method x(), y() and z() would be replaced by a direct obj.x / .y or .z

Instead, one can directly access and modify the attributes as needed.
"""
import math

class Vec3:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "{} {} {}".format(self.x, self.y, self.z)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __add__(self, v):
        return Vec3(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v):
        return Vec3(self.x - v.x, self.y - v.y, self.z - v.z)

    def __mul__(self, v):
        if isinstance(v, (int, float)):
            return Vec3(v*self.x, v*self.y, v*self.z)
        elif isinstance(v, Vec3):
            return Vec3(self.x * v.x, self.y * v.y, self.z * v.z)
        else:
            raise TypeError("Unsupported type '{}' for op: *".format(type(v)))

    def __rmul__(self, v): # This is to handle case: 3 * vec3
        return self * v

    def __truediv__(self, v): 
        # NOTE: Don't implement __rdiv__ because 3 / Vec makes no sense
        return Vec3(self.x / v, self.y / v, self.z / v)

    def __iadd__(self, v): # v is another Vec3 type
        assert isinstance(v, Vec3), "Needs to be a Vec3 object"
        self.x += v.x
        self.y += v.y
        self.z += v.z
        return self
            
    def __imul__(self, v): # v is numeric type
        if not isinstance(v, (int, float)):
            raise TypeError("unsupported type '{}' for __imul__".format(type(v)))
        self.x *= v
        self.y *= v
        self.z *= v
        return self
        
    def __itruediv__(self, v): # v is numeric type
        if not isinstance(v, (int, float)):
            raise TypeError("unsupported type '{}' for __itruediv__".format(type(v)))
        self.x /= v
        self.y /= v
        self.z /= v
        return self

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.x**2 + self.y**2 + self.z**2

    def write_colour(self):
        return "{} {} {}\n".format(int(255.99 * self.x), int(255.99 * self.y), int(255.99 * self.z))

    def dot(self, v):
        return dot(self, v)

    def cross(self, v):
        return cross(self, v)

def dot(v1, v2):
    return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z

def cross(v1, v2):
    return Vec3(v1.y*v2.z - v1.z*v2.y, v1.z*v2.x - v1.x * v2.z, v1.x*v2.y - v1.y*v2.x) 
