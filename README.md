# LED Moving Head Light DMX 3D Mapping

This repository contains a Python project that maps DMX channel values for a LED moving head light into 3D coordinates using rotation matrices. The code converts DMX channel 1 (pan) and DMX channel 3 (tilt) values into beam directions while respecting the fixture’s mechanical limits (Pan: 540°, Tilt: 205°), and visualizes the results with a 3D scatter plot.

## Features

- **DMX Mapping:**  
  Linearly scales DMX values (0–255) to the fixture's pan (0–540°) and tilt (0–205°) angles.
  
- **Rotation Matrices:**  
  Uses rotation matrices to simulate the physical movement of the light. Tilt is applied first (rotation about the X‑axis), followed by pan (rotation about the Z‑axis).

- **3D Visualization:**  
  Plots the resulting beam directions in 3D space using Matplotlib, helping you visualize the entire operating range of the fixture.

## Requirements

- Python 3.x
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/led-moving-head-dmx-mapping.git
   cd led-moving-head-dmx-mapping
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install numpy matplotlib
   ```

## Usage

Run the Python script to generate and visualize the 3D mapping of the DMX values:
  
```bash
python main.py
```

The script generates a meshgrid of DMX values, computes the corresponding 3D beam directions, and displays a 3D scatter plot of these points. You can adjust the grid resolution and other parameters within the script to refine the visualization.

## Code Overview

- **`dmx_to_xyz` Function:**  
  - **Input:** DMX channel values for pan and tilt.
  - **Mapping:**  
    - Pan (channel 1) is mapped from 0–255 to 0°–540°.  
    - Tilt (channel 3) is mapped from 0–255 to 0°–205°.
  - **Rotation Order:**  
    Applies a tilt rotation (about the X-axis) to the initial beam vector `[0, 1, 0]` and then a pan rotation (about the Z-axis) to get the final 3D direction.
  
- **Visualization:**  
  The computed 3D vectors are plotted using Matplotlib’s 3D scatter plot capabilities, allowing you to see the full range of motion of the LED moving head light.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the communities behind NumPy and Matplotlib for their excellent tools that make projects like this possible.

---

Feel free to customize the code or extend its functionality as needed for your specific application!

