# import the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# load the data
data = pd.read_csv("Customer_Churn_Prediction.csv")
print(data)

# check for the null data
print(data.isnull().sum())

print("Duplicate values : ")
print(data.duplicated().sum())

# print the information about the data
print(data.info())

# print the unique values in all the columns
print("For unique values : ")
print("\n")
print("For gender : ")
print(data['gender'].unique())

print("For Partner : ")
print(data['Partner'].unique())

print("For Dependents : ")
print(data['Dependents'].unique())

print("For PhoneService : ")
print(data['PhoneService'].unique())

print("For MultipleLines : ")
print(data['MultipleLines'].unique())

print("For InternetService : ")
print(data['InternetService'].unique())

print("For OnlineSecurity : ")
print(data['OnlineSecurity'].unique())

print("For OnlineBackup : ")
print(data['OnlineBackup'].unique())

print("For DeviceProtection : ")
print(data['DeviceProtection'].unique())

print("For TechSupport : ")
print(data['TechSupport'].unique())

print("For StreamingTV : ")
print(data['StreamingTV'].unique())

print("For StreamingMovies : ")
print(data['StreamingMovies'].unique())

print("For Contract : ")
print(data['Contract'].unique())

print("For PaperlessBilling : ")
print(data['PaperlessBilling'].unique())

print("For PaymentMethod : ")
print(data['PaymentMethod'].unique())

# different plots

plt.figure(figsize = (6, 4))
sns.countplot(x = "Churn", data = data)
plt.title("Churn Count")
plt.xlabel("Churn")
plt.ylabel("Count")
plt.show()

#Distribution plots for numerical features
plt.figure(figsize = (10, 5))

# Distribution for tenure
plt.subplot(1, 2, 1)
sns.histplot(data['tenure'], kde = True, bins = 30)
plt.title("Distribution of Tenure")

# Distribution for MonthlyCharges
plt.subplot(1, 2, 2)
sns.histplot("data['MonthlyCharges'], kde = True", bins = 30)
plt.title("Distribution of MonthlyCharges")

plt.tight_layout()
plt.show()

'''
# Box Plots to Compare Distributions by Churn

plt.figure(figsize = (10, 5))

#Tenure by Churn
plt.subplot(1, 3, 1)
sns.boxplot(x = 'Churn', y = 'tenure', data = data)
plt.title("Tenure by Churn")

plt.subplot(1, 3, 2)
sns.boxplot(x = 'Churn', y = "MonthlyCharges", data = data)
plt.title("Monthly Charges by Churn")

plt.subplot(1, 3, 3)
sns.boxplot(x = 'Churn', y = 'TotalCharges', data = data)
plt.title("Total Charges by Churn")

plt.tight_layout()
plt.show()

'''

# Heatmap for correlation Analysis
plt.figure(figsize = (8, 6))

# correlation matrix for numerical columns
corr = data[['tenure', 'MonthlyCharges']].corr()
custom_cmap = sns.dark_palette("purple", as_cmap = True)
sns.heatmap(corr, annot = True, cmap = custom_cmap, fmt = ".2f")
plt.title("Correlation Matrix of numerical features")
plt.show()

#Categorical Feature Analysis : count by churn

categorical_cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']

plt.figure(figsize = (20, 30))
for i, col in enumerate(categorical_cols):
	plt.subplot(8, 2, i+1)
	sns.countplot(x = col, hue = 'Churn', data = data)
	plt.title(f'{col} Distribution by Churn')
	plt.xlabel(col)
	plt.ylabel('Count')
	plt.tight_layout()
plt.show()








