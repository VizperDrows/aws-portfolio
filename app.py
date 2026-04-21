from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Noel Vizcaino Portfolio</title>
        <style>
            body {
                font-family: Arial;
                background:#111;
                color:white;
                text-align:center;
                padding:40px;
            }
           .box {
                max-width:700px;
                margin:auto;
                background:#222;
                padding:30px;
                border-radius:10px;
            }
            h1 {color:#00d4ff;}
            a {color:#00d4ff;}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Noel Vizcaino</h1>
            <h2>Aspiring CS UTEP Student / </h2>
            <p>I built and deployed this portfolio using Python and AWS EC2.</p>

            <h3>Projects</h3>
            <p>-AWS Python Website</p>
            <p>-Python Automation Scripts</p>
	    <p>-Python Win-Rate Tracker System Riot Games API</p>
	    <p>-Unity Adventure Mobile Game</p>

            <h3>Contact</h3>
            <p>Email: fvizcainop@miners.utep.edu</p>
        </div>
    </body>
    </html>
    """

@app.route("/api")
def api():
    return {"status": "running", "platform": "AWS EC2"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
