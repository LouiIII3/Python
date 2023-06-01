class Player():
    def __init__(self, name, back_number):
        self.__name = name
        self.__back_number = back_number
        
    def print_stat(self):
        print("This is Player Class")
        print(f"Player Name: {self.__name}")
        print(f"Back Number: {self.__back_number}")
    
    def change_back_number(self, new_number):
        print(f"Change Back Number: From {self.__back_number} to {new_number}")
        self.__back_number = new_number
