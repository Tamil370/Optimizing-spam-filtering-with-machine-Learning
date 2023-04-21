from flask import Flask, render_template, request
import pickle
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from tensorflow.keras.models import load_model
loaded_model = load_model('spam.h5')
cv = pickle.load(open('cv1.pkl', 'rb')) 
app=Flask (_name_)
@spp.route('/')
def home():
    return render_template('home.html')
@app.route('/spam',methods=['POST','get'])
def prediction():
    return render_template('spam.html')
@app.route('?predict',methods=[POST])
def predict():
    if request.method=='POST':
        message=request.form['message']
        data=message
    new_review = str(data)
    print(new_review)
    new_review = re.sub('[^a-zA-Z]', '', new_review)
    new_review=new_review.lower()
    new_review = new_review.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words ('english')
    all_stopwords.remove('not')
    new_review= [ps.stem(word) for word in new_review if not word in set(all_stopwords)]
    new_review = ''.join(new_review)
    new_corpus = [new_review]
    new_X_test = cv. transform(new_corpus).toarray()
    print(new_X_test)
    new_y_pred = loaded_model.predict(new_X_test)
    new_X_pred = np.where(new_y_pred>0.5,1,0)
    print(new_X_pred)
    if new_review[0][0]==1:
        return render_template('result.html', prediction="Spam")
    else :
        return render_template('result.html', prediction="Not a Spam")
if __name__=="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(debug=False)



    
