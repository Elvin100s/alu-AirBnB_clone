# HBNB - The Console

Welcome to the HBNB Console project! This repository contains the initial backend for a clone of the AirBnB website, focusing on a command-line interface to manage application data. The console allows users to create, update, destroy, and view objects, with persistent storage using JSON serialization.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Available Commands](#available-commands)
- [Authors](#authors)

---

## Project Overview

The HBNB Console is the first step in building a full-stack AirBnB clone. It provides a command interpreter to manage the backend data models and storage. All data is stored persistently in a JSON file, allowing for easy serialization and deserialization between sessions.

---

## Repository Structure

| Task | Files | Description |
|------|-------|-------------|
| 0 | AUTHORS | Project authors |
| 1 | N/A | All code is PEP8 compliant |
| 2 | /tests | Unit tests for all class modules |
| 3 | /models/base_model.py | Base class for all models |
| 4 | /models/base_model.py | Support for recreating instances from dicts |
| 5 | /models/engine/file_storage.py, /models/__init__.py, /models/base_model.py | Persistent file storage system |
| 6 | console.py | Basic console functionality (quit, empty lines, EOF) |
| 7 | console.py | Methods for create, destroy, show, update |
| 8 | console.py, /models/engine/file_storage.py, /models/user.py | User class implementation |
| 9 | /models/user.py, /models/place.py, /models/city.py, /models/amenity.py, /models/state.py, /models/review.py | More model classes |
| 10 | console.py, /models/engine/file_storage.py | Dynamic console and storage updates |

---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/AirBnB_clone.git
   cd AirBnB_clone
   ./console.py
   ```
When this command is run the following prompt should appear:
(hbnb)
This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.
Commands
* create - Creates an instance based on given class

* destroy - Destroys an object based on class and UUID

* show - Shows an object based on class and UUID

* all - Shows all objects the program has access to, or all objects of a given class

* update - Updates existing attributes an object based on class name and UUID

* quit - Exits the program (EOF will as well)
Alternative Syntax