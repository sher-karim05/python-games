def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, length + 1):
        if i not in numbers:
            output.append(i)
            return output
    listOfNumbers = [1,2,4,5,6,7,8,9,10]
    print(findMissingNumbers(listOfNumbers))
