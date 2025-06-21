# task2.py
from PIL import Image
import numpy as np
import os
from scipy.ndimage import uniform_filter

def spatial_average(image_path, output_path, kernel_size):
   
    # Open the image and convert it to a grayscale format
    img = Image.open(image_path).convert('L')
    img_array = np.array(img, dtype=np.float32)
    
    # Apply mean filtering using a square kernel of the given size
    averaged_array = uniform_filter(img_array, size=kernel_size)
    averaged_array = averaged_array.astype(np.uint8)
    
    # Export the smoothed image to the specified location
    Image.fromarray(averaged_array).save(output_path)
    print(f"Averaged image with kernel size {kernel_size}x{kernel_size} saved to {output_path}")

def main():
    input_path = "images/input_image.jpg"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Run filtering with various kernel dimensions
    for kernel_size in [3, 10, 20]:
        output_path = os.path.join(output_dir, f"average_{kernel_size}x{kernel_size}.jpg")
        try:
            spatial_average(input_path, output_path, kernel_size)
        except Exception as e:
            print(f"Failed for kernel_size={kernel_size}: {e}")

if __name__ == "__main__":
    main()
