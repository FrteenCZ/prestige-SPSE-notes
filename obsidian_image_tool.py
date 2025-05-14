from rembg import remove
from PIL import Image
from io import BytesIO

def remove_background(input_path, output_path):
    with open(input_path, 'rb') as inp:
        input_data = inp.read()
        result = remove(input_data)
        with open(output_path, 'wb') as out:
            out.write(result)


remove_background('input_image.png', 'output_image.png')