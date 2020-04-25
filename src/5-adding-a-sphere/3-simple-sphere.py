# Code that draws a simple red sphere with a gradient background

from tqdm import tqdm
from vec3 import Vec3
from ray import Ray
from ray import ray_color_sphere

image_width = 200
image_height = 100

if __name__ == "__main__":
    with open("3-simple-sphere.ppm", "w") as f:
        f.write("P3\n")
        f.write("{} {}\n".format(image_width, image_height))
        f.write("255\n")

        # let's setup the camera and scene
        lower_left_corner = Vec3(-2., -1., -1.)
        horizontal = Vec3(4.0, 0., 0.) # could be any other simple X vector
        vertical = Vec3(0., 2., 0.) # could be any other simple Y vector
        origin = Vec3(0., 0., 0.)

        for j in tqdm(range(image_height-1, -1, -1)):
            for i in range(image_width):
                u = i / image_width
                v = j / image_height

                ray = Ray(origin, lower_left_corner + u * horizontal + v*vertical)
                color = ray_color_sphere(ray)
                f.write(color.write_colour() + "\n")

        print("All done!")


