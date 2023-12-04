import os
from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
from PIL import Image

def get_png_files_in_directory(directory):
    png_files = [file for file in os.listdir(directory) if file.lower().endswith('.png')]
    png_files = sorted(png_files)
    return png_files

def convert_images_to_pdf(image_directory, output_pdf):
    image_paths = [os.path.join(image_directory, file) for file in get_png_files_in_directory(image_directory)]
    # c = canvas.Canvas(output_pdf, pagesize=letter)
    c = canvas.Canvas(output_pdf)
    image_paths = image_paths[:60]
    
    counter=0
    for image_path in image_paths:
        print(image_path)
        print(counter)
        counter+=1
        img = Image.open(image_path)
        # width, height = letter
        img_width, img_height = img.size
        
        # Calculate the aspect ratio to fit the image within the PDF page
        # aspect_ratio = img_width / img_height
        # new_width = min(img_width, width)
        # new_height = new_width / aspect_ratio
        
        # Center the image on the page
        # x_offset = (width - new_width) / 2
        # y_offset = (height - new_height) / 2
        
        # Draw the image on the PDF
        # c = canvas.Canvas(output_pdf, pagesize=(img_width, img_height))
        c.setPageSize((img_width, img_height))
        c.drawInlineImage(img, 0, 0, width=img_width, height=img_height)
        
        # Add a new page for the next image
        c.showPage()
    c.save()

if __name__ == "__main__":
    # Specify the directory containing PNG images
    image_directory = "ohlc-charts/dw1"

    # Specify the output PDF file
    output_pdf = "ohlc-charts/PDFs/test.pdf"

    # Convert images to PDF
    convert_images_to_pdf(image_directory, output_pdf)
