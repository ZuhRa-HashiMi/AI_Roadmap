def count_words(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        lines = content.splitlines()
        words = content.split()

        word_frequency = {}

        for word in words:
            word = word.lower()

            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        return {
            "line_count": len(lines),
            "word_count": len(words),
            "word_frequency": word_frequency
        }

    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        return None
    
result = count_words("sample.txt")
if result is not None:
    print(f"Total lines: {result['line_count']}")
    print(f"Total words: {result['word_count']}")
    print(result["word_frequency"])
