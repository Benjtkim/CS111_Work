#
# ps7pr3.py (Problem Set 7, Problem 3)
#
# Images as 2-D lists
#
# Computer Science 111
# Date: 7/26/24
# Name: Benjamin Kim
# email: benjt@bu.edu
# Description: First set of problems dealing with 2D lists and loops to 
# manipulate images.

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []
    
    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    '''creates and returns a 2-D list of pixels with height rows and width 
    columns in which all of the pixels are green.'''
    #You have to save the image that's created by create_uniform_image onto
    #a variable and return it. Here, we pass the RGB value for green into 
    #pixel.
    image = create_uniform_image(height, width, [0, 255, 0])
    return image

def flip_horiz(pixels):
    #New 2D list for pixels using blank_image. len(pixels) represents the 
    #height of the image, and len(pixels[0]) represents the width.
    new_2D_pixels_list = blank_image(len(pixels), len(pixels[0]))
    
    #For each value in each sublist in new_2D_pixels_list, replace that value
    #with whatever the value is in pixels, except c is multiplied by -1 to
    #flip the image horizontally.
    for r in range(len(new_2D_pixels_list)):
       for c in range(len(new_2D_pixels_list[0])):
           new_2D_pixels_list[r][c] = pixels[r][-c - 1]
    
    return new_2D_pixels_list

def flip_vert(pixels):
    #New 2D list for pixels using blank_image. len(pixels) represents the 
    #height of the image, and len(pixels[0]) represents the width.
    new_2D_pixels_list = blank_image(len(pixels), len(pixels[0]))
    
    #For each value in each sublist in new_2D_pixels_list, replace that value
    #with whatever the value is in pixels, except r is multiplied by -1 to
    #flip the image vertically.
    for r in range(len(new_2D_pixels_list)):
       for c in range(len(new_2D_pixels_list[0])):
           new_2D_pixels_list[r][c] = pixels[-r - 1][c]
    
    return new_2D_pixels_list

def transpose(pixels):
    #New 2D list for pixels using blank_image. Here, the height and width
    #of the image need to be flipped so we put the code representing the width
    #where the height goes and the code representing the height where the 
    #width goes.
    
    new_2D_pixels_list = blank_image(len(pixels[0]), len(pixels))
    
    #Exact same logic as the final problem in the 2nd set of problems. 
    #For each value in the original 2D pixels list going right to left, the 
    #value in new_2D_pixels_list going up to down will become said value. 
    for r in range(len(new_2D_pixels_list)):
       for c in range(len(new_2D_pixels_list[0])):
           new_2D_pixels_list[r][c] = pixels[c][r]
    
    return new_2D_pixels_list

def rotate_clockwise(pixels):
    #Transpose the image then flip it horizontally to obtain a 90 degree, 
    #clockwise rotation.
    new_image1 = transpose(pixels)
    new_image2 = flip_horiz(new_image1)
    return new_image2
    
def rotate_counterclockwise(pixels):
    #Transpose the image then flip it vertically to obtain a 90 degree, 
    #counterclockwise rotation.
    new_image1 = transpose(pixels)
    new_image2 = flip_vert(new_image1)
    return new_image2

if __name__ == '__main__':
    
    #checking to ensure blank_image returns a green rectangle.
    pixels = blank_image(100, 50)
    save_pixels(pixels, 'blank.png')
    
    #checking to ensure flip_horiz flips spam.png horizontally.
    pixels = load_pixels('spam.png')
    flipped = flip_horiz(pixels)
    save_pixels(flipped, 'flip_spam.png')
    
    #checking to ensure flip_vert flips spam.png vertically.
    pixels = load_pixels('spam.png')
    flipped = flip_vert(pixels)
    save_pixels(flipped, 'flipv_spam.png')
    
    #checking to ensure transpose works correctly.
    pixels = load_pixels('spam.png')
    transp = transpose(pixels)
    save_pixels(transp, 'transp_spam.png')
    
    #checking to ensure rotate_clockwise works correctly.
    pixels = load_pixels('spam.png')
    rot_clockwise = rotate_clockwise(pixels)
    save_pixels(rot_clockwise, 'rot_clockwise_spam.png')
    
    #checking to ensure rotate_counterclockwise works correctly.
    pixels = load_pixels('spam.png')
    rot_counterclockwise = rotate_counterclockwise(pixels)
    save_pixels(rot_counterclockwise, 'rot_counterclockwise_spam.png')
    