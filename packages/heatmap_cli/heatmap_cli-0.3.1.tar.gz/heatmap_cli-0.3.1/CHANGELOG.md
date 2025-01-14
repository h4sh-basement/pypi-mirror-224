# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [0-based versioning](https://0ver.org/).

## [Unreleased]

## v0.3.1 (2023-08-13)

### Changed

- Add logging for `-wk` related usages
- Sort URLs in project config

### Fixed

- Fix incorrect changelog URL
- Fix title without proper spacing

## v0.3.0 (2023-08-06)

### Added

- Add additional default hook for `pre-commit`
- Add `-cm` or `--cmap` option to set a default colormap

### Changed

- Rename test files based on the right term
- Add missing tests for `-wk` option

### Fixed

- Fix incorrect coverage configs
- Fix incorrect changelog URL

## v0.2.2 (2023-07-30)

### Added

- Add changelog URL to help message
- Add missing documentation for functions

### Changed

- Set title and PNG filename to year only when week is set to 52
- Reset DataFrame index after the last filtering step
- Move some coverage configs to `tox.ini` file

### Fixed

- Fix incorrect header level in changelog
- Fix incorrect source module in coverage config file

## v0.2.1 (2023-07-28)

### Changed

- Move `coverage` config from `tox` to its own file
- Reset DataFrame index after filtering

### Fixed

- Show verbose log of last date of current week
- Fix incorrect header level in changelog

## v0.2.0 (2023-07-23)

### Added

- Add `yr` or `--year` argument to filter CSV data by year
- Add `wk` or `--week` argument to filter CSV data until week of the year
- Add additional pre-commit default checks
- Show generated PNG filename upon completion

### Changed

- Group all `sphinx` related deps under the `doc` category
- Standardize `tox` environment names

### Fixed

- Fix incorrect ignored coverage module
- Suppress logging from `matplotlib` in `debug` mode

## v0.1.3 (2023-07-16)

### Fixed

- Fix missing `pylint` dependency when running `pre-commit`
- Ignore word when running `codespell` pre-commit hook

## v0.1.2 (2023-07-11)

### Changed

- Link to license from contributing doc
- Use the same output folder for `sphinx` doc generation
- Revise `pyenv` installation with plugins in contributing doc
- Install `heatmap_cli` as editable installation in `pipenv` dev env

## v0.1.1 (2023-07-09)

### Fixed

- Fix missing dependencies on `pipx` installation
- Fix incorrect module name in `pre-commit` hooks

## v0.1.0 (2023-07-08)

### Added

- Initial public release
