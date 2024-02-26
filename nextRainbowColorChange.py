from PIL import Image
import re

def change_color(image_path, iterations=8):
    # Define the color mapping
    color_map = {
        (232, 20, 22): (255, 165, 0),    # e81416 to ffa500
        (255, 165, 0): (250, 235, 54),   # ffa500 to faeb36
        (250, 235, 54): (121, 195, 20),  # faeb36 to 79c314
        (121, 195, 20): (72, 125, 231),  # 79c314 to 487de7
        (72, 125, 231): (75, 54, 157),   # 487de7 to 4b369d
        (75, 54, 157): (112, 54, 157),   # 4b369d to 70369d
        (112, 54, 157): (232, 20, 22),   # 70369d to e81416
    }

    original_image_path = image_path

    for iteration in range(iterations):
        # Open the image
        with Image.open(image_path) as img:
            pixels = img.load()

            # Process each pixel
            for i in range(img.width):
                for j in range(img.height):
                    current_color = pixels[i, j][:3]  # Get RGB part of the pixel
                    if current_color in color_map:
                        new_color = color_map[current_color]
                        if len(pixels[i, j]) == 4:  # Check if the image is RGBA
                            new_color += (pixels[i, j][3],)  # Add alpha channel if present
                        pixels[i, j] = new_color

            # Generating new file name
            new_file_name = re.sub(r'(\d+)(?=\.\w+$)', lambda x: str(int(x.group(0)) + 1), image_path)
            image_path = new_file_name  # Update image_path for the next iteration

            # Save the new image as BMP
            img.save(new_file_name, format='BMP')

    # Reset the image_path to original for the next function call
    image_path = original_image_path

# Example usage
change_color("smallCertRR0.bmp")
