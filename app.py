from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker boss! you're great bosses dddd blames me always and always and godfather and godmother"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
