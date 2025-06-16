from fastapi import FastAPI
from pydantic import BaseModel
from geometry_calculations import *

app = FastAPI()

# ----------------- 2D MODELS -----------------
class Square(BaseModel):
    side: float

class Rectangle(BaseModel):
    length: float
    width: float

class Circle(BaseModel):
    radius: float

class Triangle(BaseModel):
    base: float
    height: float
    a: float
    b: float
    c: float

# ----------------- 3D MODELS -----------------
class Cube(BaseModel):
    side: float

class Cuboid(BaseModel):
    length: float
    width: float
    height: float

class Sphere(BaseModel):
    radius: float

class Cone(BaseModel):
    radius: float
    height: float

# ----------------- 2D Endpoints -----------------
@app.post("/area_perimeter/square")
def square(data: Square):
    area, perimeter = square_area_perimeter(data.side)
    return {"area": area, "perimeter": perimeter}

@app.post("/area_perimeter/rectangle")
def rectangle(data: Rectangle):
    area, perimeter = rectangle_area_perimeter(data.length, data.width)
    return {"area": area, "perimeter": perimeter}

@app.post("/area_perimeter/circle")
def circle(data: Circle):
    area, perimeter = circle_area_perimeter(data.radius)
    return {"area": area, "perimeter": perimeter}

@app.post("/area_perimeter/triangle")
def triangle(data: Triangle):
    area, perimeter = triangle_area_perimeter(data.base, data.height, data.a, data.b, data.c)
    return {"area": area, "perimeter": perimeter}

# ----------------- 3D Endpoints -----------------
@app.post("/surface_volume/cube")
def cube(data: Cube):
    sa, vol = cube_surface_volume(data.side)
    return {"surface_area": sa, "volume": vol}

@app.post("/surface_volume/cuboid")
def cuboid(data: Cuboid):
    sa, vol = cuboid_surface_volume(data.length, data.width, data.height)
    return {"surface_area": sa, "volume": vol}

@app.post("/surface_volume/sphere")
def sphere(data: Sphere):
    sa, vol = sphere_surface_volume(data.radius)
    return {"surface_area": sa, "volume": vol}

@app.post("/surface_volume/cone")
def cone(data: Cone):
    sa, vol = cone_surface_volume(data.radius, data.height)
    return {"surface_area": sa, "volume": vol}
