import gradio as gr
import requests

EXAMPLES = [
    ["project timeline"],
    ["error log"],
    ["meeting notes"],
    ["budget"]
]

def do_search(query):
    try:
        resp = requests.post("http://localhost:5050/search", json={"query": query})
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

ui = gr.Interface(
    fn=do_search,
    inputs="text",
    outputs="json",
    examples=EXAMPLES,
    title="Local File Search Demo",
    description="Searches dummy local files and returns basic context. Ready for future AI expansion."
)

ui.launch()
