def anagram_check(str1, str2):
    if(sorted(str1) == sorted(str2)):
        print("The string is anagram")
    else:
        print("The string is not anagram")


anagram_check("silent", "listen")