import os

from PIL import Image


def resize_image(input_path, output_path, size):
    """Resize an image to the specified size."""
    with Image.open(input_path) as img:
        img = img.convert("RGB")
        img = img.resize(size)
        img.save(output_path)


def batch_resize(input_dir, output_dir, size):
    """Resize all JPG and PNG images in the input directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)
            resize_image(input_path, output_path, size)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Resize JPG and PNG images.")
    parser.add_argument("input_dir", type=str, help="Directory containing the images to resize.")
    parser.add_argument("output_dir", type=str, help="Directory to save the resized images.")
    parser.add_argument("width", type=int, help="Width of the resized image.")
    parser.add_argument("height", type=int, help="Height of the resized image.")

    args = parser.parse_args()

    size = (args.width, args.height)
    batch_resize(args.input_dir, args.output_dir, size)
