import numpy as np
import h5py
from keras.models import load_model
from keras import backend as K

batch_size = 64
num_classes = 3

def get_data(Masterdir, filename, data_name):
  """
	Purpose -> It is used to get data stored in an h5py file.
	Input   -> Filename, folder location and the key name in h5py file.
	Output  -> Extracted Data
  """
  h5f = h5py.File(Masterdir+filename+'.h5', 'r')
  return h5f[data_name]

def evaluate_model(X_test,y_test,model,batch_size,num_classes):
	"""
	Purpose -> It is used to evaluate the model on the testing data.
	Input   -> Testing data and its corresponding label, trained model.
	Output  -> Nil
	"""
	#Evaluate the accuracies
	score, acc = model.evaluate(X_test, y_test, batch_size=batch_size)
	print('Test score:', score)
	print('Test accuracy:', acc)

if __name__ == '__main__':

	#Master function
	#Load the model from h5py file and print is summary.
	print('Loading Model...')
	model = load_model("./LSTM_Keras_model.h5")
	print('Summary of the Model...\n')
	model.summary()

	print('Loading Training Data...')
	X_test = get_data('./', "Test_Data", "X_test")
	print('X_test.shape: ',X_test.shape,"\n\nEmbedding vector of a word present in test set...")
	print(X_test[1][30])

	y_test = get_data('./', "Test_Data", "y_test")
	print("Sentiment Label of Test example[0]", y_test[0])
	
	print('Data Loaded...\n\nEvaluate Model...')
	evaluate_model(X_test, y_test, model, batch_size, num_classes)

