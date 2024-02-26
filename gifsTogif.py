import os
from PIL import Image

def create_animated_gif(directory, output_filename, frame_duration):
    frames = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".gif"):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as img:
                frames.append(img.copy())

    # Save into a GIF file that loops forever
    frames[0].save(output_filename, format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=frame_duration, loop=0)

# Directory containing GIFs, output filename, and frame duration in milliseconds
create_animated_gif('.', 'animated.gif', 50)
