def no_dups(s):
    # Your code here
    words = {}
    counter = 0
    for word in s.split(" "):
        if word in words:
            continue
        else:
            counter += 1
            words[word] = counter
    return " ".join(words.keys())


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))