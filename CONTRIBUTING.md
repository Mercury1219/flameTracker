# Contributing

This repository is a fork of `combustionTools/flameTracker`. Keep changes small,
reviewable, and easy to propose upstream.

## Development setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

Run Flame Tracker from the scripts directory:

```powershell
cd scripts
python flameTracker.py
```

## Verification

From the repository root:

```powershell
python -m compileall -q scripts tests
$env:QT_QPA_PLATFORM = 'offscreen'
python -m pytest -q
Remove-Item Env:QT_QPA_PLATFORM
```

Build the Windows executable with:

```powershell
python -m PyInstaller --noconfirm --clean flameTracker.spec
```

## Change workflow

1. Create a short-lived `fix/...`, `feature/...`, or `docs/...` branch.
2. Use Conventional Commits such as `fix: show scale measurement dialog`.
3. Include tests for changed behavior and update `CHANGELOG.md` for user-facing
   changes.
4. Open a pull request and merge only after CI passes.

Release tags are annotated and use the `v<major>.<minor>.<patch>` format. The
tag, `VERSION`, application title, README release badge, and GitHub Release must
agree.
