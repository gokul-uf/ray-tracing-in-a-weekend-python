# Code that creates a simple PPM file with colour gradient

from tqdm import tqdm

image_width = 200
image_height = 100

if __name__ == "__main__":
    with open("../outputs/0-simple_image.ppm", "w") as f:
        f.write("P3\n")
        f.write("{} {}\n".format(image_width, image_height))
        f.write("255\n")

        for j in tqdm(range(image_height-1, -1, -1)):
            for i in range(image_width):
                r = i / image_width
                g = j / image_height
                b = 0.2

                ir = int(255.999 * r)
                ig = int(255.999 * g)
                ib = int(255.999 * b)

                f.write("{} {} {}\n".format(ir, ig, ib))

        print("All done!")


