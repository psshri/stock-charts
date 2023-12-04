import os
from PIL import Image

image_files1 = [f for f in os.listdir('ohlc-charts/dw1') if f.endswith('.png')]
image_files2 = [f for f in os.listdir('ohlc-charts/dw2') if f.endswith('.png')]
image_files3 = [f for f in os.listdir('ohlc-charts/dw3') if f.endswith('.png')]
image_files4 = [f for f in os.listdir('ohlc-charts/dw4') if f.endswith('.png')]
image_files1 = sorted(image_files1)
image_files2 = sorted(image_files2)
image_files3 = sorted(image_files3)
image_files4 = sorted(image_files4)

image_files1_first = image_files1[:40]
image_files1_second = image_files1[40:80]
image_files1_third = image_files1[80:]

image_files2_first = image_files2[:40]
image_files2_second = image_files2[40:80]
image_files2_third = image_files2[80:]

image_files3_first = image_files3[:40]
image_files3_second = image_files3[40:80]
image_files3_third = image_files3[80:]

image_files4_first = image_files4[:40]
image_files4_second = image_files4[40:80]
image_files4_third = image_files4[80:]

im_list = []
counter = 0
for image in image_files1_first:
    print(counter)
    counter += 1
    im = Image.open(f'ohlc-charts/dw1/{image}')
    im = im.convert('RGB')
    im_list.append(im)
im_list[0].save('ohlc-charts/PDFs/test.pdf', save_all=True, append_images=im_list[1:])