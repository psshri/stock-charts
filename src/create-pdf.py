import os
import time
from PIL import Image

image_files1 = [f for f in os.listdir('ohlc-charts/dw1') if f.endswith('.png')]
image_files2 = [f for f in os.listdir('ohlc-charts/dw2') if f.endswith('.png')]
image_files3 = [f for f in os.listdir('ohlc-charts/dw3') if f.endswith('.png')]
image_files4 = [f for f in os.listdir('ohlc-charts/dw4') if f.endswith('.png')]
image_files1 = sorted(image_files1)
image_files2 = sorted(image_files2)
image_files3 = sorted(image_files3)
image_files4 = sorted(image_files4)

image_files1_first = image_files1[:24]
image_files1_second = image_files1[24:48]
image_files1_third = image_files1[48:72]
image_files1_fourth = image_files1[72:96]
image_files1_fifth = image_files1[96:]


image_files2_first = image_files2[:24]
image_files2_second = image_files2[24:48]
image_files2_third = image_files2[48:72]
image_files2_fourth = image_files2[72:96]
image_files2_fifth = image_files2[96:]

image_files3_first = image_files3[:24]
image_files3_second = image_files3[24:48]
image_files3_third = image_files3[48:72]
image_files3_fourth = image_files3[72:96]
image_files3_fifth = image_files3[96:]

image_files4_first = image_files4[:24]
image_files4_second = image_files4[24:48]
image_files4_third = image_files4[48:72]
image_files4_fourth = image_files4[72:96]
image_files4_fifth = image_files4[96:]

im_list = []
counter = 0
for image in image_files1_first:
    print(counter)
    counter += 1
    im = Image.open(f'ohlc-charts/dw1/{image}')
    im = im.convert('RGB')
    im_list.append(im)
    # im.close()
im_list[0].save('ohlc-charts/PDFs/test.pdf', save_all=True, append_images=im_list[1:])
im.close()
print('going to sleep now')
time.sleep(100)
