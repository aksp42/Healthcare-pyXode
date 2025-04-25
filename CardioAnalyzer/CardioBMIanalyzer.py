def cal_bmi(weight,height):
    """Calculate BMI and return category"""
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal Weight"
    elif 25 <= bmi <= 29.9 :
        category = "Overweight"
    else :
        category = "Obese - High Risk!"
        
    return bmi , category

def cardio_check():
    """Heart Disease Risk Checker"""
    print("CARDIO-BMI-ANALYZER")
    print("Heart Disease & BMI Risk Checker")
    #User Inputs
    age = int(input("Enter your age : "))
    weight = float(input("Enter your weight in Kg : "))
    height = float(input("Enter your height in meters : "))
    blood_pressure = input("Do you have high blood pressure ? (yes/no) : ").strip().lower()
    Cholesterol = input("Do you have high cholesterol ? (yes/no) : ").strip().lower()
    smoking = input("Do you smoke ? (yes/no) : ").strip().lower()
    physical_activity = input("Do you exrecise reguraly ? (yes/no) : ").strip().lower()
    diabetes = input("Do you have diabetes ? (yes/no) : ").strip().lower()
    # Calculate BMI
    bmi , bmi_category = cal_bmi(weight , height)
    
    # Risk Score Counting
    risk_score = 0
    
    
    if age > 50:
        risk_score += 2
    if blood_pressure == "yes":
        risk_score += 2
    if Cholesterol == "yes":
        risk_score += 2 
    if smoking == "yes":
        risk_score += 3
    if physical_activity == "no":
        risk_score += 1
    if diabetes == "yes":
        risk_score += 2
    if bmi > 30:
        risk_score += 3
        
    # Heart Disease Risk Classification
        
    if risk_score <= 2:
        risk_level = "Low Risk"    
    elif risk_score <= 5:
        risk_level = "Moderate Risk"
    else :
        risk_level = "High Risk X Consult a Doctor as soon as Possible!"
    
    if bmi_category == "Normal Weight":
        result = "Positive"
    else :
        result = "Negative"    
    print("Results : ",result)
    print("***Heart Disease Risk : %s***" % risk_level)
    print("BMI : %.2f & Category : %s"%(bmi,bmi_category))
    
cardio_check()
