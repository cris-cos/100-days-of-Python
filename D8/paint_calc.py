import math

def paint_calc(height, width, cover):
    area = height * width
    paint_cans = math.ceil(area / cover)
    print(f"You will need {paint_cans} cans of paint for your wall.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)