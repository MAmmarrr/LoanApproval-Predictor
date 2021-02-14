from django.shortcuts import render
import joblib
import pandas as pd
from . import utils

reloadModel = joblib.load('main\MLmodel\LoanApprovalPrdictionModel.pk1')
def index(request):
    return render(request, 'main/index.html')

def request_loan(request):
    return render(request, 'main/create.html')

def prediction(request):

    if request.method=='POST':
        temp = {}
        temp['Gender'] = request.POST.get('Gender')
        temp['Married'] = request.POST.get('MartialStatus')
        temp['Dependents'] = (request.POST.get('Dependents'))
        if temp['Dependents'] == '1-5':
            temp['Dependents'] = 1
        else:
            if temp['Dependents'] == '5-10':
                temp['Dependents'] = 6
        if temp['Dependents'] == '10+':
            temp['Dependents'] = 11
        if temp['Dependents'] == 'None':
            temp['Dependents'] = 0
        temp['Education'] = request.POST.get('Education')
        temp['Self_Employeed']=request.POST.get('SelfEmployeed')
        temp['ApplicantIncome']=int(request.POST.get('ApplicantIncome'))
        temp['LoanAmount'] = int(request.POST.get('LoanAmount'))
        temp['Loan_Amount_Term'] = 360.0
        temp['Credit_History'] = 1.0

        temp['Property_Area']=request.POST.get('PropertyArea')
        
        if temp['Gender'] == 'Male':
            temp['Gender'] = 1
        else: 
            temp['Gender'] = 0
        if temp['Married'] == 'Married':
            temp['Married'] = 1
        else: 
            temp['Married'] = 0
        if temp['Education'] == 'Graduate':
            temp['Education'] = 1
        else: 
            temp['Education'] = 0
        if temp['Self_Employeed'] == 'Yes':
            temp['Self_Employeed'] = 1
        else: 
            temp['Self_Employeed'] = 0
        if temp['Property_Area'] == 'Urban':
            temp['Property_Area'] = 0
        elif temp['Property_Area'] == 'Semi-Urban': 
            temp['Property_Area'] = 1
        else:
            temp['Property_Area'] = 2

        x = utils.result(temp)
        to_send = False
        if x == 0:
            to_send = False
        else:
            to_send = True
    testdata = pd.DataFrame({'x':temp}).transpose()
    Approved = reloadModel.predict(testdata)[0]
    context = {'rating': to_send}
    
    return  render(request, 'main/result.html', context)