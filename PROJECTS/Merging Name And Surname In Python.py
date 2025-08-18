#Merging Name And Surname In Python
 
Name = ["Robin","William","John","Oliver","Mark","James","michael","Yoko","Jane"]
Surname = ["Hood","Shakespeare","Lenmon","Twist","Twain","Armstrong","Dean","Jackson","Ono","Doe"]
Famous = list(zip(Name,Surname))
Famous.sort()

for name,surname in Famous:
    print(name,surname)