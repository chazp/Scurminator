class Person(object):
    items = []
    def add_item(self, item_name):
        self.items.append(item_name)
    def remove_item(self, item_name):
        self.items.remove(item_name)
    def has_item(self, item_name):
        if item_name in self.items:
            return True
        else:
            return False
    def remove_all(self):
        self.items = []
    def print_items(self):
        print self.items

