# Chatpy

Chatpy is a simple chat application built with Django. It allows users to register, log in, join chat groups, and send messages in real-time.

## Features

- User Registration and Authentication
- Real-time messaging using WebSockets
- Join and create chat groups
- Responsive UI built with Tailwind CSS

## Prerequisites

- Python 3.8+
- Django 3.2+
- SQLite (default database)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/chatpy.git
   cd chatpy
   ```

2. **Create a virtual environment:**

   ```sh
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```sh
   python3 manage.py migrate
   ```

5. **Run the development server:**

   ```sh
   python3 manage.py runserver
   ```

6. **Open your browser and visit:**

   ```
   http://127.0.0.1:8000/
   ```

## Usage

### Registration and Login

- Register a new user at `/register/`
- Log in at `/login/`

### Chat Groups

- Join or create chat groups after logging in.
- Each group has a unique URL where you can chat with other members.

### Sending Messages

- Type your message in the input field and press Enter or click the "Send" button.

## Running Tests

To run the tests, use the following command:

```sh
python3 manage.py test
```
