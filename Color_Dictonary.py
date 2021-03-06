def Color(value):
    rgb_values = {
        0: (255, 0, 0),
        10: (255, 50, 0),
        20: (255, 100, 0),
        30: (255, 150, 0),
        40: (255, 200, 0),
        50: (255, 255, 0),
        60: (200, 255, 0),
        70: (150, 255, 0),
        80: (100, 255, 0),
        90: (50, 255, 0),
        100: (0, 255, 0),
    }
    return rgb_values.get(value, 0)