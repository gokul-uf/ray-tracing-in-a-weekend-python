from vec3 import dot

def hit_sphere(center, radius, r):
    oc = r.origin - center
    a = dot(r.direction, r.direction)
    b = 2. * dot(oc, r.direction)
    c = dot(oc, oc) - radius*radius
    discriminant = b**2 - 4*a*c
    return discriminant > 0

