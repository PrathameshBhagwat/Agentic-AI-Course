from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://evlearningworld.com")

document = loader.load()

# print(document[0].page_content)

print(document[0])