from PIL import Image
import os

__all__ = [
    # "STANDARD_IMAGE_SIZE",
    # "STANDARD_IMAGE_MODE",
    # "load_image",
    # "get_image_format",
    # "get_image_size",
    # "get_image_colour_mode",
    # "save_image_as_jpeg",
    # "resize_image",
    # "get_subsection_of_image",
    # "standardise_img",
]

STANDARD_IMAGE_SIZE = (224, 224)
STANDARD_IMAGE_MODE = "RGB"


def load_image(image_path):
    image = Image.open(image_path)
    return image


def get_image_format(image: Image) -> str:
    return image.format


def get_image_size(image: Image) -> str:
    return tuple(image.size)


def get_image_colour_mode(image: Image) -> str:
    return image.mode


def save_image_as_jpeg(image: Image, target_filepath: str):

    if target_filepath.lower().endswith(".jpeg"):
        image.save(target_filepath)
    else:
        raise Exception("File suffix should end with '.jpeg'")


def resize_image(image: Image, target_size=STANDARD_IMAGE_SIZE):
    image = image.resize(target_size)
    return image


def get_subsection_of_image(image: Image, x_pos, y_pos, width, height):
    box = (x_pos, y_pos, width, height)
    cropped_image = image.crop(box)
    return cropped_image


def standardise_img(image_path, target_img_path):

    img = load_image(image_path)

    if not get_image_colour_mode(img) == "RGB":
        raise Exception("Image must be RGB")

    if not get_image_size(img) == STANDARD_IMAGE_SIZE:
        print("Resizing to {}....".format(STANDARD_IMAGE_SIZE))
        img = resize_image(img, STANDARD_IMAGE_SIZE)

    if not image_path.lower().endswith("jpeg"):
        print("Saving as jpeg...")
        save_image_as_jpeg(img, target_img_path)

