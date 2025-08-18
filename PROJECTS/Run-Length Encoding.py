def encode(data):
    if len(data) == 0:
        return[]
    index = 1
    while index < len(data) and data[index] == data[index - 1]:
        index = index + 1 
    current = [data[0], index]
    return current + encode(data[index:len(data)])

def main():
    s = input("Enter some characters: ")
    print("When those character are run-length encoded, the result is: ",encode(s))

main()