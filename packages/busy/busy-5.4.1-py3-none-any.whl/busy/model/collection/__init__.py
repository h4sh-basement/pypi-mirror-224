from collections import UserList
from collections.abc import Iterable
from csv import DictReader, DictWriter
from io import IOBase

from busy.model.item import Item
from wizlib.class_family import ClassFamily
from busy.util.selector import Selector


class CollectionError(Exception):
    pass


class Collection(UserList, ClassFamily):

    # Attributes in order for reads and writes
    schema = ['description']

    def validate_item(self, item):
        if item.state != self.state:
            raise CollectionError(
                f"Incorrect state {item.state} for {self.state} collection")
        if '|' in item.description:
            raise CollectionError(
                f"Pipe symbol not permitted in item description '{item.description}'")

    def validate(self, value):
        for item in value if isinstance(value, Iterable) else [value]:
            self.validate_item(item)

    # Override list methods to make sure we've got Items of the right state.
    # There might be some methods missing here. Also set changed.

    def __setattr__(self, name, value):
        if name == 'data':
            self.validate(value)
        super().__setattr__(name, value)
        if name == 'data':
            self.changed = True

    def __setitem__(self, key, value):
        self.validate(value)
        self.changed = True
        return super().__setitem__(key, value)

    def __iadd__(self, value):
        self.validate(value)
        self.changed = True
        return super().__iadd__(value)

    def __delitem__(self, *args):
        self.changed = True
        return super().__delitem__(*args)

    def append(self, value):
        self.validate(value)
        self.changed = True
        return super().append(value)

    def extend(self, value):
        self.validate(value)
        self.changed = True
        return super().extend(value)

    def insert(self, index, value):
        self.validate(value)
        self.changed = True
        return super().insert(index, value)

    def __add__(self, value):
        self.validate(value)
        self.changed = True
        return super().__add__(value)

    def pop(self, *args):
        self.changed = True
        return super().pop(*args)

    def __init__(self, value=None):
        if value is None:
            super().__init__()
        else:
            self.validate(value)
            super().__init__(value)
        self.changed = False

    # Methods related to selection and maniuplation by "criteria"
    # Numbers in "criteria" start with 1.

    def select(self, *criteria):
        """Take "criteria" (such as tags, ranges of numbers, etc) and return the
        indices of the resulting items. In other parts of the class and
        subclasses, operations need to know what items to act on.
        """
        selector = Selector(criteria)
        return [i for i in selector.indices(self.data)]

    def items(self, indices: list[int] = None):
        """Return the items for a set of indices"""
        if indices is None:
            return self.data
        else:
            return [self[i] for i in indices]

    def replace(self, indices: list, newvalues: list):
        """Replace existing items at the select provided.

        Also inserts if the indices run out. Does not create items; expects them
        to already exist. Does not return anything since the calling code
        already has the new items.
        """
        _indices = sorted(indices)
        _newvalues = newvalues.copy()
        max = (_indices[-1] + 1) if _indices else 0
        while _newvalues and _indices:
            self[_indices.pop(0)] = _newvalues.pop(0)
        while _indices:
            del self[_indices.pop()]
        self[max:max] = _newvalues

    def delete(self, indices: list[int]) -> list:
        """Remove the items at select and return them"""
        killlist, keeplist = self.split(indices)
        self.data = keeplist
        self.changed = True
        return killlist

    def split(self, indices: list[int]) -> tuple[list, list]:
        """Return a tuple of items at indices and items not so"""
        inlist = [t for i, t in enumerate(self) if i in indices]
        outlist = [t for i, t in enumerate(self) if i not in indices]
        return (inlist, outlist)

    def write_items(self, fileish: IOBase, indices: list = None):
        """
        Write all or a set of items to a file-like object
        """
        writer = DictWriter(fileish, self.schema, delimiter="|")
        for item in self.items(indices):
            values = dict([(f, getattr(item, f)) for f in self.schema])
            writer.writerow(values)

    def read_items(self, fileish: IOBase, indices: list = None):
        """
        Read all or a set of items from a file-like object
        """
        indices = indices if indices else []
        reader = DictReader(fileish, self.schema, delimiter="|")
        items = [Item(state=self.state, **d) for d in reader]
        self.replace(indices, items)
        return items
