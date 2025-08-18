def characterCounts(s):
    counts = {}

    for ch in s:
        if ch in counts:
            counts[ch] = counts[ch]+1
        else:
            counts[ch]= 1
            return counts
        
def main():
    S1 = input("Enter the first string: ")
    S2 = input("Enter the second string: ")

    counts1 = characterCounts(S1)
    counts2 = characterCounts(S2)

    if counts1 == counts2:
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams.")

main()