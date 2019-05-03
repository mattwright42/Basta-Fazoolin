# Create a Menu class
class Menu:
    def __init__(self, name, items, start_time, end_time):
        pass

    def __repr__(self):
        return({self.name} + "available from " + {self.start_time} + " pm to " + {self.end_time} + " pm.")


brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
                         }, 11, 16)

early_bird = Menu("early-bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                                 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
                                 }, 15, 18)

dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'caesar                                  salad': 16.00,
                         'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 23)

kids = Menu("kids", {'chicken nuggets': 6.50,
                     'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)


print(brunch)
