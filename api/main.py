from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')
    html_content = template.render()
    return HTMLResponse(content=html_content)
