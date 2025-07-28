import os
'''ith open("sample.txt","r") as file:
    data =  file.read()
    print(data)
with open("sample.txt","w") as file:
    file.write("add new things on it !")

os.remove("example.txt")
'''
def check_file_empty(filepath):
    if not os.path.exists (filepath):
        print("this file does not exist !")
    elif os.path.getsize(filepath) == 0:
        print("this file is empty !")
    else:
        print("this file is not empty!")
print(check_file_empty("sample.txt"))
