#Q:1
def SUM(lIST):
    return sum(lIST)
numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
print(SUM(numbers))
# Q 2:
def smallest(TUPLE):
    return min(TUPLE)
numbers = (8,23,45,67,89,100,79)
print(smallest(numbers)) 
# Q 3:
def square_elements(SQUARE):
    return {x**2 for x in SQUARE}
numbers = {1, 2, 3, 4, 5,6,7,8,9}
print(square_elements(numbers)) 

#Q 4:
def keys(KEY):
    return list(KEY.keys())
dict = {'APPLE': 5, 'BANANA': 2, 'CARROT': 3}
print(keys(dict)) 