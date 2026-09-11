from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h1>DevOps HA Web Application</h1>
<h2>CI/CD Deployment Successful 🚀</h2>
<p>Server: {}</p>
""".format(socket.gethostname())
   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
