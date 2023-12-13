import os
from reportlab.pdfgen import canvas
from PIL import Image
import time

def convert_images_to_pdf(image_directory, output_pdf):
    png_files = [file for file in os.listdir(image_directory)]
    png_files = sorted(png_files)
    image_paths = [os.path.join(image_directory, file) for file in png_files]
    
    c = canvas.Canvas(output_pdf)

    counter=0
    for image_path in image_paths:
        print(image_path)
        print(counter)
        counter+=1
        img = Image.open(image_path)
        img_width, img_height = img.size
        
        c.setPageSize((img_width, img_height))
        c.drawInlineImage(img, 0, 0, width=img_width, height=img_height)
        
        c.showPage()
    c.save()