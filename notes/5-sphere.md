## Ray Tracing A Sphere
Equation of a sphere with centre at origin and radius __R__:
`x^2 + y^2 + z^2 = R^2`
* If point `(x, y, z)` is inside the sphere, then `x^2 + y^2 + z^2 < R^2`
* If point `(x, y, z)` is on the sphere, then `x^2 + y^2 + z^2 = R^2`
* If point `(x, y, z)` is outside the sphere, then `x^2 + y^2 + z^2 > R^2`

If the centre is at (x1, y1, z1), then the equation becomes:
`(x - x1)^2 + (y - y1)^2 + (z - z1)^2 = R^2`


The above is tedious and can be abstracted away under the `Vec3` class.

We can replace the above in vector notataion, if **c** is the center (x1, y1, z1), and 
arbitrary point (x, y, z) is represented by **p**. Then all points on the sphere follow the relation

`(p - c).(p - c) = R^2`.

Let's replace `p` with the ray equation, so now **p** becomes **p(t)**, where
`**p(t)** = **a** + t**b**` from the previous defintion.

We can now plug **p(t)** into the sphere equation and solve for `t` as every other symbol is a known quantity. 

We get the following quadratic equation in `t`.
`(b.b)t^2 - 2 b.(a-c)t + ((a-c).(a-c) - R^2) = 0`.

The above can have 0, 1 or 2 solutions based on the values of the vector dot products (or the symbol of the discriminant).
 * 0 solutions means that the ray does not intersect with the sphere at all.(discriminant is negative).
 * 1 solution means that the ray hits the sphere at exactly **ONE** point (discriminant is zero)
 * 2 solutions means that the ray hits the sphere at one point and exits in another (discriminant is positive).

 We can use this to decide if a sphere is hit by a ray by just checking the discriminant.

### Simple Implementation
Let's have a sphere centered at (0, 0, -1). This is inside the plane. Let this have a radius of 0.5. Now we will repeat the same "ray tracing" as earlier, passing rays through the scene and checking if the rays hit the sphere or not.

So we will leverage the previous `ray_color` method and display the gradient only if the sphere is not hit by the ray. Else, we will display the color RED (RGB: 1, 0, 0).

The code for whether the sphere is hit or not is at: `src/sphere_utils.py:hit_sphere`.
And the entire tracer is at: `src/ray.py:ray_color_sphere`

