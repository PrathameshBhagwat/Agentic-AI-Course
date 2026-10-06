from langchain_text_splitters import RecursiveCharacterTextSplitter
text = """
Python is an extremely popular, simple, and powerful programming language.It is mainly used for web development, data science, artificial intelligence (AI), and automation. Python's syntax is very easy to read, making it very easy for beginners to learn this language.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 20
)

chunks = splitter.split_text(text)

for chunk in chunks:
    print(chunk)
    print("-----------------------------------------")