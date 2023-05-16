from datetime import time

#menu class
class Menu:
  def __init__(self, name, item, start_time, end_time):
    self.name = name
    self.item = item
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return (f"{self.name} menu avaliable from {self.start_time} to {self.end_time}")

  def calculate_bill(self, purchased_items):
    calculate = 0
    for i in purchased_items:
      if i in self.item.keys():
        calculate  += self.item.get(i)
    return calculate

#franchise class
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def avaliable_menus(self, time):
    menus_avaliable = []
    for i in self.menus:
      if ((time >= i.start_time) and (time <= i.end_time)):
        menus_avaliable.append(i)
    return menus_avaliable

#business class
class Business():
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

#MENUS
#brunch
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_start = time(11,0,0)
brunch_end = time(16,0,0)
brunch = Menu("brunch", brunch_items, brunch_start, brunch_end)

#early bird
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_start = time(15,0,0)
early_bird_end = time(18,0,0)

early_bird = Menu("Early-bird", early_bird_items, early_bird_start, early_bird_end)

#dinner
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_start = time(17, 0, 0)
dinner_end = time(23, 0, 0)

dinner = Menu("Dinner", dinner_items, dinner_start, dinner_end)

#kids
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_start = time(11, 0, 0)
kids_end = time(21, 0, 0)

kids = Menu("Kids", kids_items, kids_start, kids_end)

#tests
#test_list = ["pancakes", "home fries", "coffee"]
#test2 = ["salumeria plate" ,  'mushroom ravioli (vegan)']
#print(brunch.calculate_bill(test_list))
#print(early_bird.calculate_bill(test2))

#FRANCHISE
all_menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)

#print(flagship_store.avaliable_menus(time(17,0,0)))

#Business
nI_franchises = [flagship_store, new_installment]
new_installment = Business("Basta Fazoolin",nI_franchises)

#new Menu
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_start = time(10,0,0)
arepas_end = time(20,0,0)
arepas_menu = Menu("Take a' Arepa", arepas_items, arepas_start, arepas_end)

#new franchise
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

#business
arepas_business = Business("Take a' Arepa", arepas_place)
