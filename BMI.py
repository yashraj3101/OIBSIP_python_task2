
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

height_in_meters = height /100
BMI = weight / (height_in_meters**2)
print(BMI)

if (BMI<16):
    print("you are severely underweigh"), BMI

elif (BMI >= 16 and BMI < 18.5):
    print("you are underwieght"), BMI

elif (BMI >=18.5 and BMI <24):
    print("you are Healthy"),BMI

elif (BMI >= 25 and BMI <30):
    print("you are overweight"),BMI

elif (BMI >=30):
    print("you are obese"),BMI