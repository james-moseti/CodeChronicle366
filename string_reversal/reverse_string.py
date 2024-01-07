# Reversing string without using inbuilt functions

def reverseString(stringToReverse):
    list_of_string_chars = list(stringToReverse)
    return "".join(list_of_string_chars[::-1])

if __name__ == "__main__":
    while True:
        word = input("Enter the word to reverse(q to quit): ")
        if word == 'q':
            break
        print(reverseString(word))
        