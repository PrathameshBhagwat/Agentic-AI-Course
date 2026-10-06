from langchain_community.document_loaders import CSVLoader

# loader = CSVLoader("students.csv")
loader = CSVLoader("products.csv")
documents = loader.load()

# for i in documents:
#     print(i.page_content)

for i in documents:
    print(i.page_content)