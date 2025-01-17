from flask import Flask, request

app = Flask(__name__)
secret_key = "complex_network_key"

@app.route('/flag', methods=['POST'])
def get_flag():
    if request.form.get('key') == secret_key:
        return "CTF{this_is_the_flag}", 200
    return "Access Denied", 403

def start_network_service():
    app.run(port=5000, debug=False)
