from fastapi import FastAPI
app=FastAPI()

@app.post("/")
def get_name(text='Sample text'):
    return {'Name':text}