from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def get_current_datetime():
    current_datetime = datetime.now()
    return (f' Текущая дата и время: {current_datetime.strftime("%d-%m-%Y %H:%M:%S")}')

if __name__ == "__main__":
    app.run()