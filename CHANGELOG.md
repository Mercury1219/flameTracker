# Changelog

All notable changes to this fork are documented in this file. Versions follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

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

[Unreleased]: https://github.com/Mercury1219/flameTracker/compare/v1.4.1...HEAD
