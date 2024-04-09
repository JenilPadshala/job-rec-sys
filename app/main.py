from fastapi import FastAPI
from pydantic import BaseModel
from app.model import top_roles

class InputData(BaseModel):
    res : list[str]


app = FastAPI()

@app.get('/')
def first():
    return 'hello'


@app.post("/model/")
def process_data(input: InputData):
    print(input.res)
    ans = top_roles(input.res)

    ans_dict = {'top_roles': ans}
    return ans_dict