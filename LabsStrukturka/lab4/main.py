def count_word_frequencies(text):
    text = text.lower()
    words = text.split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def print_results(frequency):
    for word, count in frequency.items():
        if count > 1:
            print(f"{word} -> {count}")


text = input("Введите текст: ")
frequencies = count_word_frequencies(text)
print_results(frequencies)