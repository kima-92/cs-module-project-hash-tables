import random

words_dict = {}
stop_words = {}
start_words = {}

my_list = []

spec_char = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', ' ']
# Read in all the words in one go
with open("input.txt") as f:
    text = f.read()
    words = text.split()

    starting_word = words[30]

    # Saving the words in the dictionaries
    for i in range(0, len(words) - 1):
        word = words[i]
        next_word = words[i+1]

        my_list += [word]

        # If this word is in the words_dict
        if word in words_dict:
            # And if there is a next_word
            if next_word:
                # Add this next_word to this word's array
                words_dict[word] += [next_word]
            # Else: If there is NOT a next_word
            else:
                if word[-1] in spec_char:
                    # Add this word to stop_words
                    stop_words[word] = 1
        # Else: if this word is NOT in the words_dict
        else:
            # Add it

            # Add it to start_words if it starts with a capital or a "
            first = word[0]
            first_upper = first.upper()
            last = word[-1]

            if first == first_upper or first == '"':
                start_words[word] = 1

            # Add it to stop_words if it ends with a special char or a "
            if last in spec_char or last == '"':
                # Add this word to stop_words
                stop_words[word] = 1

            # And if there is a next_word
            if next_word:
                # Create an array for this word in 
                # the words_dict starting with next_word 
                words_dict[word] = [next_word]
            # Else: If there is NOT a next_word
            else:
                # Add it to the stop_words
                stop_words[word] = 1





    

# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here

