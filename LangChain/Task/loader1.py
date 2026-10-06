# from langchain_community.document_loaders import TextLoader
# loader = TextLoader("students.txt")
# information = loader.load()
# print(information[0].page_content)

from langchain_community.document_loaders import TextLoader
loader = TextLoader("college_rules.txt")
rules = loader.load()
print(rules[0].page_content)