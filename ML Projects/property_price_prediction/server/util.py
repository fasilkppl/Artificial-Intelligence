import os
import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


#running predict method on saved model
def get_estimated_price(location,sqft,bhk,bath):
    # try to find the index, if not return -1
    try:
        loc_index = __data_columns.index(location.lower()) #getting index (converting to lower case, because our json file has all lower case)
    except:
        loc_index = -1
    #running predict method on saved model
    x = np.zeros(len(__data_columns)) # create a numpy array withh all zeros.
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0: # locate index>=0
        x[loc_index] = 1 #make that 1, remaining elements will be zero, (this is done because we are using hot one encoding)

    return round(__model.predict([x])[0],2)# accessing first element of array ie, [0], that is a float number, and round that by 2 decimeal




# loading json file and saved model
def load_saved_artifacts():
    print("loading saved artifacts...start")

    global __data_columns   # accessing __data_columns outside function by declarind it a global variable.
    global __locations      # accessing __locations outside function by declarind it a global variable.
    
    # Always use directory of the script (util.py)
    base = os.path.dirname(os.path.abspath(__file__))

    columns_path = os.path.join(base, "artifacts", "columns.json") # configuring path for columns.json file
    model_path = os.path.join(base, "artifacts", "home_prices_model.pickle") # configuring path for saved model file

    # Load columns.json
    with open(columns_path, "r") as f:
        __data_columns = json.load(f)['data_columns'] # read all column names including sqft, bath, bhk
        __locations = __data_columns[3:] # skip first 3: sqft, bath, bhk

    global __model # accessing __model outside function by declarind it a global variable.
    # load model only if not already loaded
    # ie, load our save house_prices_model.pickle to  __model
    if __model is None:
        with open(model_path, "rb") as f:
            __model = pickle.load(f)

    print("loading saved artifacts...done")





# skips first 3 columns, rest all locations are returned
def get_location_names():
    return __locations

# all locations including first 3 are returnes
def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts() #called inside main
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # 'other' location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # 'other' location