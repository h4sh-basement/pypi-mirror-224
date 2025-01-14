import os
import re
from dataclasses import dataclass
from io import IOBase
from pathlib import Path

from busy.model.collection import Collection
from busy.storage import Storage

STATES = Collection.family_attrs('state')
RE_QUEUE = re.compile(f"([a-zA-Z0-9\\-]+)\\.({'|'.join(STATES)})\\.psv")


class FileStorage(Storage):

    def __init__(self, path: str = ''):
        if path:
            self.root = Path(path) if isinstance(path, str) else path
        else:
            env_var = os.environ.get('BUSY_ROOT')
            self.root = Path(env_var if env_var else Path.home() / '.busy')
            self.root.mkdir(parents=True, exist_ok=True)
        assert isinstance(self.root, Path) and self.root.is_dir()
        self.cache = {}

    def filepath(self, queue: str, state: str) -> str:
        return self.root / f"{queue}.{state}.psv"

    def get_collection(self, queue: str, state: str = 'todo'):
        id = (queue, state)
        if id not in self.cache:
            collection = Collection.family_member('state', state)()
            path = self.filepath(queue, state)
            if path.is_file():
                with open(path) as file:
                    collection.read_items(file)
            collection.changed = False
            self.cache[id] = collection
        return self.cache[id]

    def queue_exists(self, queue: str):
        collections = [self.get_collection(queue, s) for s in STATES]
        return any(len(c) for c in collections)

    @property
    def queue_names(self):
        """Return names of queues. Cache nothing."""
        result = set()
        for path in self.root.iterdir():
            if path.is_file() and (match := RE_QUEUE.match(path.name)):
                queue = match.groups()[0]
                if (queue not in result) and path.stat().st_size:
                    result.add(queue)
        return result

    def save(self):
        """Save any changes and clear the cache"""
        while self.cache:
            key, collection = self.cache.popitem()
            if collection.changed:
                path = self.filepath(*key)
                with open(path, 'w') as file:
                    collection.write_items(file)
