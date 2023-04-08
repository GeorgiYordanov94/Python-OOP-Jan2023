class Player:
    players_list = []
    PLAYER_MAX_STAMINA = 100

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    # NB! с долните 3 реда правя така че self.need_sustenance да връща True, ако stamina падне по 100
    @property
    def need_sustenance(self):
        return True if self.stamina < Player.PLAYER_MAX_STAMINA else False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        if value in self.players_list:
            raise Exception(f"Name {value} is already used!")
        self.players_list.append(value)
        self.__name = value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
