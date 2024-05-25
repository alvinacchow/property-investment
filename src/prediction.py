import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


# to edit test.csv and train.csv 

# def extract_selected_columns(file_path, output_file):
#     # Define the columns to extract
#     columns_to_extract = [
#         'Id', 'LotArea', 'BldgType', 'YearBuilt', 'Heating', 'GrLivArea', 'BedroomAbvGr',
#         'FullBath', 'GarageCars', 'PoolArea', 'MoSold', 'YrSold'
#     ]
    
#     data = pd.read_csv(file_path)
#     filtered_data = data[columns_to_extract]
#     filtered_data.to_csv(output_file, index=False)

# # Example usage
# file_path = 'ai-model/original-test.csv'
# output_file = 'ai-model/test.csv'
# filtered_data = extract_selected_columns(file_path, output_file)


#################################################################
######################## TRAINING MODEL #########################
#################################################################

# read data
train = pd.read_csv('ai-model/city-listings.csv', index_col='Id')
test = pd.read_csv('ai-model/entry.csv', index_col='Id')
 
X = train.dropna(axis=0, subset=['SalePrice']) # X = table with salePrice    

# separate target from predictors
y = X.SalePrice
X.drop(['SalePrice'], axis=1, inplace=True)

X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y,
    train_size=0.8,
    test_size=0.2,
    random_state=0)

low_cardinality_cols = [cname for cname in X_train_full.columns 
                        if X_train_full[cname].nunique() < 10 and 
                        X_train_full[cname].dtype == "object"]

numeric_cols = [cname for cname in X_train_full.columns
                if X_train_full[cname].dtype in ['int64', 'float64']]

# keep selected columns only
my_cols = low_cardinality_cols + numeric_cols

X_train = X_train_full[my_cols].copy()
X_valid = X_valid_full[my_cols].copy()

# for test data also
X_test = test[my_cols].copy()

# one-hot encode the data
X_train = pd.get_dummies(X_train)
X_valid = pd.get_dummies(X_valid)
X_test = pd.get_dummies(X_test)

X_train, X_valid = X_train.align(X_valid, join='left', axis=1)
X_train, X_test = X_train.align(X_test, join='left', axis=1)

xgb =  XGBRegressor(n_estimators=1000,
                    learning_rate=0.05)

xgb.fit(X_train, y_train)
y_pred = xgb.predict(X_valid)
mae = mean_absolute_error(y_pred, y_valid)
# print("Mean Absolute Error:" , mae)

prediction = xgb.predict(X_test)
output = pd.DataFrame({'Id': X_test.index,
                       'SalePrice': prediction})
output.to_csv('ai-model/prediction.csv', index=False)
output.head()
