from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/whoami")
def whoami():
    return render_template("whoami.html")

@app.route("/ls")
def ls():
    return render_template("ls.html")

@app.route("/man")
def man():
    return render_template("man.html")

@app.route("/send-email", methods=["POST"])
def send_email():
    """Endpoint to send email - integrate your email service here"""
    data = request.get_json()
    email = data.get("email", "")
    message = data.get("message", "")
    
    # TODO: Add your email service integration here (SendGrid, AWS SES, etc.)
    # For now, just simulate success
    
    if email and message:
        return jsonify({
            "success": True,
            "message": "Message sent successfully!"
        })
    else:
        return jsonify({
            "success": False,
            "message": "Error: Missing required fields"
        }), 400

if __name__ == "__main__":
    app.run(debug=True, port=5050)
