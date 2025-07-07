# AgentID Data Analyzer (Presidio)

FastAPI REST API wrapper around Microsoft Presidio for detecting sensitive data.

## Endpoint

POST /analyze

```json
{
  "text": "Paní Nováková, email: jana@example.com, telefon: 777-123-456"
}
```

Returns:

```json
{
  "entities": ["PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER"],
  "snippet": "Paní Nováková, email: jana@example.com, telefon: 777-123-456"
}
```
