from jedd import Photo


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
            h_photos.append(Photo(i, s, tags))
        else:
            v_photos.append(Photo(i, s, tags))
    solve(photos)
inp()