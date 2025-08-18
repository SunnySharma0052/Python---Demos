# EXAMPLE:E-MAIL GENERATOR:-


user=input("Please Enter Your Name:")
user_edit=user.replace(" ","")
company_name=input("Please Enter Your Company Name:")
company_edit=company_name.replace(" ","")
email_address=user_edit+"@"+company_edit+".com"
email_edit=email_address.lower()
print("E-mail Address:",email_edit)
