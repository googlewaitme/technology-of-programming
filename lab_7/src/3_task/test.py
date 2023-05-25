import unittest

from main import *


class TestTable(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.table = Table()

    def test_add_thing_in_table(self):
        self.table.add_thing(Thing('tomat', 20))

        self.assertEqual(len(self.table.things), 1)
        self.assertEqual(self.table.get_table_cost(), 20)

        self.assertEqual(self.table.things[0].name, 'tomat')
        self.assertEqual(self.table.things[0].cost, 20)

    def test_search_on_table(self):
        self.table.add_thing(Thing('tomat', 20))
        tomat_index = self.table.get_index_by_name('tomat')
        self.assertEqual(self.table.things[tomat_index].name, 'tomat')
        self.assertEqual(self.table.find_by_cost(20).name, 'tomat')

        self.assertRaises(ValueError, self.table.find_by_name, 'notomat')
        self.assertRaises(ValueError, self.table.find_by_cost, 30)

    def test_delete_thing(self):
        self.table.add_thing(Thing('thing_to_delete', 1))
        count_of_things_now = self.table.get_count_things()
        self.table.delete_thing('thing_to_delete')
        count_of_things_after = self.table.get_count_things()
        self.assertEqual(count_of_things_now, count_of_things_after+1)

    def test_add_things_more_than_table_size(self):
        for i in range(self.table.get_count_things(), self.table.table_size):
            self.table.add_thing(Thing(f"thing{i}", i))
        self.assertRaises(TableIsFull, self.table.add_thing, Thing("over", 20))

    def tearDown(self):
        self.table.things = []
