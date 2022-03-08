# CPE 101-01
# LAB 6: Str Function
# Name: Miles Herrman   
# Section: 3

# Purpose: This function returns (in order) all the vowels in a given string
def vowel_extractor(input_str: str) -> str:
    list_of_vowels = "aeiouAEIOU"
    vowels = ""
    for ch in input_str:
        if ch in list_of_vowels:
            vowels += ch
    return vowels
  

# Purpose: This function capitalizes the first letter of every word in a given string
def str_capitalize(input_str: str) -> str:
    cap_str = ""
    isSpace = True
    for ch in input_str:
        if ch == " ":
            isSpace = True
            cap_str += ch
        elif ch >= 'a' and ch <= 'z' and isSpace == True:
            isSpace = False
            ch = chr(ord(ch) - 32)
            cap_str += ch
        else:
            cap_str += ch
    return cap_str


# Purpose: This function returns the ROT-13 encoding for a given string
def str_rotate(input_str: str) -> str:
    cap_string = ""
    for ch in input_str:
        new_ch = ch
        if ch >= 'A' and ch <= 'M':
            new_ch = chr(ord(ch) + 13)
        elif ch > 'M' and ch <= 'Z':
            new_ch = chr(ord(ch) - 13)
        elif ch >= 'a' and ch <= 'm':
            new_ch = chr(ord(ch) + 13)
        elif ch > 'm' and ch <= 'z':
            new_ch = chr(ord(ch) - 13)
        cap_string += new_ch
    return cap_string

# Purpose: This function makes a substring of the given string using given start/end index and increment
def make_substring(input_str: str, start_idx: int, end_idx: int, inc: int) -> str:
    str_sub = ""
    for idx in range(start_idx, end_idx, inc):
        str_sub += input_str[idx]
    return str_sub

# Purpose: This function returns true if the given string is a palindrome, and false if not
def is_palindrome(input_str: str) -> str:
    idx1 = idx2 = 0
    for idx1 in range(0,len(input_str)//2):
        if input_str[idx1] != input_str[len(input_str) - 1 - idx1]:
            return False
    return True

# Purpose: This function counts the instances of a given character in the given string
def count_characters(input_str: str, ch) -> str:
    count = 0
    for idx in range(0,len(input_str)):
        if input_str[idx] == ch:
            count += 1
    if count == 0:
        return -1
    return count