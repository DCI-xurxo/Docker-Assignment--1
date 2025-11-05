from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/terminal")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/send-email", methods=["POST"])
def send_email():
    """Endpoint to simulate email sending from terminal"""
    data = request.get_json()
    name = data.get("name", "")
    email = data.get("email", "")
    message = data.get("message", "")
    
    # Here you could integrate a real email service like SendGrid, AWS SES, etc.
    # For now we just simulate the response
    
    if name and email and message:
        return jsonify({
            "success": True,
            "message": f"✓ Email sent successfully\n✓ From: {name} ({email})\n✓ Message registered in the system"
        })
    else:
        return jsonify({
            "success": False,
            "message": "✗ Error: Missing required fields"
        }), 400

if __name__ == "__main__":
    app.run(debug=True, port=5050)
