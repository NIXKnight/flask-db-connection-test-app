import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def check_db_connection():
    try:
        # Connect to the database using environment variables
        conn = psycopg2.connect(
            host=os.environ.get("DATABASE_HOST"),
            port=os.environ.get("DATABASE_PORT"),
            user=os.environ.get("DATABASE_USER"),
            password=os.environ.get("DATABASE_PASSWORD"),
            dbname=os.environ.get("DATABASE_NAME")
        )
        # Return a successful response
        return jsonify(message="Connection to database successful"), 200
    except:
        # Return a failure response
        return jsonify(message="Error connecting to database"), 500

if __name__ == '__main__':
    app.run()
