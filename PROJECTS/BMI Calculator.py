# BMI Calculator:-

Height=float(input("Please Enter Your Height In Meter:"))
Weight=int(input("Please Enter Your Weight:"))
Gender=str(input("Please Enter Your Gender:"))
BMI=Weight/(Height**2)

print("BMI:",BMI)

BMI=float(input("Please Enter Your BMI:"))
if BMI<18.5:
    print("Under Weight!",('So Sad'),"Your Body Mass Is Low")
elif 18.5<BMI<=24.9:
    print("Congratulation! Your Weight Is Normal")
elif 25<BMI<=29.9:
    print("Good!","Your Weight Is Over Weight")
elif 30<BMI<=34.9:
    print("Sad!","Your Weight Is Obese")
elif BMI>35.0:
    print("SO Sad!","Your Weight Is Over Weight")
else :
    print("Have Your Nice Day!")
