# Code that creates a simple PPM file with colour gradient

from tqdm import tqdm
from vec3 import Vec3

image_width = 200
image_height = 100

if __name__ == "__main__":
    with open("../../outputs/1-simple_image.ppm", "w") as f:
        f.write("P3\n")
        f.write("{} {}\n".format(image_width, image_height))
        f.write("255\n")

        for j in tqdm(range(image_height-1, -1, -1)):
            for i in range(image_width):
                color = Vec3(i / image_width, j / image_height, 0.2)
                f.write("{}\n".format(color.write_colour()))

        print("All done!")


