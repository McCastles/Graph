
import math
import os

from .display import Display
from .loader import get_figures


def main():
    

    # CONSTANTS
    filename = 'input2.txt'
    path = os.path.dirname(__file__) + f'/../data/{filename}'

    
    width = 1200
    height = 800
    
    step = 100
    # cells = 16
    # cellsize = width // cells
    # scale_factor = 1.25
    
    rotation_angle = math.pi/18 # rad
    


    # DATA LOADING FROM FILE
    figures = get_figures(path)
    # print(figures)
    # figures = get_figures(path, cubes_qty, cellsize)


    # DEFINED DISPLAY OBJECT
    window = Display(width, height, rotation_angle, step)
    # window = Display(width, height, cellsize, rotation_angle, scale_factor)
    for i in range(len(figures)):
        window.figures[f'cube{i+1}'] = figures[i] 
    print(window.figures)
    window.set_camera()
    print(window.camera)
    # a
    window.run()

    

if __name__ == "__main__":
    main()
