def find_replace(filepath, new_word, old_word):
    file = open(filepath, 'r')
    content = file.read()
    file.close()

    file = open(filepath, 'w')
    file.write(content)
    file.close()

    print(f"here {old_word} and here is {new_word}")
filepath = "sample.txt"
new_word = 'hello'
old_word = 'hii'