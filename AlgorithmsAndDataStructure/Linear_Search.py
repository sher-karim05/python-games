#In linear search program iterates through each item and return a result
def linear_search(list, target):
    """
    Retruen the index position of the target index
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
        return None

#         Verify function
def verify_target(index):
    if index is not None:
        print("Target is at index: ", index)
    else:
        print("Target not found")

numbers = [1,2,3,4,5,6,7,8,9]

result = linear_search(numbers, 7)
verify_target(result)
