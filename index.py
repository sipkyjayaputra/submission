#1
def subNotLessThanZero(nums):
    arr = []
    for i in nums:
        notLessThanZero = True
        for j in nums:
            if i - j < 0:
                notLessThanZero = False
        if notLessThanZero:
            arr.append(i)
            
    return arr

print(subNotLessThanZero([1, 2, 3, 4]))

#2
def divNotSimilarWithOne(nums, x):
    arr = []
    for i in nums:
        if i / x != 1:
            arr.append(i)
            
    return arr

print(divNotSimilarWithOne([1, 2, 3, 4], 4))

#3
def wordLenEqualsToX(word, x):
    arr = []
    for i in word.split():
        if len(i) == x:
            arr.append(i)
            
    return arr

print(wordLenEqualsToX('souvernir loud four lost', 4))
            
            
            
            
            
            
