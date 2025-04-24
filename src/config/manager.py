import yaml
from pathlib import Path
from .summarizer import summarize

class AgentConfigManager:
    def __init__(self, config_root: Path):
        self._configs = {
            p.stem: yaml.safe_load(p)
            for p in (config_root/"agent").glob("**/*.yaml")
        }

    def get(self, key: str, filter_keys: list = None) -> str:
        data = self._configs[key]
        if filter_keys:
            data = {k: data[k] for k in filter_keys if k in data}
        text = yaml.dump(data, sort_keys=False)
        return summarize(text) if len(text) > 1000 else text