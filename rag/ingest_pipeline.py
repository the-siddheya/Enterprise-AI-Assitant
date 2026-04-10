import pandas as pd

def load_documents(path):
    if path.endswith('.pdf'):
        loader = PyPDFLoader(path)
    
    elif path.endswith('.txt'):
        loader = TextLoader(path)
    
    elif path.endswith('.docx'):
        loader = DocxLoader(path)
    
    return loader.load()

def ingest_pending_documents():
    df = pd.read_csv('documents.csv')
    pending_docs = df[[df['status'] == 'pending']]
    for index, row in pending_docs.iterrows():
        file_name = row['file_name']
        df.at[index, 'status'] = 'ingested'
    
