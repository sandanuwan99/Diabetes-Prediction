import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open('E:/ml_project/trained_model.sav','rb'))


# Assuming input_data contains values for all 8 features
input_data = [7,195,70,33,145,25.1,0.163,55]

# Standardize the input data using a separate scaler object fitted on the entire dataset or training set only
input_data_reshaped = np.array(input_data).reshape(1, -1)
#std_data = scaler.transform(input_data_reshaped)

# Predict using the classifier
prediction = loaded_model.predict(input_data_reshaped)

if prediction[0] == 0:
    print('The person is not diabetic')
else:
    print('The person is diabetic')
