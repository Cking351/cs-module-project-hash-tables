def word_count(s):
    # Your code here
    if len(s) == 0:
        return {}

    counts = {}
    bad_chars = ["\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]
    bad_chars2 = ["\t", "\r", "\n"]

    for char in bad_chars:
        s = s.replace(char, " ")
    for char in bad_chars2:
        s = s.replace(char, " ")

    words = s.split(" ")

    for word in words:
        lowered_word = word.lower()
        if word in counts:
            word = lowered_word
            counts[word] += 1
        elif word == '':
            continue
        else:
            word = lowered_word
            counts[word] = 1

    return counts


if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    # print(word_count('":;,.-+=/\\|[]{}()*^&'))
    # print(word_count('a a\ra\na\ta \t\r\n'))
    print(word_count("this, this, This"))
