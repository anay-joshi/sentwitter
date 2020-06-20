from flask import Flask, request, jsonify
from classify import classify
import pickle

app = Flask(__name__)
f = open('sentiment_model.pickle', 'rb')
classifier = pickle.load(f)
f.close()

@app.route('/')
def hello():
	return "Hello World"

@app.route("/api/", methods=["POST"])
def classify_tweet():
	if request.method == "POST":
		data = request.get_json()
		sentence = data["sentence"]
		output = classify(sentence, classifier)
		data = {
			"sentence": sentence,
			"sentiment": output,
			"status_code": 200
		}
		return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True)