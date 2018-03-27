from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    text_color = shapes[randint(0,3)]['text']
    color_of_shape = shapes[randint(0,3)]['color']

    return [
                text_color,
                color_of_shape,
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):

    if quiz_type == 0:
        for inf in shapes:
            if inf['text'] == text:
                rectangle = inf['rect']
    if quiz_type == 1:
        for inf in shapes:
            if inf['color'] == color:
                rectangle = inf['rect']
    from is_inside_def import is_inside
    t_f = is_inside([x,y],rectangle)
    return t_f
