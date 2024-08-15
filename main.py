from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_page():
    return app.send_static_file('index.html')

@app.route("/lora_test")
def lora_test_page():
    return app.send_static_file('car_test_set.html')

@app.route("/lora_eval")
def lora_eval_page():
    return app.send_static_file('car_eval_set.html')