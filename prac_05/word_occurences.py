"""
Word Occurences
Estimate :40mins
Actual Time: 37mins
"""


def main():
    user_text = input("Text: ")
    word_counts = {}
    words = user_text.split()
    words.sort()
    get_word_occurences(word_counts, words)
    print_word_occurences(word_counts)


def print_word_occurences(word_counts):
    """Print word occurences"""
    for word, count in word_counts.items():
        word, width, count = word, 10, count
        print(f"{word:{width}} = {count}")



def get_word_occurences(word_counts, words):
    """Strip the unnecessary parts of a word and count the total of each"""
    for word in words:
        clean_word = word.strip(". , ! ? /")
        word_counts[clean_word] = word_counts.get(clean_word, 0) + 1


main()

