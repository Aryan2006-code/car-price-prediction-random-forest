import gradio as gr
from predictor import my_prediction

demo = gr.Interface(
    fn=my_prediction,
    inputs=gr.File(),
    outputs=gr.File(),
    api_name="predict"
)

demo.launch()