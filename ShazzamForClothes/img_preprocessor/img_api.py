from PIL import Image
import os


# Used as default values in all appropriate functions
# Should match image processing requirements
STANDARD_IMAGE_SIZE = (224, 224)
STANDARD_IMAGE_MODE = "RGB"


def load_image(image_path):
    """Load image as pillow object"""
    image = Image.open(image_path)
    return image


def get_image_format(image: Image) -> str:
    """Get str representing image format"""
    return image.format


def get_image_size(image: Image) -> str:
    """Get size of image in 2 dimensions
    as number of pixels per dimension e.g. (224, 224)"""
    return tuple(image.size)


def get_image_colour_mode(image: Image) -> str:
    """Get str representing image colour e.g. RGB"""
    return image.mode


def save_image_as_jpeg(image: Image, target_filepath: str):
    """Save pillow object to jpeg at the target_filepath"""
    if target_filepath.lower().endswith(".jpeg"):
        image.save(target_filepath)
    else:
        raise Exception("File suffix should end with '.jpeg'")


def resize_image(image: Image, target_size=STANDARD_IMAGE_SIZE):
    """Resize pillow Image to target size"""
    image = image.resize(target_size)
    return image


def get_subsection_of_image(image: Image, x_pos, y_pos, width, height):
    """Take pillow image and return a cropped version of it. Crop lines
    are determined with x_pos, y_pos, width and height parameters"""
    box = (x_pos, y_pos, width, height)
    cropped_image = image.crop(box)
    return cropped_image


def standardise_img(image_path, target_img_path):
    """A preconfigured workflow of operations to perform on an image
    stored at the passed target_filepath. All images passed to this
    function are persisted to the target_img_path having passed 
    through the same set of operations"""

    # Load the image
    img = load_image(image_path)

    # Refuse non RGB pallets
    if not get_image_colour_mode(img) == "RGB":
        raise Exception("Image must be RGB")

    # Resize image if different to STANDARD_IMAGE_SIZE
    if not get_image_size(img) == STANDARD_IMAGE_SIZE:
        print("Resizing to {}....".format(STANDARD_IMAGE_SIZE))
        img = resize_image(img, STANDARD_IMAGE_SIZE)

    # Persist to the directory at the target_img_path
    if not image_path.lower().endswith("jpeg"):
        print("Saving as jpeg...")
        save_image_as_jpeg(img, target_img_path)

