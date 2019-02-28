
sol = dict()
memoTable = dict()


def solve(allPosSlides):

    def getBest(allPosSlides, i, formerScore):

        if i == len(allPosSlides):
            return formerScore

        score = 0
        maxScore = score
        for j in range(i, len(allPosSlides) - 1):
            
            formerScore += getScore(allPosSlides[j], allPosSlides[j + 1])
            score = getBest(allPosSlides, j, formerScore)
            if score > maxScore:
                maxScore = score

        return maxScore

