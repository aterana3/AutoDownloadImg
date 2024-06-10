import requests
import os
from pathlib import Path

file_links = Path("links.txt")
folder_images = Path("images")

def init():
    if not file_links.exists():
        file_links.write_text("https://www.python.org/static/img/python-logo.png")
    if not folder_images.exists():
        folder_images.mkdir()

def get_url_img(line):
    line = line.strip()
    if line.startswith('<img') and 'src="' in line:
        start_index = line.find('src="') + len('src="')
        end_index = line.find('"', start_index)
        url = line[start_index:end_index]
        return url
    else:
        return line

def download_image(folder_name_toSave):
    folder_toSave = Path(os.path.join(folder_images, folder_name_toSave))
    if not folder_toSave.exists():
        folder_toSave.mkdir()
    
    with open(file_links, "r") as file_links_open:
        array_lines = file_links_open.readlines()
        
        for str_line in array_lines:
            str_url = get_url_img(str_line)
            file_img = os.path.join(folder_toSave, str_url.split('/')[-1])
            
            with open(file_img, "wb") as file_img_wb:
                response_url = requests.get(str_url)
                file_img_wb.write(response_url.content)
                print(f"Downloaded {file_img}")
        
        print("Download completed in folder: ", folder_toSave)
        
if __name__ == "__main__":
    init()
    folder_toSave = input("Enter the folder name to save the images: ")
    download_image(folder_toSave)
