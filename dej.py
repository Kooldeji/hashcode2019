from jedd import getScore


def solve1(slides):
    slides = set(slides)
    max_s = 0
    max_slides = None
    for slide in slides:
        slides.remove(slide)
        solu = gen(slide, slides)
        s = getTotalScore(solu)
        slides.add(slide)
        if s > max_s:
            max_s = s
            max_slides = solu
    return max_slides



def gen(slide, slides):
    lst = []
    max_s = 0
    max_slides = None
    lst.append(slide)
    if len(slides) == 1:
        lst.extend(slides)
        return lst
    for slide1 in slides:
        slides.remove(slide1)
        solu = gen(slide1, slides)
        s = getScore(slide, slide1) + getTotalScore(solu)
        slides.add(slide1)
        if s > max_s:
            max_s = s
            max_slides = solu
    lst.extend(max_slides)
    return lst


def getTotalScore(slides):
    sum = 0
    for i in range(0, len(slides)-1):
        sum += getScore(slides[i], slides[i+1])
    return sum
