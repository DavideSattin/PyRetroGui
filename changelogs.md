# Changelog

## [2026-03-11]

### Added
- New `LayoutManager` (singleton) to calculate UI element viewports based on position and resize behaviors.
- New `SingletonLayoutManager` metaclass.
- Enhanced `ViewPort` class with helper methods: `top_left`, `top_right`, `bottom_left`, `bottom_right`, `center`, `top`, `bottom`, `left`, `right`.
- Added `translate` and `translate_to` methods to `Location` class.
- Added `add_width` and `add_height` methods to `Size` class.

### Changed
- Renamed package `pyretrogui/apparence` to `pyretrogui/appearance`.
- Integrated `WidgetAppearance` into `UIElement` and `TextWidget`.
- Refactored `UIElement` to delegate viewport calculation to `LayoutManager`.
- Updated `UIPanel` drawing methods (`draw_border`, `draw_text`, `draw_background`) to use absolute viewport translations.
- Improved `Context` and `VideoBuffer` with better drawing logic and error handling.
- Updated examples and tests to reflect the new appearance and layout structure.

### Fixed
- Fixed text drawing logic in `UIPanel` and `TextWidget`.
- Improved stability of `VideoBuffer` with better bounds checking.

## [2026-03-08]

### Added
- New file `pyretrogui/appearance/widget_appearance.py`:
  - Definition of the `WidgetAppearanceMode` enumeration for various color modes (PRIMARY, SECONDARY, SUCCESS, INFO, WARNING, ERROR, CUSTOM).
  - New `WidgetAppearance` class to manage the visual appearance of widgets, acting as a bridge between the global `Theme` and individual widgets.
  - Support for color customization in `CUSTOM` mode.

### Changed
- Initial refactoring in `pyretrogui/ui_elements/text_widget.py`:
  - Removal of the old direct theme management to prepare for integration with the new `WidgetAppearance` class.
