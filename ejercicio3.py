def num_letters(n: int) -> int:
    """
    Returns the number of letters in the word form of the input integer.
    """
    # dictionary that maps digits to their word form
    digits = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }
    # string that will store the word form of the input integer
    word = ""
    # loop through each digit of the input integer
    for digit in str(n):
        word += digits[int(digit)] # add the word form of the digit to the string
    return len(word) # return the length of the word string

def stable_equilibrium(n: int) -> list:
    """
    Returns a list showing the path from the input integer to a stable equilibrium.
    """
    # list that will store the path to the stable equilibrium
    path = [n]
    while True:
        n = num_letters(n) # get the number of letters in the word form of the current number
        if n in path: # check if we have reached a stable equilibrium (if the current number of letters is already in the path)
            return path # return the path if we have reached a stable equilibrium
        else:
            path.append(n) # add the current number of letters to the path and continue the loop
