from PIL import Image
import numpy


class Picture:  
    def __init__(self, filename): 
        self.filename = filename
        #find average pixel color
        self.pixel = self.find_average_rgb()
   
    def find_average_rgb(self):
        red = 0
        green = 0
        blue = 0
        im = Image.open(self.filename)
        print("Old photo size: ", im.size)
        width, height = im.size
        pixel_values = list(im.getdata())
        size = min(width, height)
        box = (width // 2 - size // 2, height // 2 - size // 2, width // 2 + size // 2, height // 2 + size // 2) 
        cropped_image = im.crop(box)
        cropped_image.save(self.filename)
        
        pixel_values = numpy.array(pixel_values).reshape((width, height, 3))
        print("New photo size: ", cropped_image.size)
        for x in range(size): 
            for y in range(size):
                print(pixel_values[x][y], end=" ")
            print("")
        return Pixel(red, green, blue)

class Pixel: 
    def __init__(self, red, green, blue): 
        self.red = red
        self.green = green
        self.blue = blue

source_pictures = []

def compile_source_file_data(source_files):
    for file in source_files: 
        source_pictures.append(Picture(file))

def process_picture():
    #compile_source_file_data(source_files)
    p = Picture("images/Australian-Shepherd.jpg")
    print("Hello world!!")