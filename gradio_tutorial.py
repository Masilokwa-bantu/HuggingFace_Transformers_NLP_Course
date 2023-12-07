import gradio as gr
from transformers import pipeline

if __name__ == "__main__":
    def greet(name):
        return "Hello " + name

    # text generation model
    model = pipeline("text-generation")

    def predict(prompt):
        completion = model(prompt)[0]["generated_text"]
        return completion

    def summarizer(prompt):
        model = pipeline('summarization', model='sshleifer/distilbart-cnn-12-6')
        summary = model(prompt)[0]['summary_text']
        return summary

    # Initializing the Textbox class
    textbox = gr.Textbox(label="Type your name here: ", placeholder="Ba Phiri", lines=2)

    demo = gr.Interface(fn=summarizer, inputs="text", outputs="text")

    demo.launch()