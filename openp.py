import pickle

# Open the .p file in binary mode
with open('german-traffic-signs/test.p', 'rb') as f:
        train_data = pickle.load(f)
print(len(train_data)   ) 

# Now 'data' contains the Python object that was saved in the .p file
