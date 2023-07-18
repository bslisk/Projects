# Enter a string and the program will reverse it and print it out.

def reverse_string(to_reverse: str) -> str:
    reversed_string = ""
    for i in range(len(to_reverse)-1, -1, -1):
        reversed_string += to_reverse[i]
    return reversed_string


text = input("Enter string to reverse: ")
print(reverse_string(text))
