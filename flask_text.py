import tensorflow as tf
from tensorflow import keras
import numpy as np

word_index = data.get_word_index()

word_index = {k:(v+3) for k,v in word_index.items() }

word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3
reverse_word_index = dict([(value , key) for (key , value) in word_index.items()])


def decode_review(text): 
    return " ".join([reverse_word_index.get(i , "?") for i in text])



model = keras.models.load_model("model.h5")



def review_encode(s):
	encoded = [1]

	for word in s:
		if word.lower() in word_index:
			encoded.append(word_index[word.lower()])
		else:
			encoded.append(2)

	return encoded


def make_prediction(predicted_text) :
    for i in predicted_text :
	    nline = i.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace(":", "").replace("\"","").strip().split(" ")
	    encode = review_encode(nline)
	    encode = keras.preprocessing.sequence.pad_sequences([encode], value=word_index["<PAD>"], padding="post", maxlen=250) # make the data 250 words long
	    predict = model.predict(encode)
		return predict