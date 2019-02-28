from jedd import getScore


def solve(allPosSlides):

    sol = [-1 for i in range(len(allPosSlides))]
    memoTable = [-1 for i in range(len(allPosSlides))]
    done = set()

    def getBest(allPosSlides, i, formerScore):

        if i == len(allPosSlides):
            return formerScore

        if i != -1 and memoTable[i] != -1:
            return memoTable[i]

        score = formerScore
        maxScore = score
        for j in range(i + 1, len(allPosSlides)):
            for photo in allPosSlides[j].Photos:
                if photo.Id in done:
                    continue
            for photo in allPosSlides[j].Photos:
                done.add(photo.Id)
            if i != -1:
                formerScore = 0
            else:
                formerScore += getScore(allPosSlides[i], allPosSlides[j])

            score = getBest(allPosSlides, j, formerScore)
            if score >= maxScore:
                sol[j] = i
                maxScore = score

            for photo in allPosSlides[j].Photos:
                done.remove(photo.Id)

        memoTable[i] = maxScore
        return maxScore

    maxScore = getBest(allPosSlides, -1, 0)

    stack = []
    pos = len(allPosSlides) - 1
    while pos != -1:
        stack.append(allPosSlides[pos])
        pos = sol[pos]
    return stack


