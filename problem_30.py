# Problem 30: Calculate area of circle
# Find and fix the error

def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

r = 5  # use a number instead of a string
print(f"Area: {area_of_circle(r)}")
