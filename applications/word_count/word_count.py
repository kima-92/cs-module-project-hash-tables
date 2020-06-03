
ignored = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', ' ']

def word_count(s):

    words = s.split()
    words_dict = {}
    bad_char = ""

    for word in words:
        new_word = ""
        
        for char in word:
            if char in ignored:
                bad_char += char
            else:
                new_word += char

        word = new_word.lower()
        
        if word in words_dict:
            words_dict[word] += 1

        elif word == "" or word == " ":
            break
        else: 
            words_dict[word] = 1
    
    if s == "":
        return {}
    else:
        return words_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))