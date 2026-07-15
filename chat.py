import gradio as gr
import requests

API_URL = "https://nlp-backend-4.onrender.com/explain"


def explain_code(code):
    if not code.strip():
        return "Please enter Python code."

    try:
        response = requests.post(
            API_URL,
            data=code,
            headers={"Content-Type": "text/plain"}
        )

        if response.status_code == 200:
            return response.json()["explanation"]
        else:
            return response.text

    except Exception as e:
        return str(e)


with gr.Blocks(title="Python Code Explainer") as demo:

    gr.Markdown("# 🐍 Python Code Explainer")
    gr.Markdown("Paste your Python code below and click *Explain*.")

    with gr.Row():

        with gr.Column():

            code = gr.Textbox(
                label="Python Code",
                placeholder="Paste your Python code here...",
                lines=20
            )

            with gr.Row():
                clear = gr.Button("Clear")
                submit = gr.Button("Explain")

        with gr.Column():

            output = gr.Textbox(
                label="Explanation",
                lines=20
            )

    submit.click(
        fn=explain_code,
        inputs=code,
        outputs=output
    )

    clear.click(
        lambda: ("", ""),
        outputs=[code, output]
    )
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
