# EC7212 – Computer Vision and Image Processing
## Take Home Assignment 1

This repository contains Python programs for the first take-home assignment of EC7212 – Computer Vision and Image Processing. The tasks implement various image processing operations using Python libraries such as PIL, NumPy, and SciPy).

### Prerequisites
- Python 3.10
- Required libraries:
  - PIL (Pillow): `pip install Pillow`
  - NumPy: `pip install numpy`
  - SciPy: `pip install scipy`
- An input image file named `input_image.jpg` in the `images` directory.


### Tasks and Implementations

#### Task 1: Reduce Intensity Levels (`task1.py`)
- Reduces grayscale intensity levels in an image from 256 to to variable levels (2^n, n=0 to 8).
- Implementation: Normalizes pixel values, quantizes to specified levels, and saves output images.

#### Task 2: Spatial Averaging (`task2.py`)
- Applies 3x3, 10x10, and 20x20 average average spatial filters to to smooth an image.
- Implementation: Uses `scipy.ndimage.uniform_filter` for mean filtering.

#### Task 3: Image Rotation (`task3.py`)
- Rotates an image by 45° and 90°.
- Implementation: Uses PIL’s `rotate` method with canvas expansion and RGB conversion for JPEG compatibility.

#### Task 4: Block-wise Averaging (`task4.py`)
- Reduces spatial resolution by replacing 3x3, 5x5, and 7x7 blocks with their average intensity.
- Implementation: Reshapes image array to compute block means and replicates them.

### Running the Programs
1. Ensure the input image is in `images/input_image.jpg`.
2. Install dependencies: `pip install Pillow numpy scipy`.
3. Run each script individually:
   ```bash
   python task1.py
   python task2.py
   python task3.py
   python task4.py
   ```
4. Output images will be saved in the `output/` directory.

### Notes
- All scripts create the `output/` directory if it doesn’t exist.
- Error handling is implemented to catch invalid inputs or processing failures.
- The input image should be in a format supported by PIL (e.g., JPEG, PNG).
