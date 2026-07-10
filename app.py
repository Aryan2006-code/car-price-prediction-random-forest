import gradio as gr
from predictor import my_prediction

demo = gr.Interface(
    fn=my_prediction,
    title ="Car Price Prediction",
    description="""
    **file should contail**
    - Year
    - Present_Price
    - Driven_kms
    - Fuel_Type
    - Selling_type
    - Transmission 
    - Owner""",
    inputs=gr.File(label="upload CSV"),
    outputs=gr.File(label="Download result"),
    api_name="predict"
)

demo.launch()