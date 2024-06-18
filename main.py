import os
from PIL import Image


def square_crop(src_path, output_dir, resolution=600, default_size=1000):
    image = Image.open(src_path)
    w, h = image.size
    os.makedirs(output_dir, exist_ok=True)
    extension = src_path.split('.')[-1]
    new_name = str(resolution) + '.' + extension

    if h != default_size or w != default_size:
        if h < resolution or w < resolution:
            if w > h:
                resolution = h
            else:
                resolution = w
        if w == h:
            image = image.resize((resolution, resolution))
            image.save(os.path.join(output_dir, new_name))

        elif w > h:
            left = (w - h)/2
            top = 0
            right = (w + h)/2
            bottom = h
            image = image.crop((left, top, right, bottom))
            image = image.resize((resolution, resolution))
            image.save(os.path.join(output_dir, new_name))
        else:
            left = 0
            top = (h - w)/2
            right = w
            bottom = (h + w)/2
            image = image.crop((left, top, right, bottom))
            image = image.resize((resolution, resolution))
            image.save(os.path.join(output_dir, new_name))


INPUT_DIR = 'input'
ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'webp']
OUTPUT_DIR = 'output'

TARGET_SIZES = [48, 72, 96, 144, 168, 192, 512]

def process_file(image_path):
    for size in TARGET_SIZES:
        square_crop(image_path, OUTPUT_DIR, size)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for file in os.listdir(INPUT_DIR):
        if file.split('.')[-1] in ALLOWED_EXTENSIONS:
            process_file(os.path.join(INPUT_DIR, file))


if __name__ == '__main__':
    main()