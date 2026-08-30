# Changelog

All notable changes to this fork are documented in this file. Versions follow
[Semantic Versioning](https://semver.org/).

## [1.5.0] - 2026-08-30

### Added

- Added live English and Simplified Chinese switching from the new Language
  menu, with the selected language remembered between launches.
- Added centralized translations for the Preview, Manual, Luma, RGB, HSV, and
  Ember interfaces, including menus, dialogs, status messages, and graph axes.
- Added localization regression tests covering live widget updates and stable
  canonical values used by the tracking algorithms.

### Changed

- Kept English combo-box and action values as internal control identifiers so
  changing the display language does not alter analysis behavior or saved data.
- Added bilingual usage documentation and included localization in release
  verification.
- Excluded unrelated optional AI and notebook packages from Windows release
  builds so artifacts remain reproducible and compact.

## [1.4.2] - 2026-08-30

### Fixed

- Replaced the hidden, blocking OpenCV scale-measurement flow with one visible
  Qt dialog that combines endpoint selection, known-length input, and unit
  selection.
- Added a clear warning when Scale is selected before opening a video or image.
- Preserved quantitative accuracy when the measurement image is scaled to fit
  the display by mapping clicks back to the original frame coordinates.
- Fixed the analysis-method template's empty function so every Python source
  file passes compilation checks.

### Changed

- Added `VERSION` as the single release-version source.
- Added reproducible dependency, test, CI, and Windows packaging definitions.

[1.4.2]: https://github.com/Mercury1219/flameTracker/compare/v1.4.1...v1.4.2
[1.5.0]: https://github.com/Mercury1219/flameTracker/compare/v1.4.2...v1.5.0
