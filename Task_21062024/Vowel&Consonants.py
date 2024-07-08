def vowel_consonants(C):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

    vowel_count = 0
    consonants_count = 0

    for char in C:
        if char in vowels:
            vowel_count += 1
        else:
            consonants_count += 1

    return vowel_count, consonants_count

vowels, consonants = vowel_consonants("I am learning Automation with Python")
print(f"Vowels Count: {vowels} , Consonant Count: {consonants}")




