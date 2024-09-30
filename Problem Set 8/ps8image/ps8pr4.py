#
# ps8pr4.py (Problem Set 8, Problem 4)
#
# Image processing with loops and image objects
#
# Computer Science 111
#

from cs111png import *

def flip_vert(filename):
    '''creates a copy of filename that has been flipped vertically.'''
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    
    #Create a blank image with the same dimensions as filename.
    new_img = Image(height, width)
    
    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            #get the rgb values for each pixel.
            rgb = img.get_pixel(r, c)
            #save that pixel onto new_image except start sourcing the 
            #original image from the bottom up so that new_image is
            #flipped vertically.
            new_img.set_pixel(height - r - 1, c, rgb) 
            
    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'flipv_' + filename
    new_img.save(new_filename)

def mirror_vert(filename):
    '''creates a new image in which the original image is “mirrored” 
    vertically.'''
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    
    #Create a blank image with the same dimensions as filename.
    new_img = Image(height, width)
    
    # process the image, one pixel at a time except stop once the loop is 
    #halfway through the original image.
    for r in range(int(height / 2)):
        for c in range(width):
            #get the rgb values for each pixel.
            rgb = img.get_pixel(r, c)
            #save that pixel onto new_image.
            new_img.set_pixel(r, c, rgb) 
    
    # process the image, one pixel at a time except stop once the loop is 
    #halfway through the original image.
    for r in range(int(height / 2)):
        for c in range(width):
            #get the rgb values for each pixel.
            rgb = img.get_pixel(r, c)
            #save that pixel onto new_image except start sourcing the 
            #original image from the bottom up so that the bottom half of 
            #new_image is flipped vertically.
            new_img.set_pixel(height - r - 1, c, rgb) 
            
    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'mirrorv_' + filename
    new_img.save(new_filename)
    
def reduce(filename):
    '''creates a new image that is half the size of the original image.'''
    '''creates a copy of filename that has been flipped vertically.'''
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the halved dimensions of new_image.
    height = int(img.get_height() / 2)
    width = int(img.get_width() / 2)
    
    #Create a blank image with the halved dimensions of new_image.
    new_img = Image(height, width)
    
    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            #get the rgb values for each pixel except each pixel will 
            #have to carry twice as much information.
            rgb = img.get_pixel(r * 2, c * 2)
            #save that pixel onto new_image.
            new_img.set_pixel(r, c, rgb) 
            
    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'reduce_' + filename
    new_img.save(new_filename)
    
def  extract(filename, rmin, rmax, cmin, cmax):
    '''extracts a portion of the original image that is specified by the other 
    four parameters.'''
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = rmax - rmin
    width = cmax - cmin
    
    #Create a blank image with the same dimensions as filename.
    new_img = Image(height, width)
    
    # process the image, one pixel at a time using the calculated height and 
    #width variables
    for r in range(height):
        for c in range(width):
            #get the rgb values for each pixel starting from the edges of the 
            #new image to the ends.
            rgb = img.get_pixel(r + rmin, c + cmin)
            #save that pixel onto new_image.
            new_img.set_pixel(r, c, rgb) 
            
    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'extract_' + filename
    new_img.save(new_filename)

if __name__ == '__main__':
    #flipv test case.
    flip_vert('spam.png')
    
    #mirror_vert test case.
    mirror_vert('spam.png')
    
    #reduce test case.
    reduce('spam_two.png')
    
    #extract test case.
    extract('spam.png', 90, 150, 75, 275)