# Presidio on Railway

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/presidio-pii?referralCode=ZqgrJ0)

Deploy Presidio 2.2.364 analyzer and anonymizer services behind generated HTTP Basic authentication.

The Deploy on Railway button is added after the published route is verified.

## What this deploys

- Private Presidio Analyzer `2.2.364`, pinned to the maintained GHCR Linux/AMD64 image digest
- Private Presidio Anonymizer `2.2.364`, pinned by digest
- Public Caddy `2.10.2-alpine` proxy with generated HTTP Basic credentials
- Upstream-backed health checks and a 1 MB text request limit

## Usage

Read `BASIC_AUTH_USER` and `BASIC_AUTH_PASSWORD` from the proxy service variables.

Analyze text:

```bash
curl --user "$BASIC_AUTH_USER:$BASIC_AUTH_PASSWORD" \
  --header 'Content-Type: application/json' \
  --data '{"text":"Call me at 212-555-5555","language":"en"}' \
  https://your-domain.example/analyze
```

Pass the analyzer results with the same text to `/anonymize` to replace, redact, hash, encrypt, or mask detected values. No analyzed text is intentionally persisted by this topology.

## Model and accuracy scope

The official analyzer image provides its default English NLP setup. Presidio 2.2.364 can return HTTP 500 and write a traceback for some malformed or schema-invalid analyzer requests, so clients should validate JSON and required fields before submission. Presidio findings are probabilistic and pattern-based; false positives and false negatives are expected. Do not treat a successful response as proof that all sensitive data was detected. Add recognizers, models, languages, thresholds, and tests for your data domain.

## Security

Authentication reduces anonymous access but does not make arbitrary sensitive text safe to send. Operators remain responsible for transport clients, log hygiene, retention outside Presidio, access rotation, and reviewing detected entities before downstream use. The proxy does not log request bodies or Authorization values.

## Updating

Update analyzer, anonymizer, and Caddy tags and digests together, read migration notes, then repeat entity detection, anonymization, invalid input, authentication, model startup, logs, and redeploy soak tests.

## Validation

```bash
npm test
BASE_URL=https://your-domain.example BASIC_AUTH_USER=presidio BASIC_AUTH_PASSWORD=... ./scripts/smoke.sh
```

## Upstream

- Source: https://github.com/data-privacy-stack/presidio/tree/2.2.364
- Release: https://github.com/data-privacy-stack/presidio/releases/tag/2.2.364
- Documentation: https://microsoft.github.io/presidio/
- License: MIT

This repository contains Railway adapters and documentation. Presidio remains copyright Data Privacy Stack contributors and is not affiliated with Railway.
