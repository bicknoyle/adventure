import unittest

from adventure.inventory import Inventory, Item

class TestIventory(unittest.TestCase):
    def setUp(self):
        self.inventory = inventory = Inventory()
        self.item = Item(id='my_item')
        inventory.add(self.item)

    def test_add(self):
        inventory = self.inventory
        self.assertTrue(inventory.has('my_item'))
        self.assertFalse(inventory.has('unknown_item'))

    def test_get(self):
        inventory = self.inventory
        self.assertEqual(inventory.get('my_item'), self.item)
        with self.assertRaises(KeyError):
            inventory.get('unknown_item')

    def test_remove(self):
        inventory = self.inventory
        self.assertEqual(inventory.remove('my_item'), self.item)
        with self.assertRaises(KeyError):
            inventory.remove('my_item')

    def test_list(self):
        inventory = self.inventory
        item = Item(id='another_item')
        inventory.add(item)
        self.assertEqual(len(inventory.list()), 2)

class TestItem(unittest.TestCase):
    def test_use(self):
        item = Item(id='my_item')
        self.assertIsNone(item.use())
