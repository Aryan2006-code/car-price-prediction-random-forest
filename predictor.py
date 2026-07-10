import joblib
import pandas as pd
import gradio as gr
from config import MODEL_FILE,PIPELINE_FILE

model = joblib.load(MODEL_FILE)
pipeline =joblib.load(PIPELINE_FILE)

def file_check(csv):
    # raise error if csv empty
    if csv.empty:
        raise gr.Error("The uploaded CSV is empty.")

    #raise error if column empty
    required_columns = [
    "Year",
    "Present_Price",
    "Driven_kms",
    "Fuel_Type",
    "Selling_type",
    "Transmission",
    "Owner"
    ]

    missing = [col for col in required_columns if col not in csv.columns]

    if missing:
        raise gr.Error(
            f"Missing columns: {', '.join(missing)}"
        )

def my_prediction(csv_file):
    #lets do inference
    gr.Info("⏳ Processing started...")

    input_data = pd.read_csv(csv_file)
    
    if "Selling_Price" in input_data.columns:
        input_data = input_data.drop("Selling_Price", axis=1)

    file_check(input_data)

    transformed_data = pipeline.transform(input_data)
    prediction = model.predict(transformed_data)
    input_data["Selling_Price"] = prediction
    output_path = "output.csv"
    input_data.to_csv(output_path,index=False)
    gr.Info("✅ Prediction completed!")
    return output_path
    # print("inference is completed successfully , output is saved to output.csv")