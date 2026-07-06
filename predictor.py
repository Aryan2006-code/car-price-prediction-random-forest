import joblib
import pandas as pd
from config import MODEL_FILE,PIPELINE_FILE

model = joblib.load(MODEL_FILE)
pipeline =joblib.load(PIPELINE_FILE)

def my_prediction(csv_file):
    #lets do inference
    input_data = pd.read_csv(csv_file)
    
    if "Selling_Price" in input_data.columns:
        input_data = input_data.drop("Selling_Price", axis=1)

    transformed_data = pipeline.transform(input_data)
    prediction = model.predict(transformed_data)
    input_data["Selling_Price"] = prediction
    output_path = "output.csv"
    input_data.to_csv(output_path,index=False)
    return output_path
    # print("inference is completed successfully , output is saved to output.csv")