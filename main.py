

def sum_numbers(a , b):
    return a + b

def sum_count_numbers(i, n):
    a = i
    while n > 0:
        a += 1
        i = i + a
        print ("I is: " + str(i) + " N is: " + str(n))
        n-=1
    
    return i


def main():
    print ("Hello World!")
    a = float(input("Start the count sum from: "))
    b = float(input("Sum a number of cycles: "))
    
    result = sum_count_numbers(a , b)
    sum_num = sum_numbers(a, b)
    print ("Count sum starting from : " + str(a) + " summed by " + str(b) + " is: " + str(result))
    print ("Sum of number " + str(a) + " + " + str(b) + " is : " + str(sum_num))




if __name__ == "__main__":
    main()