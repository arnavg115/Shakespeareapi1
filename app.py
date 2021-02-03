from flask import Flask,jsonify
import tensorflow as tf
app = Flask(__name__)
textmd = tf.saved_model.load("one_step")
@app.route("/")
def home():
    return ("The api is up")
@app.route("/api/v1/request/<id>")
def api(id:int):
    try:
        id = int(id)
    except ValueError:
        id = 50
    if id>200 or id<0:
        id = 50
    states = None
    next_char = tf.constant(['ROMEO:'])
    result = [next_char]

    for n in range(id):
        next_char, states = textmd.generate_one_step(next_char, states=states)
        result.append(next_char)
    m = tf.strings.join(result)[0].numpy().decode("utf-8")
    k = {"Shakespeare":m}
    return jsonify(k)
    
if "__main__" == __name__:
    app.run()
