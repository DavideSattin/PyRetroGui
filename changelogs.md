# Changelog

## [2026-03-08]

### Added
- New file `pyretrogui/appearance/widget_appearance.py`:
  - Definition of the `WidgetAppearanceMode` enumeration for various color modes (PRIMARY, SECONDARY, SUCCESS, INFO, WARNING, ERROR, CUSTOM).
  - New `WidgetAppearance` class to manage the visual appearance of widgets, acting as a bridge between the global `Theme` and individual widgets.
  - Support for color customization in `CUSTOM` mode.

### Changed
- Initial refactoring in `pyretrogui/ui_elements/text_widget.py`:
  - Removal of the old direct theme management to prepare for integration with the new `WidgetAppearance` class.
