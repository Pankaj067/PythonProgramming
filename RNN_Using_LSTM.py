from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

print("Test")

Data = [[[(i+j)/100] for i in range(5)] for j in range(100)]
Target = [(i+5)/100 for i in range(100)]
Data = np.array(Data, dtype=float)
Target = np.array(Target, dtype=float)

Data.shape

Target.shape

x_train,x_test,y_train,y_test=train_test_split(Data,Target,test_size=0.2, random_state=4)

model = Sequential()
model.add(LSTM((1),batch_input_shape=(None,None,1),return_sequences=True))
model.add(LSTM((1),return_sequences=False))
model.compile(loss='mean_absolute_error',optimizer='adam',metrics=['accuracy'])
model.summary()

history = model.fit(x_train,y_train,epochs=400,validation_data=(x_test,y_test))

results = model.predict(x_test)


plt.scatter(range(20),results,c='r')
plt.scatter(range(20),y_test,c='g')
plt.show()

plt.plot(history.history['loss'])
plt.show()