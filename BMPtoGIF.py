import os
from PIL import Image

def convert_bmp_to_gif(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".bmp"):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as img:
                filename_without_ext = os.path.splitext(filename)[0]
                gif_path = os.path.join(directory, filename_without_ext + '.gif')
                img.save(gif_path, 'GIF')

# Replace '.' with your directory if it's different
convert_bmp_to_gif('.')
