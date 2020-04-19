figure_type = str(input())
if figure_type == 'square':
    figure_side_1 = float(input())
    figure_area = float(figure_side_1 * figure_side_1)
    print(f'{figure_area:.3f}')
elif figure_type == 'rectangle':
    figure_side_1 = float(input())
    figure_side_2 = float(input())
    figure_area = float(figure_side_1 * figure_side_2)
    print(f'{figure_area:.3f}')
elif figure_type == 'circle':
    figure_radius = float(input())
    from math import pi
    figure_area = float(pi * figure_radius* figure_radius)
    print(f'{figure_area:.3f}')
else:
    figure_side = float(input())
    figure_height = float(input())
    figure_area = float(figure_side * figure_height / 2)
    print(f'{figure_area:.3f}')