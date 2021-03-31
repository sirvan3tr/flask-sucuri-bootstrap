from flask import Flask, render_template_string
from sucuri import rendering

app = Flask(__name__)

@app.route('/')
def hello_world():
    template = rendering.template('/templates/main.suc',{"x": 1, "y": 3})
    return render_template_string(template)
