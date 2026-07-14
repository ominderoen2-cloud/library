# Library

A Flask-based REST API for managing a library system — members, books, borrowing records, and user authentication — backed by PostgreSQL.

## Features

- **Member management** — track library members
- **Book catalog** — manage books available for borrowing
- **Borrowing records** — track which books are borrowed, by whom, and when
- **User authentication** — JWT-based auth with `flask-jwt-extended`, passwords hashed with `bcrypt`
- **Layered architecture** — routes, services, models, and validators are separated for maintainability

## Tech Stack

- **Framework:** Flask
- **Database:** PostgreSQL (`psycopg2-binary`)
- **Auth:** Flask-JWT-Extended, bcrypt
- **Server:** Gunicorn (production)
- **Config:** python-dotenv

## Project Structure

```
library/
├── app.py              # Application entry point
├── database/           # DB connection and table creation
├── models/              # Data models
├── routes/               # Flask blueprints / API routes
├── services/            # Business logic
├── validators/          # Request/input validation
├── tests/               # Test suite
├── requirements.txt
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL instance
- `pip`

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/ominderoen2-cloud/library.git
   cd library
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables

   Create a `.env` file in the project root:

   ```env
   JWT_SECRET_KEY=your-secret-key
   PORT=67
   # Add your PostgreSQL connection details here, e.g.:
   # DATABASE_URL=postgresql://user:password@host:port/dbname
   ```

5. Run the application

   ```bash
   python app.py
   ```

   The API will start on `http://0.0.0.0:$PORT` (defaults to port `67`).

### Verifying it's running

```bash
curl http://localhost:67/
```

```json
{"status": "api running"}
```

## Database

On startup, the app automatically creates the required tables if they don't already exist:

- `members`
- `books`
- `borrow_books`
- `users`

## Running Tests

```bash
pytest tests/
```

## Deployment

The app is Gunicorn-ready for production:

```bash
gunicorn app:app
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to the branch and open a pull request

## License

No license specified yet. Consider adding one (e.g., MIT) to clarify how others can use this project.
