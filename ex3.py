def count_words(input_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            words = content.split(" ")
            small_words = [word for word in words if len(word) < 3]
            large_words = [word for word in words if len(word) >= 3]
            with open('small_words.txt', 'w') as small_file:
                small_file.write('\n'.join(small_words))
            with open('large_words.txt', 'w') as large_file:
                large_file.write('\n'.join(large_words))
            total_unique = len(set(words))
            return total_unique
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

def ex3():
    total_words = count_words("words.txt")
    print(f"Total words: {total_words}.")

ex3()