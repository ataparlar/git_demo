def divide_by_six(a):
    return a/6  # ataparlar fixed the division

if __name__ == '__main__':
    print("Give the number to be divided by six.")
    a = input()
    result = divide_by_six(a)
    if(result == a/6):
        print("You fixed it.")
    else:
        print("Result is: ", result, ". Try again.")
