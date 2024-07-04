# distance_between_points.py
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if __name__ == "__main__":
    x1, y1 = map(float, input("Enter coordinates of first point (x1 y1): ").split())
    x2, y2 = map(float, input("Enter coordinates of second point (x2 y2): ").split())
    dist = distance(x1, y1, x2, y2)
    print(f"The distance between points is: {dist:.2f}")
