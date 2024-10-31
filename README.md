<<<<<<< HEAD
<<<<<<< HEAD
# png-metadata-viewer
Simple and fast way of viewing Stable Diffusion PNG files along side associated metadata.
=======
=======
# PNG Metadata Viewer

A Python GUI application to view image and metadata for PNG files, specifically designed for Stable Diffusion-generated metadata. The viewer provides a dark mode interface and allows navigation through images using arrow keys.

---
## Features

- Display PNG image previews and associated metadata.
- Dark mode UI with customizable colors.
- Navigate images using left/right arrow keys.
---
## Requirements

### System Dependencies
Before installing the Python packages, make sure the following system libraries are installed as these libraries are required for Pillow to handle image processing correctly:

```
sudo apt update
sudo apt install libjpeg-dev zlib1g-dev libpng-dev
```

### Python Packages
The necessary Python packages are listed in `requirements.txt`. To install them, run:

```
pip install -r requirements.txt
```

---
## Installation
### Clone the Repository:
```
git clone https://github.com/yourusername/png-metadata-viewer.git
cd png-metadata-viewer
```
### Create and Activate a Virtual Environment:

```
python3 -m venv venv-pnginfo
source venv-pnginfo/bin/activate  # On Windows: venv-pnginfo\Scripts\activate
```

### Install Python Packages:

```
pip install -r requirements.txt
```

### Install System Dependencies (if not done yet):

```
sudo apt install libjpeg-dev zlib1g-dev libpng-dev
```
### Usage
Run the script with the following command:

```
python png_metadata_viewer.py
```

---

## Contributing
Feel free to fork the repository and submit pull requests for new features or bug fixes.

License
This project is licensed under the MIT License.
>>>>>>> 96bfed8 (Initial commit)
