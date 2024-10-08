from flask import Flask, render_template
from google.cloud import firestore

app = Flask(__name__)

# Initialize Firestore
db = firestore.Client()

@app.route('/')
def index():
    try:
        # Query Firestore data
        docs = db.collection('responses').stream()
        responses = [doc.to_dict() for doc in docs]
        
        # Sort responses by timestamp; most recent games appended to top
        responses.sort(key=lambda x: x['timestamp'], reverse=True)
        
        return render_template('index.html', responses=responses)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
