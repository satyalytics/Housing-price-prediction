from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge, Lasso
from sklearn.ensemble import RandomForestRegresor
from sklearn.ensemble import AdaBoostRegressor, GadientBoostingRegressor
from sklearn.model_selection import train_test_split, cross_val_score, RepeatedKFold

def apply_model(df):
    lin_reg = LinearRegression()
    ridge = Ridge()
    lasso = Lasso()
    rf = RandomForestRegresor()
    mod_dict = {'linear regression':lin_reg, 
                'ridge':ridge, 
                'lasso':lasso,
                'rf':rf}
    X,y = df.drop('median_housing_price', axis=1), df['median_housing_price']
    X_tr, X_te, y_tr, y_te = train_test_split(X,y,test_size=0.2)
    perf_dict = {}
    for name, model in mod_dict:
        model.fit(X_tr,y_tr)
        y_pred = model.predict(X_te)
        perf_dict[name] = {'mse':mean_squared_error(y_test,y_pred),
                           'rmse': root_mean_squared_error(y_test, y_pred),
                           'r2_score': model.score(X_te, y_te)}
    return perf_dict
