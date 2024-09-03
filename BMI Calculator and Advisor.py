weight = int(input("Enter your weight in kg="))
print("Enter your height:")
h_ft = int(input("Feet= "))
h_inch = int(input("Inches= "))
print("-" * 50)

if weight <= 0 or h_ft <= 0 and h_inch <= 0:
    print("Weight and height must be positive numbers.")
else:
    #Conversion of height from feet and inches to meter
    h_m = (h_ft*0.3048)+(h_inch*0.0254)

    #Calculate BMI
    BMI= weight/(h_m * h_m)
    print("BMI in kg/m^2 = ",BMI)
    print("-" * 50)

    #BMI ranges
    if BMI<18.5:
        print("Your BMI indicates that you are in the Underweight range.")
        print("-" * 50)
        #Goal and Advise
        print("Goal: Increase calorie intake to gain weight.")
        print("Advice:")
        print("Focus on nutrient-dense foods like whole grains, lean proteins, fruits, and vegetables. \nConsult a dietitian for a personalized meal plan.\nIncorporate regular strength training to build muscle mass.")
    elif BMI>= 18.5 and BMI<= 24.9:
        print("Your BMI indicates that you are in the Healthy weight range.")
        print("-" * 50)
        #Goal and Advise
        print("Goal: Maintain a healthy weight.")
        print("Advice:")
        print("Continue a balanced diet with a variety of foods. \nAim for regular physical activity, including both cardio and strength training. \nManage stress through techniques like meditation or yoga.")
    elif BMI>= 25 and BMI<= 29.9:
        print("Your BMI indicates that you are in the Overweight range.")
        print("-" * 50)
        #Goal and Advise
        print("Goal: Lose weight gradually.")
        print("Advice:")
        print("Reduce calorie intake and increase physical activity. \nFocus on whole, unprocessed foods and portion control. \nConsult a dietitian for a personalized meal plan.")
    elif BMI>= 30 and BMI<= 34.9:
        print("Your BMI indicates that you are in the obese weight range.")
        print("-" * 50)
        #Goal and Advise
        print("Goal: Lose weight and improve overall health.")
        print("Advice:")
        print("Create a personalized weight loss plan with a healthcare professional or registered dietitian. \nIncorporate a combination of diet and exercise. \nAddress any underlying health conditions that may be contributing to weight gain.")
    else:
        print("Your BMI indicates that you are in the Morbid obesity weight range.")
        print("-" * 50)
        #Goal and Advise
        print("Goal: Lose weight and improve overall health.")
        print("Advice:")
        print("Create a personalized weight loss plan with a healthcare professional or registered dietitian. \nIncorporate a combination of diet and exercise. \nAddress any underlying health conditions that may be contributing to weight gain.")
    