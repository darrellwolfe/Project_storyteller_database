# Storyteller Database(s)
https://github.com/darrellwolfe/storyteller_database


This project is a minimal viable product (MVP) for a storytelling software tool. The application features a graphical user interface (GUI) for managing a storytelling database that includes characters, assets, and locations. This project is designed to run locally on your computer without any hosting or monthly fees.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Future Development](#future-development)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Graphical User Interface (GUI)**: Built with Tkinter, featuring sections for a world map and various lists.
- **Database Management**: Uses SQLite for local storage of characters, assets, and locations.
- **Basic CRUD Operations**: Create, Read, Update, and Delete functionality for database entries.
- **Modular Design**: Easily extendable with new columns and features.

## Technologies Used

- **Python**: Programming language.
- **Tkinter**: GUI library for Python.
- **SQLite**: Lightweight, disk-based database.
- **Folium** (optional): For map integration.

## Setup Instructions

### Prerequisites

- Python 3.x installed on your computer.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/darrellwolfe/storyteller_database.git
    cd storyteller_database
    ```

2. (Optional) Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Navigate to the project directory:
    ```bash
    cd storyteller_database
    ```

2. Run the main application script:
    ```bash
    python main.py
    ```

## Usage

- **Characters**: Add, view, update, and delete characters.
- **Assets**: Manage assets in your story.
- **Locations**: Keep track of various locations.

## Database Schema

The application uses SQLite with the following initial schema:

### Characters Table
| Column     | Type    |
|------------|---------|
| id         | INTEGER |
| name       | TEXT    |
| description| TEXT    |
| age        | INTEGER |
| birthdate  | TEXT    |

### Assets Table
| Column     | Type    |
|------------|---------|
| id         | INTEGER |
| name       | TEXT    |
| description| TEXT    |
| value      | REAL    |

### Locations Table
| Column     | Type    |
|------------|---------|
| id         | INTEGER |
| name       | TEXT    |
| description| TEXT    |
| coordinates| TEXT    |

## Future Development

- **Map Integration**: Display interactive maps with Folium or another library.
- **Enhanced UI**: Improve the user interface and experience.
- **Collaboration Features**: Allow multiple users to work on the same project.
- **Export/Import**: Enable data export and import functionality.
- **Additional Integrations**: Integrate with other tools and platforms.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

# Storyteller Database(s)

![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)

This project is a minimal viable product (MVP) for a storytelling software tool...

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. See the [LICENSE](LICENSE) file for details.


