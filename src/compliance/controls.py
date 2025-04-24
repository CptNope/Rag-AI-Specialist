import yaml
from pathlib import Path

class NISTControls:
    def __init__(self, path: Path = Path(__file__).parents[2] / "docs" / "nist-800-171" / "controls.yaml"):
        with open(path, 'r') as f:
            self._raw = yaml.safe_load(f)

    def get_control(self, family: str, id: str) -> dict:
        fam = self._raw.get(family, {})
        ctrl = fam.get(id)
        if not ctrl:
            raise KeyError(f"Control {family} {id} not found")
        return ctrl

    def list_all(self):
        for family, controls in self._raw.items():
            for cid, data in controls.items():
                yield family, cid, data