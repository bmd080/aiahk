from docquery import document, pipeline
p = pipeline('document-question-answering')

b = input("Brochure: ")

doc = document.load_document(b)
while True:
    q = input("Question: ")
    # [{'score': 0.9996325373649597, 'answer': '58', 'word_ids': [46], 'page': 2}]
    lst = p(question=q, **doc.context)
    for idx in range(len(lst)):
        ans = lst[idx]
        if ans["score"] > 0.8:
            print("Answer:", ans["answer"])