import pandas as pd 
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression as lr 
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import cross_val_score

# random / fake data 
data = {
    # 'time': ['01-08-2024', '02-08-2024', '03-08-2024', '04-08-2024',...],
    'sustainableDevelopment': np.random.randint(100, 10000, 50),
    'greenBusiness': np.random.randint(100, 10000, 50),
    'localSpending': np.random.randint(100, 10000, 50),
    'wasteManagement': np.random.randint(100, 10000, 50),
    'transportPractices': np.random.randint(100, 10000, 50),
    'carbonFootprint': np.random.randint(100, 10000, 50),
    'energyEfficiency': np.random.randint(100, 10000, 50),
    'rewardSD' : np.random.randint(1, 30, 50),
    'rewardGB': np.random.randint(1, 30, 50),
    'rewardLS': np.random.randint(1, 30, 50),
    'rewardWM': np.random.randint(1, 30, 50),
    'rewardTP': np.random.randint(1, 30, 50),
    'rewardCF': np.random.randint(1, 30, 50),
    'rewardEE': np.random.randint(1, 30, 50)
}

# creating a dataframe
df = pd.DataFrame(
    data = data
)

# creating our data 
X = df[['sust¡¡ainableDevelopment','greenBusiness','localSpending','wasteManagement','transportPractices','carbonFootprint','energyEfficiency']]
y = df[['rewardSD','rewardGB','rewardLS','rewardWM','rewardTP','rewardCF','rewardEE']]

# scaling our data 
scaler = MinMaxScaler()
pop = scaler.fit_transform(X)
X = pop

# scaling our results
test = MinMaxScaler()
test.fit_transform(y)

# train, test and validation split
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# linear regression model : future is reinforced learning
model = lr()
model.fit(X_train, y_train)

# predicting the reward points
pred = model.predict(X_val)

# metrics
cv = cross_val_score(
    model, 
    X, 
    y,
    cv = 5 
)

cv *= -1

final = ['sustainableDevelopment','greenBusiness','localSpending','wasteManagement','transportPractices','carbonFootprint','energyEfficiency']

# for k in range(len(cv)):
#     print(f"Reward point awarded for {final[k]}: ",int(cv[k] * test.data_range_[k] + test.data_min_[k]))

# calculating RP for nth case
case = 2

print(f"Reward point for {final[k]} : {int(cv[k] * test.data_range_[k] + test.data_min_[k])}")
