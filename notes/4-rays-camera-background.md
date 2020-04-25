Ray is defined as following

`p(t) = **a** + t**b**` where **a** is the origin vector and **b** is the direction vector. `t` is a real number.  

Based on the values of `t`, you can move along the ray `p(t)`. Positive values of `t` lets you move along the direction of `b` and negative values in the opposite direction.

See `src/ray.py` for an implementation.

## Simple Ray Tracer
Sends rays through pixels and computes the colour seen in the direction of those rays.
Q. How many rays?
Q. In which directions?

### Steps
1. Calculate ray from eye to pixel (see above Q's)
2. Determine which objects the ray intersects (Q. how do you set up the scene?)
3. Compute color for that intersection point

**NOTE** Good idea to stick to rectangle images instead of square to make sure you don't transpose. This is easy to miss if you use a square image

**NOTE** Let's first have a simple gradient background to get up and running (following the author).  

## Outputing a Gradient Background
The gradient will be from White (RGB: 1,1,1) to Blue (RGB: 0.5, 0.7, 1.0).  
The interpolated color at any point will be a function of `y` **ONLY**

More specifically, we scale the ray direction to unit length, (so `y` will be between -1. and 1). Then rescale it to lie between \[0,1\]. 

We follow the convention that when `y` is `0`, we get white and when it is `1`, we get Blue (well, the blue hue we decide above). This forms an __Linear Interpolation__ or __lerp__.
Mathematically, this is written as  

`blendedValue = (1 - t) * startValue + t * endValue`  

In our case, `startValue` is WHITE and `endValue` is BLUE. You can change these(`start_color` and `end_color`) in the code to get different gradients. 

Since we are looking at value of `y` after normalizing the entire vector, we will see an horizontal gradient alongwith the expected vertical gradient. This is because the denominator (the vector's length) also changes.

### Steps for Linear Interpolation
1. Normalize the ray's direction vector (length of 1)
2. Rescale the direction vector's `y` to lie between (0,1) from (-1, 1).
3. Compute the blended colour using the above equation for `blendedValue`

See `src/ray.py:ray_color` method for the implementation.

### Camera Setup and Cordinate Convention
* Let's put the camera in the origin (0, 0, 0).
* Y axis is vertical, X axis horizontal, Positive Z goes outside the plane.
* The above is following a right hand cordinate system convention.

Q: Why are the following ranges chosen? 
A: I suppose to respect the (200, 100) image size and for easier computation.

The borders of the scene are as follows (in counter-clockwise direction):
1. Bottom Left: (-2, -1, -1)
2. Top Left: (-2, 1, -1)
3. Top Right: (2, 1, -1)
4. Bottom Right: (2, -1, -1)
* See: [here](https://raytracing.github.io/images/fig.cam-geom.jpg) for an image of the above setup.  

* The image will be traversed from bottom left using two offset vectors to the top right endpoint
* see `src/4-rays-camera-n-background/main.py` for implementation.



