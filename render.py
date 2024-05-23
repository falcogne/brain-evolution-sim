from PIL import Image
import numpy as np

IMAGES_DICT = 'run_1'


def render_env(environment):
    pixels = make_pixel_list(environment)
    render_image(pixels)

def make_pixel_list(env):
    pass

def render_image(pixels):
    array = np.array(pixels, dtype=np.uint8)
    image = Image.fromarray(array)
    image.save(f"{IMAGES_DICT}/env.png")
    image.show("environment state")



if __name__ == "__main__":
    pixels = [
        [(255, 0, 0), (255, 0, 0), (255, 0, 0)], 
        [(0, 255, 0), (0, 255, 0), (0, 255, 0)], 
        [(0, 0, 255), (0, 0, 255), (0, 0, 255)], 
    ]
    pixels = np.random.random_integers(100, 200, (200, 200, 3))
    render_image(pixels)