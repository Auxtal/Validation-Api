from flask import Flask, jsonify, request
import re

app = Flask(__name__)
email_regex = re.compile(r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""")
time_regex = re.compile(r"((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]))")

@app.route('/')
def index():
    return jsonify({"What?": "API For Validating Time And Emails For Technical Production Form Submissions."}), 200

@app.route("/validate/time", methods=["POST"])
def validate_time():
    time = request.json.get("time")
    if not time:
        return jsonify({"error": "Time is required"}), 400

    match = re.search(time_regex, time)
    print(f"Time Match:\n{match}")
    return jsonify({"result": True if match else False}), 200

@app.route("/validate/email", methods=["POST"])
def validate_email():
    email = request.json.get("email")
    if not email:
        return jsonify({"error": "Email is required"}), 400

    match = re.search(email_regex, email)
    print(f"Email Match:\n{match}")
    return jsonify({"result": True if match else False}), 200

if __name__ == "__main__":
    app.run(debug=True)
