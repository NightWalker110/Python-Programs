#pip install pillow

from PIL import Image
img = Image.open("gs.jpeg") #your image name
blackAndWhite = img.convert("L")
blackAndWhite.save('bw.png')
blackAndWhite.show()
