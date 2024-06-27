class Genre:
    def __init__(self, name, description, category):
        self.__name = name
        self.__description = description
        self.__category = category

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def category(self):
        return self.__category

    def get_category_details(self):
        return f"Genre: {self.__name}, Description: {self.__description}, Category: {self.__category}"

    def __repr__(self):
        return f"Genre('{self.__name}', '{self.__description}', '{self.__category}')"
