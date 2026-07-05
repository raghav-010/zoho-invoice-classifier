# zoho-invoice-classifier
Automatic invoice classification custom function for Zoho Books using Python

## Workflow

```
Invoice Status = Sent
        │
        ▼
Workflow Rule Triggered
        │
        ▼
Python Custom Function Executes
        │
        ▼
Extract Invoice Details
        │
        ▼
Check Invoice Amount
        │
        ▼
Amount >= 5000 ? ──► Enterprise
        │
        ├── Amount >= 1000 ? ─► High
        │
        ├── Amount >= 500 ? ──► Medium
        │
        └── Otherwise ─────────► Low
        │
        ▼
Log Classification in Workflow Logs
```
