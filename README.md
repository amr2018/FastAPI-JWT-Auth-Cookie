
# FastAPI-JWT-Auth-Cookie

## Overview
This repository contains a FastAPI application that demonstrates a secure authentication system using JWT (JSON Web Tokens) and cookie management. The code showcases how to handle user logins, token generation, and verification, as well as protecting routes to ensure only authorized users can access them.

## Features
- User login with email and password validation.
- JWT token generation for successful logins.
- Cookie management for maintaining user sessions.
- Protected endpoints that require a valid token to access.

## Installation
To run this FastAPI application, you will need to install the required dependencies:

```bash
fastapi==0.111.0
pydantic==2.7.1
PyJWT==2.8.0
```

## Usage
Start the server with the following command:

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Endpoints
- `POST /login`: Authenticate users and set a cookie with a JWT token.
- `GET /dashboard`: Display user information if authenticated.

## Security
The application uses JWT for secure authentication. The secret key and algorithm are customizable for enhanced security.

## Contributing
Contributions are welcome! Please feel free to submit pull requests or create issues for any bugs or improvements.

## License
[MIT](LICENSE)

