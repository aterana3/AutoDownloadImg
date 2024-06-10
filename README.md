---

# AutoDownloadImg-Python

AutoDownloadImg-Python is a simple tool for downloading multiple images using Python.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Make sure you have a `links.txt` file in the project's root directory containing the links of the images you want to download. If it doesn't exist, it will be created automatically with an example link.
2. Run the `main.py` script.
3. You will be prompted to enter the folder name where you want to save the downloaded images. If the folder doesn't exist, it will be created automatically.
4. The images will be downloaded into the specified folder.

## How it Works

The `main.py` script works as follows:

- It reads image links from the `links.txt` file.
- It iterates over each link and downloads the corresponding image.
- It saves the downloaded images in the folder specified by the user.

## Example `links.txt` File

```
https://www.python.org/static/img/python-logo.png
https://example.com/image1.jpg
https://example.com/image2.jpg
```

---