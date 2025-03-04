


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/topic/<topicid>")
def topic_page(topicid):
    return f"<p>You asked for {topicid}</p>"
