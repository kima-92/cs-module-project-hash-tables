

def no_dups(s):
    cache = {} 

    # Split the string into words
    words = s.split()
    new_string = ""

    # For each word in words
    for word in words:
        # If the word is not already in the cache
        if word not in cache:
            # If new_string is still EMPTY, 
            # Add the word with out a space in the front
            if new_string == "":
                cache[word] = 1
                new_string += word  
            # If new_string in NOT EMPTY,
            # Add the word with a space in the front 
            else:
                cache[word] = 1
                new_string += " "
                new_string += word
    # Return the new string
    return new_string





if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))