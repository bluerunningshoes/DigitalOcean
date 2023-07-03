from flask import Flask
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Welcome to S14A2023</p>"

@app.route("/datetime")
def get_datetime():
    # Define time zones
    utc = pytz.timezone('UTC')
    cst = pytz.timezone('US/Central')
    est = pytz.timezone('US/Eastern')

    # Get current UTC time
    current_utc_time = datetime.now(tz=utc)

    # Convert to CST
    cst_time = current_utc_time.astimezone(cst)

    # Convert to EST
    est_time = current_utc_time.astimezone(est)

    # Assign what we're printing to a variable (since print doesn't work with Flask: you have to return something)
    output = "Current UTC time: {}<br>Where the server is: CST time: {}<br>Where Emilia is: EST time: {}".format(
        current_utc_time, cst_time, est_time)

    return output

if __name__ == "__main__":
    app.run()

