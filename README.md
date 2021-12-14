# Production-Deployment-ML-Model
A tutorial on deploying any ML model with Flask + Gunicorn + Nginx.

### Folder structure ###
![](others/my_code_LIGHT.png)

### The ML model we have ###
Given a text corpus, we run word2vec model on it. After tuning our parameters, we save our word2vec model as -
              `model.save("models/w2v.model")`
Now in any environment, all we need to do is - 
    ```
    model = w2v.load('models/w2v_bi_v10.model')
    word = "doctor"
    prediction = model.wv.most_similar(word)
    ```
 The prediction will contain list of top words with similarity score that are similar to word "doctor".
 
 ### GOAL ###
 We need to deploy a simple UI which intakes a word from user and then provides list of words similar to that word, based on our trained word2vec model.
 ![This is what we want](others/UI.png)
