high_income =True
good_credit= True
student = False

if high_income  and good_credit:
    print("Eligible")
else:
    print("Not Eligible")


if not student:
    print("Eligible")
else:
    print("Not Eligible")



if (high_income  or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")