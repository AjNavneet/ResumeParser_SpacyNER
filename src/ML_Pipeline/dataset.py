
import utils

# Define a function to read and convert data from JSON files
def read_data():
    # Read and convert data from the training JSON file
    train = utils.convert_json_to_spacy("D:\\Resume_Parser\\input\\train_1.json")  # train file

    # Read and convert data from the test JSON file
    test = utils.convert_json_to_spacy("D:\\Resume_Parser\\input\\test.json")      # test file

    # Return the training and test data
    return train, test
