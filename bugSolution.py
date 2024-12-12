def function(a, b):
    try:
        return int(a) + int(b)  #Attempt to convert both to integers
    except ValueError:
        return str(a) + str(b) #If conversion fails, concatenate as strings

result = function(5, '10')
print(result)

result2 = function('hello', 'world')
print(result2)