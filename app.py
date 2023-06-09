import pickle
import numpy as np

# Loading the saved model
with open('saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)

reg_load = data['model']

print("========================Mine vs Rock detecor========================")
print()
print()
print("In this application a linear regression model is used to detect whether the sonar sensor detects a rock or a mine. When entering the sensor data enter with comma seperated values.")
print()
print()
input_data = input("Enter the sonar sensor data")
# print(input_data)
# map the string to
input_data = list(map(float, input_data.split(",")))
# changing the input data for a numpy array
input_data_arr = np.asarray(input_data)

# reshape the numpy array
input_data_re = input_data_arr.reshape(1, -1)

prediction = reg_load.predict(input_data_re)
# print(prediction)

if (prediction[0] == 'R'):
    print('this is rock')
else:
    print('this is a mine')
