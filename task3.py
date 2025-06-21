# task3.py
from PIL import Image
import os

def rotate_image(image_path, output_path, angle):
    """
    Rotates the image by the given angle and saves it to the output path.
    Ensures compatibility with JPEG format by converting to RGB mode.
    """
    # Open the image file
    img = Image.open(image_path)
    
    # Rotate the image; expand canvas to fit new dimensions
    rotated_img = img.rotate(angle, expand=True)

    # Convert to RGB if image has alpha channel (to support JPEG format)
    if rotated_img.mode == 'RGBA' or rotated_img.mode == 'LA':
        rotated_img = rotated_img.convert("RGB")
    
    # Save the rotated result to the designated file
    rotated_img.save(output_path)
    print(f"Image rotated by {angle}° has been saved to {output_path}")

def main():
    input_path = "images/input_image.jpg"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Apply rotation for different specified angles
    for angle in [45, 90]:
        output_path = os.path.join(output_dir, f"rotated_{angle}.jpg")
        try:
            rotate_image(input_path, output_path, angle)
        except Exception as e:
            print(f"Failed to rotate image by {angle}°: {e}")

if __name__ == "__main__":
    main()
