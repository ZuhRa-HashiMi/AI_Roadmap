with open("sample.txt", "w") as file:
    file.write("python is fun\n")
    file.write("python is usful for AI\n")
    file.write("AI use Python\n")
    
    
with open("sample.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()
    line_count = len(lines)
    words = content.split()
    word_count = len(words)
print(f"Total lines: {line_count}")
print(f"Total words: {word_count}")