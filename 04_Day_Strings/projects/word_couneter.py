def word_count():
    text = input('Enter text to count word: ')

    # Split the text into words and count the number of words
    words = text.split()
    word_counts = len(words)

    # Print the result
    print('Word count:', word_counts)


word_count()


# This is Advance after Dictionary lesson
def letter_count():
    text = input('Enter text to count letter: ')

    # Create an empty dictionary to store letter counts
    letter_counts = {}

    # Loop through each character in the text
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Convert the letter to lowercase
            char = char.lower()
            # Increment the count for the letter
            letter_counts[char] = letter_counts.get(char, 0) + 1

    # Print the result
    for letter, count in letter_counts.items():
        print(letter, count)


letter_count()


# This is Advance after List lesson
def vowel_count():
    text = input('Enter text to count Vowel: ')

    # Create a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Count the number of vowels in the text
    vowel_counts = 0
    for char in text:
        if char.lower() in vowels:
            vowel_counts += 1

    # Print the result
    print('Vowel count:', vowel_counts)


vowel_count()
