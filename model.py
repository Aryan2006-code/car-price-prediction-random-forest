import os
import joblib
import numpy as np
import pandas as pd 
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import OneHotEncoder 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error ,r2_score

MODEL_FILE ="model_pkl"
PIPELINE_FILE = "pipeline_pkl"

def build_pipeline(num_attribute , low_cat_attribute ):

    # for  normal categorical columns 
    cat_pipeline = Pipeline([
        ("onehot" ,OneHotEncoder(handle_unknown="ignore"))
    ])

    

    # combine all pipelines
    full_pipeline = ColumnTransformer([
        ("num", "passthrough", num_attribute),
        ("l_cat",cat_pipeline,low_cat_attribute)])

    return full_pipeline


def train_model():
    car_data = pd.read_csv("data/car data.csv")
    car_data= car_data.drop("Car_Name",axis=1)


    # creating Stratified test set
    car_data["P_price_cat"]= pd.cut(car_data["Present_Price"],bins=[0.0,1.5,3.0,4.5,6.0,np.inf],labels=[1,2,3,4,5])
    splitt= StratifiedShuffleSplit(n_splits=1, test_size =0.2 , random_state=42)

    for train_idx , test_idx in splitt.split(car_data,car_data["P_price_cat"]):
        car_data.iloc[test_idx].drop("P_price_cat",axis=1).to_csv("input.csv", index=False)
        car_data = car_data.iloc[train_idx].drop("P_price_cat",axis=1)

    car_label = car_data["Selling_Price"].copy() # this is what our model will try to predict
    car_features = car_data.drop("Selling_Price",axis=1)

    num_attributes =car_features.drop(["Fuel_Type","Selling_type","Transmission"],axis =1).columns.tolist()
    l_cat_attributes = ["Fuel_Type","Selling_type","Transmission"]
        

    pipeline = build_pipeline(num_attributes,l_cat_attributes)
    car_prepared = pipeline.fit_transform(car_features,car_label)

    model = RandomForestRegressor()
    model.fit(car_prepared,car_label)

    joblib.dump(model , MODEL_FILE)
    joblib.dump(pipeline,PIPELINE_FILE)

    print("model trained")


if __name__=="__main__":
    train_model()