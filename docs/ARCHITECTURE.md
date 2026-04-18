# Architecture

## Overview

The platform uses a FastAPI backend and React frontend with modular vulnerability scanners.

## Scanner Core

- `src/core/advanced_scanner.py` aggregates foundational tier scanners and advanced module scanners.
- Total loaded checks now exceed 2000 with module-level metadata for payloads, detection logic, exploitation technique, remediation, and test case coverage.

## API Layer

- REST routes are defined in `backend/src/api/routes.py`.
- Root metadata in `backend/src/api/app.py` is generated dynamically from scanner summary values.

## Data and Reporting

- In-memory persistence and reporting stubs are located under `backend/src/database` and `backend/src/reporting`.
- Reports support JSON generation and can be extended for PDF/HTML/compliance templates.
