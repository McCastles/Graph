
from .loader import get_figures
from .display import Display
import os


def main():
    

    # CONSTANTS
    cubes_qty = 1
    # path = 'input.txt'
    path = os.path.dirname(__file__) + '/../data/input.txt'
    # print(os.path.dirname(__file__) + '/../data/input.txt')

    
    width = 1200
    height = 800
    
    cells = 8
    cellsize = width // cells
    scale_factor = 1.25
    
    rotation_angle = 0.1 # rad
    


    # DATA LOADING FROM FILE
    figures = get_figures(path, cubes_qty, cellsize)


    # DEFINED DISPLAY OBJECT
    window = Display(width, height, cellsize, rotation_angle, scale_factor)

    for i in range(len(figures)):
        # window.add_figure(, )
        window.figures[f'cube{i+1}'] = figures[i] 
    window.run()

    

if __name__ == "__main__":
    main()
    

