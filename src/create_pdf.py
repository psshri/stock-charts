import os
from reportlab.pdfgen import canvas
from PIL import Image
import time

# def get_png_files_in_directory(directory):
#     png_files = [file for file in os.listdir(directory) if file.lower().endswith('.png')]
#     png_files = sorted(png_files)
#     return png_files

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

# if __name__ == "__main__":

#     start_time = time.time()
    
#     # Specify the directory containing PNG images
#     image_directory_dw1 = "ohlc-charts/dw1"
#     # image_directory_dw2 = "ohlc-charts/dw2"
#     # image_directory_dw3 = "ohlc-charts/dw3"
#     # image_directory_dw4 = "ohlc-charts/dw4"
#     # image_directory_myport = "ohlc-charts/myport"

#     # Specify the output PDF file
#     output_pdf_dw1 = "ohlc-charts/PDFs/dw1.pdf"
#     # output_pdf_dw2 = "ohlc-charts/PDFs/dw2.pdf"
#     # output_pdf_dw3 = "ohlc-charts/PDFs/dw3.pdf"
#     # output_pdf_dw4 = "ohlc-charts/PDFs/dw4.pdf"
#     # output_pdf_myport = "ohlc-charts/PDFs/myport.pdf"

#     # Convert images to PDF
#     convert_images_to_pdf(image_directory_dw1, output_pdf_dw1)
#     # convert_images_to_pdf(image_directory_dw2, output_pdf_dw2)
#     # convert_images_to_pdf(image_directory_dw3, output_pdf_dw3)
#     # convert_images_to_pdf(image_directory_dw4, output_pdf_dw4)
#     # convert_images_to_pdf(image_directory_myport, output_pdf_myport)

#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     minutes = round(elapsed_time / 60, 2)
#     print(f"Time taken: {minutes} minutes")