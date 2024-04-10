from fastapi import FastAPI
from pydantic import BaseModel
from app.model import top_roles
from fastapi.middleware.cors import CORSMiddleware

class InputData(BaseModel):
    skills : list[str]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
def first():
    return 'hello'


@app.post("/model/")
def process_data(input: InputData):
    print(input.skills)
    ans = top_roles(input.skills)

    ans_dict = {'top_roles': ans}
    return ans_dict