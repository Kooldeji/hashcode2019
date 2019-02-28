from jedd import getScore


def solve(allPosSlides):

    sol = [-1 for i in range(len(allPosSlides))]
    memoTable = [-1 for i in range(len(allPosSlides))]

    def getBest(allPosSlides, i, formerScore):

        if memoTable[i] != -1:
            return memoTable[i]

        if i == len(allPosSlides):
            return formerScore

        score = formerScore
        maxScore = score
        for j in range(i, len(allPosSlides) - 1):

            formerScore += getScore(allPosSlides[i], allPosSlides[j + 1])
            score = getBest(allPosSlides, j+1, formerScore)
            if score >= maxScore:
                sol[j+1] = i
                maxScore = score

        return maxScore

    maxSore = getBest(allPosSlides, 0, 0)

    stack = []
    pos = len(allPosSlides) - 1
    while pos != 0:
        stack.append(allPosSlides[pos])
        pos = sol[pos]
    stack.append(allPosSlides[0])
    return stack


