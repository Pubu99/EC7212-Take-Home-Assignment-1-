# task4.py
from PIL import Image
import numpy as np
import os

def block_average(image_path, output_path, block_size):
    """
    Apply block-wise averaging by replacing each block with its average intensity.
    :param image_path: Source image path
    :param output_path: Location to store the processed image
    :param block_size: Size of square blocks to average (e.g., 3 for 3x3)
    """
    # Open the image and convert it to grayscale
    img = Image.open(image_path).convert('L')
    img_array = np.array(img, dtype=np.float32)
    
    # Get original image dimensions
    height, width = img_array.shape
    
    # Add padding if needed so that width and height are divisible by block_size
    pad_height = (block_size - height % block_size) % block_size
    pad_width = (block_size - width % block_size) % block_size
    padded_array = np.pad(img_array, ((0, pad_height), (0, pad_width)), mode='edge')
    
    # Reshape array to isolate each block
    new_height, new_width = padded_array.shape
    blocks = padded_array.reshape(new_height // block_size, block_size,
                                  new_width // block_size, block_size)
    
    # Calculate the average pixel value for each block
    block_means = blocks.mean(axis=(1, 3))
    
    # Replicate each block mean across its original dimensions
    result = np.repeat(np.repeat(block_means, block_size, axis=0), block_size, axis=1)
    
    # Trim back to original image dimensions
    result = result[:height, :width].astype(np.uint8)
    
    # Save the final block-averaged image
    Image.fromarray(result).save(output_path)
    print(f"Saved block-averaged image ({block_size}x{block_size}) to {output_path}")

def main():
    input_path = "images/input_image.jpg"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Run block averaging for different block dimensions
    for block_size in [3, 5, 7]:
        output_path = os.path.join(output_dir, f"block_average_{block_size}x{block_size}.jpg")
        try:
            block_average(input_path, output_path, block_size)
        except Exception as e:
            print(f"Failed for block_size={block_size}: {e}")

if __name__ == "__main__":
    main()
