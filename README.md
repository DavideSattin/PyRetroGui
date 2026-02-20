# PyRetroGUI

A retro-style terminal UI framework built with pygame.

## Overview

PyRetroGUI is an experimental framework that emulates a retro text-based screen
for building user interfaces. It uses a character grid buffer and a dirty-cell
rendering strategy to optimize drawing operations.

The goal of the project is to explore:

- Low-level rendering concepts
- Invalidation areas (dirty rectangles)
- Event-driven architecture
- Terminal-style UI abstraction
- Lightweight UI framework design

## Features (Work in Progress)

- Character-based screen buffer
- Dirty cell rendering optimization
- Basic event system
- Theme support
- Retro visual style

## Architecture

The rendering system is based on:

- A virtual character matrix
- A video buffer abstraction
- Dirty area tracking to minimize redraw operations
- Pygame as low-level rendering backend

## Status

⚠️ This project is experimental and under active development.
Architecture and APIs may change.

## Roadmap

- [ ] Improve invalidation strategy
- [ ] Add layout management
- [ ] Expand event system
- [ ] Widget abstraction layer
- [ ] Performance profiling

## Author

Davide Sattin