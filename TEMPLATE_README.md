# Deploy and Host Presidio on Railway

## About Hosting Presidio

Presidio detects personally identifiable information in text and applies configurable anonymization operators. This template deploys stable version 2.2.364 with analyzer and anonymizer services kept private behind an authenticated proxy.

Retrieve `BASIC_AUTH_USER` and the generated `BASIC_AUTH_PASSWORD` from the proxy service before calling `/analyze` and `/anonymize`.

## Common Use Cases

- Detect names, phone numbers, emails, payment data, and identifiers
- Redact or replace sensitive text before storage or model processing
- Add a private PII-processing API to internal pipelines

## Dependencies for Presidio Hosting

### Deployment Dependencies

- Private Presidio Analyzer
- Private Presidio Anonymizer
- Public Caddy authentication proxy
- No database or persistent volume

### Implementation Details

Railway HTTPS routes to Caddy on port 8080. The proxy enforces generated HTTP Basic credentials, limits request bodies to 1 MB, and routes `/analyze` and `/anonymize` over Railway private DNS. `/healthz` verifies the analyzer; each private service also has its own `/health` deployment check.

Presidio 2.2.364 can return HTTP 500 for some malformed or schema-invalid requests, so clients should validate payloads before submission. Presidio detection is not infallible. The included official image uses its default English setup; production deployments need domain-specific recognizers, models, thresholds, and test corpora.

## Why Deploy Presidio on Railway?

Railway provides managed HTTPS, generated credentials, private service networking, health checks, and reproducible deployment for a stateless PII processing pipeline.
