# https://www.codewars.com/kata/6a95cebfe92add3a9634a71c

import uuid

class Menu:
    def __init__(self, name, external_id, menu_items=None):
        self.internal_id = uuid.uuid4()
        self.external_id = external_id
        self.name = name
        self.menu_items = menu_items or []  

class MenuItem:
    """ e.g. a hamburger"""

    def __init__(self, name, external_id, modifiers=None):
        self.internal_id = uuid.uuid4()
        self.name = name 
        self.external_id = external_id 
        self.modifiers = modifiers or [] 

class Modifier:
    """ e.g. 'extra cheese' """

    def __init__(self, name, external_id):
        self.internal_id = uuid.uuid4()
        self.name = name
        self.external_id = external_id
    
def create_new_menu(external_menu: dict) -> Menu:
    """ Parse a single external menu and return a fully-populated Menu object. """
    
    # Instantiate Modifiers on the menu
    modifiers = {}
    for modification in external_menu['modifiers']:
        new_mod = Modifier(modification['name'], modification['id'])
        modifiers[modification['id']] = new_mod
    
    # Instantiate Menu Items on the menu
    menu_items = []
    for dish in external_menu['menu_items']:
        new_dish = MenuItem(dish['name'], dish['id'], [modifiers[id] for id in dish.get('modifiers', [])])
        menu_items.append(new_dish)
        
    # Instantiate Menu object
    new_menu = Menu(
        external_menu['name'], 
        external_menu['id'], 
        menu_items
    )
    
    return new_menu
