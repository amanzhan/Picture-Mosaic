from PIL import Image
import numpy
import math
import os
import progressbar

bar = progressbar.ProgressBar(max_value=2000)
counter = 1

class Picture:  
    def __init__(self, filename): 
        self.filename = filename
        #find average pixel color
        self.pixel = self.find_average_rgb()
   
    def find_average_rgb(self):
        global counter
        bar.update(counter)
        counter += 1
        red = 0
        green = 0
        blue = 0
        try:
            im = Image.open(self.filename)
        except:
            return Pixel(-999999999, -999999999, -999999999)
        width, height = im.size
        size = min(width, height)
        box = (width // 2 - size // 2, height // 2 - size // 2, width // 2 + size // 2, height // 2 + size // 2) 
        cropped_image = im.crop(box)
        cropped_image.save(self.filename)
        if im.mode != 'RGB':
            im = im.convert(mode='RGB')
        try:
            pixel_values = list(im.getdata())
            pixel_values = numpy.array(pixel_values).reshape((width, height, 3))
        except:
            print(self.filename)
            print(im.mode)
            exit(1)
        avg_red = 0
        avg_blue = 0
        avg_green = 0
        for x in range(size): 
            for y in range(size):
                red, green, blue = pixel_values[x][y]
                avg_red += red
                avg_green += green
                avg_blue += blue
        avg_red = avg_red // (size * size)
        avg_blue = avg_blue // (size * size)
        avg_green = avg_green // (size * size)
        return Pixel(avg_red, avg_green, avg_blue)

class Pixel: 
    def __init__(self, red, green, blue): 
        self.red = red
        self.green = green
        self.blue = blue

source_pictures = []

def compile_source_file_data(source_files):
    for file in source_files: 
        source_pictures.append(Picture("source/" + file))

def find_nearest_image(red, green, blue):
    min_distance = 100000000000000
    filename = ""
    for pic in source_pictures: 
        distance = math.sqrt((red - pic.pixel.red)**2 + (green - pic.pixel.green)**2 + (blue - pic.pixel.blue)**2)
        if distance < min_distance: 
            min_distance = distance
            filename = pic.filename
    return filename

def generate_mosaic(picture_path):
    im = Image.open(picture_path)
    old_width, old_height = im.size
    im.thumbnail(100, 100)
    im.save("pixelated_photo.jpg") 
    width, height = im.size
    stock_im_width = old_width // width
    stock_im_height = old_height // height
    pixel_values = list(im.getdata())
    pixel_values = numpy.array(pixel_values).reshape((width, height, 3))
    im.resize(width * stock_im_width, height * stock_im_height)
    im.save("pixelated_photo.jpg")
    
    for h in range(width):
        for w in range(height):
            red = pixel_values[w][h][0]
            green = pixel_values[w][h][1]
            blue = pixel_values[w][h][2]
            replacement = find_nearest_image(red, green, blue) #returns filename of best image
            repl_photo = Image.open(replacement)
            repl_photo.resize(stock_im_width, stock_im_height)
            im.paste(repl_photo, (w * stock_im_width, h * stock_im_height)) # Todo: fix the w and h offsets

            

def process_picture(target, source_dir):
    print("Generating picture mosaic...")
    source_files = os.listdir(source_dir)
    compile_source_file_data(source_files)
    generate_mosaic(target)
    print("Picture mosaic generated!")