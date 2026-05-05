# WonderfulMysteriousApp

A self-contained FastAPI application that exposes several fun and useful endpoints — weather data, insights, fortunes, data submission, and user favorites — all backed by in-memory storage with no external service dependencies.

## Tech Stack

- **Python 3.11**
- **FastAPI** — web framework
- **Uvicorn** — ASGI server
- **Pydantic** — data validation
- **Pytest + pytest-asyncio + httpx** — testing
- **Docker** — containerization

## Project Structure

```
WonderfulMysteriousApp/
├── app/                    # Application source code
├── tests/                  # Unit, integration, and security tests
├── .github/workflows/      # CI pipeline
├── Dockerfile
├── requirements.txt
├── Test Plan.md
├── Test Strategy.md
├── Manual_Testing.md
└── Updated Test Report.md
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/weather` | Returns mock weather data (optional `city` query param) |
| GET | `/api/insight` | Returns a random insight |
| GET | `/api/fortune` | Returns a random fortune |
| POST | `/api/submit` | Accepts a structured `{ user, data }` payload |
| GET | `/api/favorites` | Returns the current favorites list |
| POST | `/api/favorites` | Adds an item to the favorites list |

> Rate limiting is enforced globally via middleware. Exceeding the limit returns `429 Too Many Requests`. The best way to try out these endpoints is using Swagger: http://localhost:8000/docs 

## Getting Started

### Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`.

### Run with Docker

```bash
# Build the image
docker build -t wonderfulmysteriousapp .

# Run the container
docker run -p 8000:8000 wonderfulmysteriousapp
```

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v
```

The test suite includes unit tests, integration tests (via FastAPI's `TestClient`), security tests (input sanitization, rate limiting), and negative tests for invalid inputs.

## CI

The GitHub Actions pipeline automatically installs dependencies, sets `PYTHONPATH`, and runs the full test suite on every push. A failing test fails the build.

## Documentation

Additional testing documentation is available in the repository:

- [`Test Plan.md`](./Test%20Plan.md) — Full testing strategy and scope
- [`Test Strategy.md`](./Test%20Strategy.md) — High-level testing approach
- [`Manual_Testing.md`](./Manual_Testing.md) — Manual test cases
- [`Updated Test Report.md`](./Updated%20Test%20Report.md) — Latest test results

