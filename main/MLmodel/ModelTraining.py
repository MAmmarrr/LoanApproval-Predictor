import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
import joblib

df_origional = pd.read_csv(r'LoanApprovalPredictor\main\MLmodel\LoanPredictionTrain.csv')
df = df_origional



knn = KNeighborsClassifier()
nb = GaussianNB()
classifierLR = LogisticRegression()
SVectorMachine = SVC()
DecisionTree = DecisionTreeClassifier()

df = df.replace([np.inf, -np.inf], np.nan).dropna(axis=0)
df['Dependents'] = df['Dependents'].map(lambda x: x.rstrip('$+'))
df.loc[df["Gender"] == "Female", "Gender"] = 0
df.loc[df["Gender"] == "Male", "Gender"] = 1
df.loc[df["Married"] == "No", "Married"] = 0
df.loc[df["Married"] == "Yes", "Married"] = 1
df.loc[df["Property_Area"] == "Urban", "Property_Area"] = 0
df.loc[df["Property_Area"] == "Rural", "Property_Area"] = 2
df.loc[df["Property_Area"] == "Semiurban", "Property_Area"] = 1
df.loc[df["Self_Employed"] == "No", "Self_Employed"] = 0
df.loc[df["Self_Employed"] == "Yes", "Self_Employed"] = 1
df.loc[df["Loan_Status"] == "Y", "Loan_Status"] = 1
df.loc[df["Loan_Status"] == "N", "Loan_Status"] = 0
df.loc[df["Education"] == "Graduate", "Education"] = 1
df.loc[df["Education"] == "Not Graduate", "Education"] = 0

X = df.drop(['Loan_ID','Loan_Status','CoapplicantIncome'], axis=1)
y = df['Loan_Status']

y = y.astype('int')
xtrain, xtest, ytrain, ytest = train_test_split(
    X, y, test_size=0.2, random_state= 12
)

nb.fit(xtrain, ytrain)

joblib.dump(nb,'LoanApprovalPrdictionModel.pk1')