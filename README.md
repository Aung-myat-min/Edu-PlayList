# Enterprise Software Engineering - Assignment 2

## 🎵 Console Music Playlist Manager

This repository contains the source code for Assignment 2 of the CET3016 module at the University of Sunderland. It is a robust, console-based application for managing music playlists, developed using **Python**.

The project demonstrates modern software engineering practices, including the **Model-View-Controller (MVC)** architectural pattern, clean code principles, and user-friendly console interactions.

---

## 🚀 Features

### 🔐 Authentication & Security
*   **Secure Login**: Single-user authentication system.
*   **Lockout Mechanism**: After 3 failed attempts, the system locks for **5 minutes** with a live countdown timer.
*   **Input Validation**: Strict validation for usernames and passwords.

### 📂 Playlist Management
*   **Create & Delete**: Easily create new playlists with names and notes, or delete existing ones.
*   **View & Sort**: View all playlists in a formatted table. Sort them **Alphabetically (A-Z)** or **Reverse (Z-A)**.
*   **Export**: Export all playlists and songs to an **Excel (.xlsx)** file for external use.
*   **Duplicate Detection**: Identify songs that appear in multiple playlists.

### 🎶 Song Management
*   **CRUD Operations**: Add, Edit, and Delete songs within a playlist.
*   **Sorting**: Sort songs within a playlist alphabetically.
*   **Shuffle**: Randomize the order of songs in a playlist.
*   **Live Updates**: The song list automatically refreshes and displays after any modification.

### 💾 Data Persistence
*   **Auto-Save**: All data is automatically saved to `.data/program_data.json`.
*   **Error Handling**: Corrupted data files are handled gracefully with automatic state recovery.

### 🖥️ User Interface
*   **Rich Console UI**: Uses `colorama` for colored output and `tabulate` for clean, readable tables.
*   **Smooth Experience**: Implements screen clearing and simulated typing delays for a polished user experience.
*   **Emojis**: Visual cues using emojis for better navigation.

---

## 🏗️ Architectural Pattern: MVC

The project is strictly organized following the **Model-View-Controller** pattern to ensure separation of concerns:

*   **📂 Models** (`/models`):
    *   Defines the data structure (`Playlist`, `Song`, `User`, `ProgramMeta`).
    *   Handles business logic and validation (e.g., regex for IDs).
    *   Manages serialization/deserialization (JSON conversion).
*   **📂 Views** (`/views`):
    *   Contains menu definitions and static display configurations.
    *   Decoupled from logic, focusing only on what to present.
*   **📂 Controllers** (`/controllers`):
    *   Acts as the bridge between Models and Views.
    *   Handles user input, calls model methods, and triggers UI updates.
    *   Specific controllers for specific tasks (e.g., `LoginController`, `PlaylistController`).

---

## 🧹 Clean Code & Best Practices

*   **Modularization**: Code is split into small, reusable modules (e.g., `utils/console_utils.py`, `utils/input_controller.py`).
*   **Type Hinting & Docstrings**: Functions and classes are documented with docstrings and type hints for clarity.
*   **Input Sanitization**: All user input is cleaned (trimmed, extra spaces removed) before processing.
*   **Configuration**: Global settings (like timeouts and file paths) are centralized in `settings.py`.
*   **Dependency Management**: External libraries are listed in `requirements.txt`.

---

## 🛠️ Setup & Installation

1.  **Clone the repository**:
    ```bash
    git clone <repo_url>
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application**:
    ```bash
    python main.py
    ```
