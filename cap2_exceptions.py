#GOAls
#Accept three arguments, first a prompt , a low , a high limit number
#if user enters a string that is not a integer, "Error: wrong input" , and ask to another input
#If insert a number outside a range "Error: the value is not within permitted range (min..max)"
#If its all right on print the result

def read_int(prompt, min, max):
    integer = int(input(prompt))

    if integer < min or integer > max :
        print("Error: the value is not within permitted range (min..max)")
    else:
        global flag
        flag = False
        return integer

flag = True
while flag: 
    try:
        v = read_int("Enter a number from -10 to 10: ", -10, 10)
    except:
        print("Error: wrong input")
        continue 

print("The number is:", v)
