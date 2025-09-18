# Simple String Stats (Dockerized Python CLI)

## Description
This project contains a very simple Python program (`app.py`) that:
- Accepts a command-line argument (or uses `"hello docker"` by default).
- Prints:
  1. The original string.
  2. The string length (number of characters).
  3. The number of words (split by whitespace).
  4. The reversed string.

The program is packaged in a Docker image so it can be run easily with or without arguments.

---

## Files
- `app.py` → Python program.
- `Dockerfile` → Dockerfile to build the image.
- `README.md` → This file with usage instructions.

# Run with custom string
docker run --rm simple-string-stats:1.0 sh -c 'python app.py "Docker is fun"'
