
import math
import os

from .window import Window
from .loader import get_figures


def main():
    
    filename = 'input4.txt'
    # filename = 'input2.txt'
    # filename = 'input1.txt'
    path = os.path.dirname(__file__) + f'/../data/{filename}'

    width = 1100
    height = 600
    step = 40
    rotation_angle = math.pi/36
    focal = 300
    focal_step = 10
    focal_min = 20
    focal_max = 470

    safe_mode = False

    
    # DEFINE WINDOW OBJECT
    window = Window(
        width, height, 
        rotation_angle,
        step,
        focal, focal_step,
        focal_min, focal_max,
        safe_mode)

    # DATA LOADING FROM FILE
    figures = get_figures(path)
    window.figures = figures
    window.run()
    

if __name__ == "__main__":
    main()
