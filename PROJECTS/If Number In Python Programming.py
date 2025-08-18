List_1 = ["London",18,"Birmingham",33,"Oxford","John",77,9823,"Jane",(77,313),(39)]
for elements in List_1:
    try:
        elements = int(elements)
        print(elements)
    except:
        pass