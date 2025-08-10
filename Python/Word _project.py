# Word Statistics Program - Level One Version

def count_characters(text):
    return len(text)

def count_words(text):
    return len(text.split())

def word_frequencies(text):
    freq = {}
    for word in text.split():
        word_lower = word.lower()
        if word_lower in freq:
            freq[word_lower] += 1
        else:
            freq[word_lower] = 1
    return freq

def reverse_text(text):
    return text[::-1]

def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()

# Main program
text = input("Enter a text: ").strip()

while True:
    print("\n--- MENU ---")
    print("1 - Count characters")
    print("2 - Count words")
    print("3 - Show word frequency")
    print("4 - Reverse the text")
    print("5 - Convert to UPPERCASE")
    print("6 - Convert to lowercase")
    print("7 - Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print("Number of characters:", count_characters(text))
    elif choice == "2":
        print("Number of words:", count_words(text))
    elif choice == "3":
        print("Word frequencies:")
        for word, count in word_frequencies(text).items():
            print(f"{word}: {count}")
    elif choice == "4":
        print("Reversed text:", reverse_text(text))
    elif choice == "5":
        print("Uppercase text:", to_uppercase(text))
    elif choice == "6":
        print("Lowercase text:", to_lowercase(text))
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
