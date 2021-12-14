from flask import Flask, request,render_template
from gensim.models import Word2Vec as w2v

app=Flask(__name__)
model = w2v.load('models/w2v.model')

keys = []
for index, word in enumerate(model.wv.index_to_key):
    keys.append(word)

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html', prediction_text = 'HOME')

@app.route("/predict", methods=['POST']) #decorator
def predict():
    word = request.form["word"]
    if word in keys:
        prediction = model.wv.most_similar(word)
        return  render_template('index.html', prediction_text='Similar words would be $ {}'.format(prediction))
    return  render_template('index.html', prediction_text = "Given word is not key in w2v model")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')