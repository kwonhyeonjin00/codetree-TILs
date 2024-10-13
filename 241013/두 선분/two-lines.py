x1, x2, x3, x4 = map(int, input().split())

string = "intersecting"

if x3 > x2 or x1 > x4:
    string = "nonintersecting"

print(string)