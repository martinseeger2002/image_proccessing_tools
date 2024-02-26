import subprocess

def convert_gif_to_webp(input_gif, output_webp):
    gif2webp_path = r"C:\libwebp-1.3.2-windows-x64\bin\gif2webp"  # Update this path if necessary
    command = [gif2webp_path, input_gif, '-o', output_webp]
    subprocess.run(command)

# Example usage
convert_gif_to_webp('animated.gif', 'animated.webp')
