# Manually Trainer.py

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.layers import Dense
from keras.optimizers import Adam
from keras.backend import clear_session
import numpy
import os
current_dir = os.getcwd()

# Loading Mnist dataset from keras.datasets 
(X_train, Y_train),(X_test, Y_test)=mnist.load_data('/storage/mnist.npz')
# changinging dimensions to 28*28 and datatype to float
X_test = X_test.reshape(-1,28*28)
X_test = X_test.astype('float32')
X_train = X_train.reshape(-1,28*28)
X_train = X_train.astype('float32')

# converting labels into categorical variables
Y_test = to_categorical(Y_test)
Y_train = to_categorical(Y_train)

# Creating NN Architecture using Sequential Model
model = Sequential()
model.add(Dense(units=30 , input_dim=28*28 , activation='relu'))
model.add(Dense(units=150 , input_dim=28*28 , activation='relu'))
model.add(Dense(units=100 , input_dim=28*28 , activation='relu'))
model.add(Dense(units=10 , input_dim=28*28 , activation='softmax'))
model.compile( optimizer='Adam',loss='categorical_crossentropy',metrics=['accuracy'] )
fit_model=model.fit(X_train,Y_train,epochs=2,verbose=False)

hist=fit_model.history
# Extracting accuracy from the accuracy metrics and also rounding off it.
acc = hist['accuracy'][1]*100
acc = int(acc)
with open('/storage/file','w+') as f:
    f.write(str(acc))
print("Manual training using hardcoded hyper-parameter, test ID = 1 and accuracy = ",acc, "%")
if int(acc)>95:
    model.save('/storage/trained_model.h5')
    print("model is saved as the accuracy was greater than 95 %")
else:
    print("model was not saved as the accuracy was lesser than 95%")
