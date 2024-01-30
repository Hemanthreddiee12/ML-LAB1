def count_vowels_and_consonants(input_string):
    vowel_count = 0
    consonant_count = 0
    vowels = set("aeiouAEIOU")
    for char in input_string:
        if char.isalpha():
         vowel_count += 1 if char in vowels else 0
         consonant_count += 1 if char not in vowels else 0
    return vowel_count, consonant_count

def get_user_input():
    return input("Enter a string: ")

def display_results(vowel_count, consonant_count):
    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")

def main():
    input_string = get_user_input()
    vowel_count, consonant_count = count_vowels_and_consonants(input_string)
    display_results(vowel_count, consonant_count)

if __name__ == "__main__":
    main()
