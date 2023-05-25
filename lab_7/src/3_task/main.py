'''
writed by Bulat Zaripov
'''
from typing import List


class TableIsFull(Exception):
    "Called if the number of objects on the table is greater than it should be"


class Thing:
    '''
    class thing
    '''
    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost

    def __str__(self):
        return f"{self.name} {self.cost}"


class Toy(Thing):
    '''
    class thing
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Table:
    '''
    class table
    '''
    def __init__(self, table_size:int = 10, things: List[Thing] = []):
        self.table_size = table_size 
        self.things = things

    def get_table_cost(self):
        return sum(thing.cost for thing in self.things)

    def add_thing(self, thing: Thing):
        if len(self.things) >= self.table_size:
            raise TableIsFull
        self.things.append(thing)

    def delete_thing(self, search_name: str):
        index = self.get_index_by_name(search_name)
        del self.things[index]

    def get_count_things(self):
        return len(self.things)

    def find_by_name(self, search_name: str):
        index = self.get_index_by_name(search_name)
        return self.things[index]

    def get_index_by_name(self, search_name: str):
        for index, thing in enumerate(self.things):
            if search_name == thing.name:
                return index
        raise ValueError(f"Name {search_name} is not found")

    def find_by_cost(self, search_cost: int):
        for thing in self.things:
            if thing.cost == search_cost:
                return thing
        raise ValueError(f"Cost {search_cost} is not found")

    def __str__(self):
        name = "Table:"
        for thing in self.things:
            name += "\n" + str(thing)
        return name
