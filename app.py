import gradio as gr
from docquery import document, pipeline

qamap = {
    'OnYourSidePlan': {
        "pdf": "OnYourSidePlan_en.pdf",
        "doc": None
    }
}

qapip = pipeline('document-question-answering')

def greet(brochure, question, threshold):
    ans = ""
    
    tag = qamap[brochure]
    doc = tag.get("doc")
    pdf = tag.get("pdf")
    if not doc and pdf:
        doc = document.load_document(pdf)
        tag["doc"] = doc

    if doc:
        lst = qapip(question=question, **doc.context)
        for idx in range(len(lst)):
            if lst[idx]["score"] > float(threshold):
                ans = lst[idx]["answer"]

    return ans

title = "QA Demo"
description = "Demo for end-to-end QA."
article = "<p style='text-align: center'><a href='' target='_blank'>demo</a> | <a href='' target='_blank'>repo</a></p><br><br><br><br><br><br><br><br><br><br><br><br>"
examples =[['OnYourSidePlan',"how many total diseases?", 0.8]]
css = ".image-preview {height: auto !important;}"

iface = gr.Interface(fn=greet, 
                    inputs=[
                        gr.Dropdown(["OnYourSidePlan"], lable="Brochure"),
                        gr.Textbox(lines=1, placeholder="Question", lable="Question"),
                        gr.Slider(0, 1, 0.1, lable="Threshold")
                    ],
                    outputs=gr.Textbox(lines=3, placeholder="Answer", lable="Answer"),
                    title=title,
                    description=description,
                    article=article,
                    examples=examples,
                    css=css)

iface.launch(server_name="0.0.0.0", server_port=8080)
gr.close_all()