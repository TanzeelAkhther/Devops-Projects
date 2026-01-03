from flask import Flask, render_template, request, redirect, url_for
import redis
import os
import socket

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = 6379
redis_db = 0

r = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

@app.route("/", methods=["GET", "POST"])
def vote():
    if request.method == "POST":
        vote = request.form["vote"]
        r.rpush("votes", vote)
        return redirect(url_for("vote"))

    hostname = socket.gethostname()
    return f"""
    <h1>Voting App</h1>
    <form method="POST">
        <button name="vote" value="cats">Cats</button>
        <button name="vote" value="dogs">Dogs</button>
    </form>
    <p>Served from: {hostname}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)