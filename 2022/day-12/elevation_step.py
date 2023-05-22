class ElevationStep:

    data = None
    children = []
    parent = None
    path = []

    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        child.parent = self
        child.path = child.get_parent_data() + [child.data]
        self.children.append(child)

    def contains(self, new_data):
        return new_data in self.path

    def get_parent_data(self):
        if self.parent is None:
            return []
        return self.parent.get_parent_data() + [self.parent.data]
