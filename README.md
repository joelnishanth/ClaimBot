# ClaimBot

Minimal MVP for Etsy DMCA protection. This repository contains a Next.js frontend and three FastAPI services managed via Docker Compose.

## Development

```
docker-compose up --build
```

The services expose the following ports:

- **frontend**: http://localhost:3000
- **ListingContext**: http://localhost:8000
- **ScannerContext**: http://localhost:8001
- **DMCAContext**: http://localhost:8002

Configure environment variables in `.env` if needed.
