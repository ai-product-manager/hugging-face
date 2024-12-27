from transformers import pipeline
import gradio as gr


model = pipeline(
    "summarization",
)

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

with gr.Blocks() as demo:
    textbox = gr.Textbox(
        placeholder="Enter text block to summarize",
        lines=4,
        label="Your text here"
    )
    output = gr.Textbox(label="Summary")
    button = gr.Button("Summarize")

    button.click(
        fn=predict,
        inputs=textbox,
        outputs=output
    )

demo.launch()