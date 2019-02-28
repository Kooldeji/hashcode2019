from jedd import Photo, Slide
from timilehin import solve
from b70 import gen
from dej import solve1, getTotalScore


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
    return h_photos, v_photos

def out(slides):
    fname = "out.txt"
    f = open(fname, "w")
    print(len(slides), file=f)
    for slide in slides:
        p = slide.Photos
        if len(p) > 1:
            print(p[0].Id, p[1].Id, file=f)
        else:
            print(p[0].Id, file=f)


def main_solve(h_photos, v_photos):
    slides = []
    for p in h_photos:
        slides.append(Slide([p]))
    slides.extend(gen(v_photos))
    return solve1(slides)


slides = inp()
a = main_solve(slides[0], slides[1])
print(getTotalScore(a))
out(a)
