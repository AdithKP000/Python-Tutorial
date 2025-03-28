"""11.	Write a Python program to find the quadrant of a point, say (x,y)."""

def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    elif x > 0 and y < 0:
        return "Quadrant IV"
    elif x == 0 and y != 0:
        return "On the Y-axis"
    elif y == 0 and x != 0:
        return "On the X-axis"
    else:
        return "Origin"

# Example usage:
x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))
print("The point is in:", find_quadrant(x, y))


