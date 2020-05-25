# Tuning Model's hyper-parameters using jenkins job by running this script.

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.layers import Dense
from keras.optimizers import Adam
from keras.backend import clear_session
import numpy

def trainModel(numUnits,model,numEpochs,test):
    model.add(Dense(units = numUnits , input_dim = 28*28 , activation = 'relu'))
    model.add(Dense(units=200 , input_dim = 28*28 , activation = 'relu'))
    model.add(Dense(units=60 , input_dim = 28*28 , activation = 'relu'))
    model.add(Dense(units=10 , input_dim = 28*28 , activation = 'softmax'))
    model.compile( optimizer='Adam',loss='categorical_crossentropy',metrics=['accuracy'] )
    return model

def validate(fit_model,epochs):
    hist=fit_model.history
    acc=hist['accuracy'][epochs-1]*100
    acc=int(acc)
    with open('/storage/file','w+') as f:
        f.write(str(acc))
    return acc



# Loading Mnist dataset from keras.datasets 
(X_train, Y_train),(X_test, Y_test)=mnist.load_data('/storage/mnist.npz')

# changinging dimensions to 28*28 and datatype to float
X_test=X_test.reshape(-1,28*28)
X_test=X_test.astype('float32')
X_train=X_train.reshape(-1,28*28)
X_train=X_train.astype('float32')

# converting labels into categorical variables
Y_test=to_categorical(Y_test)
Y_train=to_categorical(Y_train)

# Creating initial parameters
neurons=5
acc=0
epochs=1
test=2 # starting from 1st
f=False
#checking for better accuracy and 
while int(acc)<95:
    if f==True:
        # clearning previous model layers using clearing sessions
        model=keras.backend.clear_session()
        # tuning parameters hardcoding
        neurons+=1       
        epochs+=1
        test+=1
    model=Sequential()
    model=trainModel(neurons,model,epochs,test)
    fit_model = model.fit(X_train,Y_train,epochs=epochs,verbose=False)
    acc=validate(fit_model , epochs)
    print("Automatically tuning of parameters with test ID. = ",test," and accuracy = ",round(acc,2),"%")
    f=True
print("Saving the model as the accuracy becomes greater than 95%")
model.save('/storage/trained_model.h5')
