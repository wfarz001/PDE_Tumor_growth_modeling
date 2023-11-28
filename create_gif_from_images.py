# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 20:13:14 2023

@author: Walia Farzana
"""

import imageio
import os

# Directory containing PNG images
# image_dir = 'E:/Fall-2023/Numerical Methods/Project'

# # Output GIF file path
# output_gif_path = 'output.gif'

# # List all PNG files in the directory
# image_files = sorted([os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.endswith('.png')])

# # Create GIF
# with imageio.get_writer(output_gif_path, duration=0.5) as gif_writer:
#     for image_file in image_files:
#         image = imageio.imread(image_file)
#         gif_writer.append_data(image)

# print(f'GIF created successfully at: {output_gif_path}')



import imageio
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np



# Directory containing PNG images
image_dir = 'E:/Fall-2023/Numerical Methods/Project'

# Output GIF file path
output_gif_path = 'output_3.gif'
# Font settings
font_size = 16
# List all PNG files in the directory
image_files = sorted([os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.endswith('.png')])

# Create GIF with filename annotations at the top
with imageio.get_writer(output_gif_path, duration=0.5) as gif_writer:
    for image_file in image_files:
        # Read image
        image = imageio.imread(image_file)
        
        # Create a Pillow Image object from the numpy array
        pil_image = Image.fromarray(image)

        # Add filename as text at the top
        draw = ImageDraw.Draw(pil_image)
        font = ImageFont.load_default()  # Using default font
        filename = os.path.splitext(os.path.basename(image_file))[0]
        text_width, text_height = draw.textsize(filename, font=font)
        text_position = (((pil_image.width - text_width) // 2) + 180, (pil_image.height - text_height) // 2)  # Slightly towards the right
        draw.text(text_position, filename, fill=(0, 0, 0), font=font)  # Black text

        # Convert back to numpy array
        image_with_text = np.array(pil_image)

        # Append image to GIF
        gif_writer.append_data(image_with_text)

print(f'GIF created successfully at: {output_gif_path}')


