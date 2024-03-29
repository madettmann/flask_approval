from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/approve")
def approve():
    return render_template("approvals.html")

@app.route("/approved")
def approve_doc():
    # Send invoice in email and delete from invoice folder
    # If more invoices to approve, show next one
    return "<p>Approved</p>"

@app.route("/denied")
def deny_doc():
    # Send tristan email saying invoice was denied
    # If more invoices to approve, show next one
    return "<p>Denied</p>"

@app.route("/upload")
def upload_inoices():
    # Saves new invoice to the invoices folder
    # Sends manager email saying new invoice is ready for approval
    # Reloads to allow for more uploads
    return "<p>Uploaded</p>"

