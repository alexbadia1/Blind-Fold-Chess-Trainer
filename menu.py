class MenuItem:
    def __init__(self, newKey, newDescription, newFunction):
        self.key = newKey
        self.description = newDescription
        self.newFunction = newFunction
    
    def toString(self):
        return self.key + ".) " + self.description

class Menu:
    def __init__(self, greeting):
        self.dictionary = {}
        self.greeting = greeting

    def addMenuItem(self, key, menuItem):
        self.dictionary.update({key : menuItem})

    def showMenu(self):
        print()
        print(self.greeting)
        for menuItem in self.dictionary.values():
            print(menuItem.toString())

    def getUserChoice(self):
        self.showMenu()

        # Get user choice
        choice = input("Choose a menu option: ").upper()

        # Lookup choice in dictionary and fire the function linked to it
        try:
            self.dictionary.get(choice).newFunction()
        except:
            print("\nPlease select a valid choice from the menu!")
            self.showMenu()
            self.getUserChoice()

        
