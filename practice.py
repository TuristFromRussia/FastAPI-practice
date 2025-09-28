from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def say_hui():
    return 'huilo'

@app.get("/minus")
def minus_two(a: int, b: int) -> int:
    return a - b

@app.get("/fuck/{print}")
def paint(print: str):
    ret = ''
    ret = print.upper()
    return ret
