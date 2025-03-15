# Virtual Laboratory

## Overview
The Virtual Laboratory is an interactive chemistry simulation application built using Pygame. Users can mix various chemicals to observe virtual chemical reactions, enhancing their understanding of chemistry in a fun and engaging way.

## Project Structure
```
virtual-laboratory
├── src
│   ├── main.py
│   ├── lab
│   │   ├── __init__.py
│   │   ├── chemicals.py
│   │   └── reactions.py
│   └── assets
│       ├── sounds
│       └── images
├── setup.sh
├── requirements.txt
└── README.md
```

## Installation

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd virtual-laboratory
   ```

2. **Set up a Python virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the setup script:
```
bash setup.sh
```

This will activate the virtual environment and start the main program.

## Features

- **Chemical Mixing:** Users can select and mix different chemicals to see the results of their combinations.
- **Visual and Audio Feedback:** The application includes sound effects and images to enhance the user experience.
- **Educational Tool:** Aimed at students and enthusiasts to learn about chemical reactions in a safe virtual environment.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.