from jedd import getScore


def solve1(slides):
    slides = set(slides)
    max_s = 0
    max_slides = None
    for slide in slides:
        slides.remove(slide)
        s = getTotalScore(gen(slide, slides))
        slides.add(slide)
        if s > max_s:
            max_s = s
            max_slides = slides
    return max_slides



def gen(slide, slides):
    if len(slides) == 2:
        return [slides[0], slides[1]]
    lst = []
    max_s = 0
    max_slides = None
    lst.append(slide)
    for slide1 in slides:
        slides.remove(slide1)
        s = getScore(slide, slide1) + getTotalScore(gen(slide1, slides))
        slides.add(slide1)
        if s > max_s:
            max_s = s
            max_slides = slides
    lst.extend(max_slides)
    return max_slides


def getTotalScore(slides):
    sum = 0
    for i in range(0, len(slides)):
        sum = getScore(slides[i], slides[i+1])
    return sum
