#
# ps8pr3.py (Problem Set 8, Problem 3)
#
# Image processing with loops and image objects
#
# Computer Science 111
# 

from cs111png import *

def invert(filename):
    """ loads a PNG image from the file with the specified filename
        and creates a new image in which the colors of the pixels are
        inverted.
        input: filename is a string specifying the name of the PNG file
               that the function should process.
        No value is returned, but the new image is stored in a file
        whose name is invert_filename, where filename is the name of
        the original file.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]

            # invert the colors of the pixel at row r, column c
            new_rgb = [255 - red, 255 - green, 255 - blue]
            img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'invert_' + filename
    img.save(new_filename)

def brightness(rgb):
    """ takes the RGB values of a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    return (21*red + 72*green + 7*blue) // 100

### PUT YOUR WORK FOR PROBLEM 3 BELOW. ###
def grayscale(filename):
    '''creates a grayscale copy of filename.'''
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)

            #change the rgb values of the image so that the red, green, and
            #blue values are all the brighness of the original image.
            #(We use the helper function brightness to find the brightness)
            #of the original image.
            new_rgb = [brightness(rgb), brightness(rgb), brightness(rgb)]
            img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'gray_' + filename
    img.save(new_filename)
    
def bw(filename, threshold):
    '''creates a black and white copy of filename'''
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)
            
            #The pixels's brightness using the brightness helper function.
            pixel_brightness = brightness(rgb)
            
            #If the pixel's brighness is greater than the threshold value,
            #set it white.
            if pixel_brightness > threshold:
                new_rgb = [255, 255, 255]
                img.set_pixel(r, c, new_rgb)
            
            #Else, set it black.
            else:
                new_rgb = [0,0,0]
                img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'bw_' + filename
    img.save(new_filename)

def fold_diag(filename):
    '''creates a folded copy of filename.'''
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)
            
            #If the row index is greater than the column index, set the 
            #pixel white.
            if r > c:
                new_rgb = [255, 255, 255]
                img.set_pixel(r, c, new_rgb)
        
    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'fold_' + filename
    img.save(new_filename)

if __name__ == '__main__':
    #Invert test case.
    invert('test.png')
    
    #grayscale test case.
    grayscale('spam.png')
    
    #bw test case.
    bw('spam.png', 100)
    
    #bw test case.
    fold_diag('spam.png')