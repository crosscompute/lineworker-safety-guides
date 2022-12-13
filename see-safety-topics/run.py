import json
from os import getenv
from pathlib import Path


from invisibleroads_macros_text import format_slug


def get_lines(path):
    try:
        lines = path.read_text().splitlines()
    except OSError:
        lines = []
    return lines


input_folder = Path(getenv(
    'CROSSCOMPUTE_INPUT_FOLDER', 'batches/standard/input'))
output_folder = Path(getenv(
    'CROSSCOMPUTE_OUTPUT_FOLDER', 'batches/standard/output'))
datasets_folder = Path('datasets')


topics = []
for section in ['task', 'environment', 'equipment', 'weather']:
    path = input_folder / f'{section}.txt'
    for subsection in get_lines(path):
        path = datasets_folder / section / f'{format_slug(subsection)}.txt'
        for topic in get_lines(path):
            topics.append(topic)
with (output_folder / 'topics.json').open('wt') as f:
    json.dump({'options': [{'value': _ for _ in topics}]}, f)
with (output_folder / 'topics.txt').open('wt') as f:
    f.write('')
