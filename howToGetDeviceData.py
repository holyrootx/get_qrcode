from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.user_agent
    device = user_agent.platform
    browser = user_agent.browser
    version = user_agent.version
    language = request.headers.get('Accept-Language')

    return f"Device: {device}<br>Browser: {browser} {version}<br>Language: {language}"


app.run(debug=True)