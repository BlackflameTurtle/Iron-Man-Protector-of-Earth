import pickle
import os
class SaveandLoad:
    def __init__(self, file_extension, save_folder):
        self.file_extension = file_extension
        self.save_folder = save_folder
    def save_game(self,  data, name):
        data_file = open(name + self.file_extension, "wb")
        pickle.dump(data, data_file)
    def load(self, name):
        data_file = open(name + self.file_extension, "rb")
        data = pickle.load(data_file)
        return data
    def check_file(self, name):
        return os.path.isfile(name + self.file_extension)
    def del_save(self, name):
        return os.remove(name + self.file_extension)

    