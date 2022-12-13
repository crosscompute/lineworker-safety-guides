import json
from pathlib import Path


topics = []
datasets_folder = Path(__file__).parents[2] / 'see-safety-topics' / 'datasets'
for path in datasets_folder.glob('**/*.txt'):
    topics.extend(path.read_text().splitlines())
datasets_folder = Path(__file__).parents[1] / 'batches' / 'standard' / 'input'
with (datasets_folder / 'topics.json').open('wt') as f:
    json.dump({'options': [{'value': _} for _ in topics]}, f)
