def majorityElement(self, A):
    majElem = A[0]
    count = 0
    for currElem in A:
        if currElem == majElem:
            count += 1
        elif count == 0:
            majElem = currElem
        else:
            count -= 1
    return majElem
