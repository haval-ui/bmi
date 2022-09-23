weight=int(input("enter you weight (kg) :"))
height=float(input("enter your height (m) : "))
bmi=round(weight//height**2)
print(f"your bmi is{bmi}")
if bmi < 18.5 :
    print("you are underweight, you should eat more ")
elif bmi <25:
    print("you have a normal weight, keep it up champ!! ")
elif  bmi <30:
    print(" you are over weight , be more care full  about what you eat  ")
elif bmi <35:
    print("you are obese, you have to start a diet or you will be in trouble ")
else:
    print("you are clinically obese, you should see an doctor ")