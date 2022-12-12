import json
from os import getenv
from pathlib import Path


NAME_LENGTH = 32


input_folder = Path(getenv(
    'CROSSCOMPUTE_INPUT_FOLDER', 'batches/standard/input'))
output_folder = Path(getenv(
    'CROSSCOMPUTE_OUTPUT_FOLDER', 'batches/standard/output'))


task = (input_folder / 'task.txt').read_text().splitlines()
environment = (input_folder / 'environment.txt').read_text().splitlines()
equipment = (input_folder / 'equipment.txt').read_text().splitlines()
weather = (input_folder / 'weather.txt').read_text().splitlines()


options = []
if 'hot' in weather:
    options.append({'value': 'stay hydrated'})
with (output_folder / 'topics.json').open('wt') as f:
    json.dump({'options': options}, f)
with (output_folder / 'topics.txt').open('wt') as f:
    f.write('')
