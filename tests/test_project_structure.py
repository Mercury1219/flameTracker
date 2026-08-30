import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_required_release_files_exist():
    required = {
        'VERSION',
        'README.md',
        'LICENSE',
        'CHANGELOG.md',
        'CONTRIBUTING.md',
        'requirements.txt',
        'flameTracker.spec',
        'scripts/flameTracker.py',
    }
    missing = sorted(
        item for item in required if not (PROJECT_ROOT / item).is_file()
    )
    assert not missing, f'Missing release files: {missing}'


def test_version_is_semver_and_matches_source():
    version = (PROJECT_ROOT / 'VERSION').read_text(encoding='utf-8').strip()
    assert re.fullmatch(r'\d+\.\d+\.\d+', version)
    source = (PROJECT_ROOT / 'scripts' / 'flameTracker.py').read_text(
        encoding='utf-8'
    )
    assert 'self.version_FT = loadVersion()' in source
