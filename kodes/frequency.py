def count_frequency(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char] = 1
        return frequency

text = "hello world"
print(count_frequency(text))
print(len(text))

for char, freq in count_frequency(frequency).items():
    print(f"Character: {char}, Frequency: {freq}")
    