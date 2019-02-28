from jedd import Photo, Slide
from timilehin import solve
from b70 import gen


def inp():
    fname = "a.txt"
    file = open(fname)
    n = int(file.readline())
    v_photos = []
    h_photos = []
    for i in range(n):
        line = file.readline().strip().split(" ")
        s = line[0]
        tags = line[2:]
        if s == "H":
            h_photos.append(Photo(i, s, set(tags)))
        else:
            v_photos.append(Photo(i, s, set(tags)))
    return v_photos, h_photos


def main_solve(h_photos, v_photos):
    slides = []
    for p in h_photos:
        slides.append(Slide([p]))
    slides.extend(gen(v_photos))
    return solve(slides)


photos = inp()
a = main_solve(photos[0], photos[1])
print(a)
