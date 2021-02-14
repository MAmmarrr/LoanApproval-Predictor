def result(temp):
    print(temp)
    if temp['Gender'] == 1 and temp['Self_Employeed'] == 0:
        if temp['ApplicantIncome'] < 1000 and temp["Education"] == 0:
            print('1st')
            return 0  
    else:
        if temp["Property_Area"] == 1 and temp['Gender'] == 0:
            if temp['ApplicantIncome'] > 4000 and temp["Education"] == 1:
                print('2nd')
                return 1
    if temp["Property_Area"] == 1 and temp['Gender'] == 0:
        if temp['ApplicantIncome'] < 4000 and temp["Education"] == 0:
            if temp['Married'] == 0:
                print('3rd')
                return 0
    else:
        if temp["Property_Area"] == 1 and temp['Gender'] == 0:
            if temp['LoanAmount'] < 50 and temp["Education"] == 0:
                print('4th')
                return 1
    if temp["Property_Area"] == 1 and temp['Gender'] == 0:
        if temp['ApplicantIncome'] > 4000 and temp["Education"] == 1:
            print('5th')
            return 1
    else:
        if temp['Gender'] == 1:
            if temp['ApplicantIncome'] > 2000 and temp["Education"] == 1:
                print('6th')
                return 1
        else:
            return 0
 
