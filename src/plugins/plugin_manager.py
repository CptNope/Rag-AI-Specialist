import importlib, pkgutil
from .base import PluginBase

class PluginManager:
    def __init__(self, pkg='src.plugins'):
        self._plugins = {}
        self.discover(pkg)

    def discover(self, pkg):
        for _, name, _ in pkgutil.iter_modules([pkg.replace('.', '/')]):  # adjust path
            mod = importlib.import_module(f"{pkg}.{name}")
            for cls in vars(mod).values():
                if isinstance(cls, type) and issubclass(cls, PluginBase) and cls is not PluginBase:
                    inst = cls()
                    self._plugins[inst.name] = inst

    def get(self, name): return self._plugins.get(name)
    def list(self):    return list(self._plugins.keys())