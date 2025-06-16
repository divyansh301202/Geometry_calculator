import math

# 2D shapes
def square_area_perimeter(side):
    return side ** 2, 4 * side

def rectangle_area_perimeter(length, width):
    return length * width, 2 * (length + width)

def circle_area_perimeter(radius):
    return math.pi * radius ** 2, 2 * math.pi * radius

def triangle_area_perimeter(base, height, a, b, c):
    area = 0.5 * base * height
    perimeter = a + b + c
    return area, perimeter

# 3D shapes
def cube_surface_volume(side):
    surface_area = 6 * side ** 2
    volume = side ** 3
    return surface_area, volume

def cuboid_surface_volume(length, width, height):
    surface_area = 2 * (length * width + width * height + height * length)
    volume = length * width * height
    return surface_area, volume

def sphere_surface_volume(radius):
    surface_area = 4 * math.pi * radius ** 2
    volume = (4/3) * math.pi * radius ** 3
    return surface_area, volume

def cone_surface_volume(radius, height):
    slant_height = math.sqrt(radius**2 + height**2)
    surface_area = math.pi * radius * (radius + slant_height)
    volume = (1/3) * math.pi * radius**2 * height
    return surface_area, volume
