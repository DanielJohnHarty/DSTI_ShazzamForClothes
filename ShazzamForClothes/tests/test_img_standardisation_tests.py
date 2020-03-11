import pytest
import os
from PIL import Image
from context import img_preparation, tests_root_dir
from img_preparation import standardise_img

test_dog_img = os.path.join(tests_root_dir, "TestFiles", "test_dog.jpeg")
test_dog_img_renamed = os.path.join(tests_root_dir, "TestFiles", "test_dog_jpeg.jpeg")
robot_img = os.path.join(tests_root_dir, "TestFiles", "robot.jpg")


def test_dog_image_opens():
    """
    Image loads correctly
    """
    try:
        image = standardise_img.load_image(test_dog_img)
    except IOError:
        pytest.fail("IOError -> Unable to access image at path")


def test_dog_image_is_jpg():
    img = standardise_img.load_image(test_dog_img)
    assert standardise_img.get_image_format(img) == "JPEG"


def test_dog_resolution():
    img = standardise_img.load_image(test_dog_img)
    assert standardise_img.get_image_size(img) == (1100, 619)


def test_dog_image_mode():
    img = standardise_img.load_image(test_dog_img)
    assert standardise_img.get_image_colour_mode(img) == "RGB"


def test_save_as_jpeg():
    img = standardise_img.load_image(test_dog_img)
    try:
        standardise_img.save_image_as_jpeg(img, test_dog_img_renamed)
    except Exception as e:
        raise pytest.fail("Unable to save as jpeg at target path")


def test_image_resized_to_target_size():
    img = standardise_img.load_image(test_dog_img)

    original_image_size = standardise_img.get_image_size(img)
    assert original_image_size != standardise_img.STANDARD_IMAGE_SIZE

    resized_image = standardise_img.resize_image(img)
    resized_image_size = standardise_img.get_image_size(resized_image)

    assert original_image_size != resized_image_size
    assert isinstance(original_image_size, tuple)


def test_get_subsection_of_image():
    # robot.jpg,6189,"{}",2,0,"{""name"":""rect"",""x"":53,""y"":15,""width"":118,""height"":73}","{""clothes"":""hat""}"
    img = standardise_img.load_image(robot_img)
    cropped_image = standardise_img.get_subsection_of_image(img, 53, 15, 118, 73)
    final_width = 118 - 53
    final_height = 73 - 15
    assert standardise_img.get_image_size(cropped_image) == (final_width, final_height)
