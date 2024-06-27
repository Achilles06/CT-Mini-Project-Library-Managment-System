import os

class DataHandler:
    @staticmethod
    def save_data(file_name, data):
        with open(file_name, 'w') as file:
            for key, obj in data.items():
                file.write(f"{key}:{obj}\n")

    @staticmethod
    def load_data(file_name):
        data = {}
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                for line in file:
                    key, obj_str = line.strip().split(':', 1)
                    data[key] = eval(obj_str)  # Caution: eval can be dangerous in production code.
        return data
