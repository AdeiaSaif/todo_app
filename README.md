# UltraTodoPro - Task Management Application

## Overview
UltraTodoPro is a modern, dark-themed desktop application built with Python and Tkinter for managing personal tasks. It features a clean single-window interface with robust task management capabilities.

## Features
- Create, update, and delete tasks
- Mark tasks as pending/completed
- Modern dark theme UI
- Design-by-Contract validation layer
- In-memory task storage
- Responsive design with column resizing
- Keyboard shortcuts for common actions

## Installation
1. Ensure you have Python 3.8+ installed
2. Clone this repository:
   ```
   git clone https://github.com/AdeiaSaif/UltraTodoPro.git
   ```
3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the application with:
```
python UltraTodoPro.py
```

### Key Interactions
- **Add Task**: Click the "+" button or use keyboard shortcut
- **Edit Task**: Double-click on a task
- **Toggle Status**: Click the status checkbox
- **Delete Task**: Select task and press Delete key

## Development
### Architecture
The application follows a three-layer architecture:
1. **GUI Layer** (Tkinter-based interface)
2. **Contract Layer** (Design-by-Contract validation)
3. **Storage Layer** (In-memory task list)

### Quality Assurance
We employ multiple strategies to ensure usability:
- Regular user testing sessions
- Heuristic evaluations against Nielsen's principles
- Automated usability metrics tracking
- WCAG 2.1 compliance for accessibility

## Versioning
We use semantic versioning (MAJOR.MINOR.PATCH). Current version: 1.0

## Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License
[MIT License](LICENSE)

## References
- ISO 9241-210:2019 - Human-centred design principles
- Nielsen's Heuristic Evaluation (1994)
- W3C WCAG 2.1 Accessibility Guidelines
