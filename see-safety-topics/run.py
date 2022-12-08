import json
from os import getenv
from pathlib import Path

from invisibleroads_macros_disk import make_random_folder


NAME_LENGTH = 32


input_folder = Path(getenv(
    'CROSSCOMPUTE_INPUT_FOLDER', 'batches/standard/input'))
output_folder = Path(getenv(
    'CROSSCOMPUTE_OUTPUT_FOLDER', 'batches/standard/output'))


task = (input_folder / 'task.txt').read_text().splitlines()
environment = (input_folder / 'environment.txt').read_text().splitlines()
equipment = (input_folder / 'equipment.txt').read_text().splitlines()
weather = (input_folder / 'weather.txt').read_text().splitlines()


run_folder = Path(make_random_folder(
    '../log-safety-briefing/runs', NAME_LENGTH))
run_input_folder = run_folder / 'input'
run_input_folder.mkdir()
options = []
if 'hot' in weather:
    options.append({'value': 'stay hydrated'})
with (run_input_folder / 'topics.json').open('wt') as f:
    json.dump({'options': options}, f)


batch_name = run_folder.name
with (output_folder / 'variables.dictionary').open('wt') as f:
    json.dump({
        'form': f'http://localhost:7000/a/log-safety-topics/r/{batch_name}/i',
    }, f)
