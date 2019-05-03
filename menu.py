class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        available_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menu.append(menu)

        return available_menu


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return self.name + " Menu available from " + str(self.start_time) + " to " + str(self.end_time) + "."

    def calculate_bill(self, purchased_items):
        bill = 0
        for item in purchased_items:
            if item in self.items:
                bill += self.items[item]
        return bill


brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
                         }, 1100, 1600)

early_bird = Menu("Early-Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                                 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
                                 }, 1500, 1800)

dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'caesar                                  salad': 16.00,
                         'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 1700, 2300)

kids = Menu("Kids", {'chicken nuggets': 6.50,
                     'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 1100, 2100)


menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise('1232 West End Road', menus)

new_installment = Franchise('12 East Mulberry Street', menus)

business_one = Business("Basta Fazoolin' with my Heart", [
                        flagship_store, new_installment])

# Arepa menu

arepas_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)

arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

business_two = Business("Take a' Arepa", [arepas_place])

print(business_two.franchises[0])
