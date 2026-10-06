from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("1.LangChain.pdf")
information = loader.load()

# print(information[0].page_content)

for page in information:
    print(page.page_content)
    print("----------------------------------")