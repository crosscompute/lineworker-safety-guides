from datetime import datetime
from os import getenv
from pathlib import Path


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
jobs_folder = datasets_folder / 'jobs'
briefings_folder = datasets_folder / 'briefings'


outline_lines = []


for path in briefings_folder.glob('**/topics.txt'):
    briefing_datetime = datetime.fromtimestamp(path.stat().st_mtime)
    topic_lines = get_lines(path)
    outline_lines.extend([
        '## ' + briefing_datetime.strftime('%A, %B %d, %Y %H:%M'),
    ] + ['- ' + _ for _ in topic_lines])


print('\n'.join(outline_lines))


with (output_folder / 'outline.md').open('wt') as f:
    f.write('\n'.join(outline_lines))
