from PIL import Image

im01 =Image.open("2.jpg")
print(im01.mode)
im_c=im01.convert("L")
print(im_c.mode)
im_c.show()
im01.show()
