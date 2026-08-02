#!/bin/sh
set -eu
: "${BASE_URL:?Set BASE_URL}"
: "${BASIC_AUTH_USER:?Set BASIC_AUTH_USER}"
: "${BASIC_AUTH_PASSWORD:?Set BASIC_AUTH_PASSWORD}"
base=${BASE_URL%/}
health=$(curl -fsS "$base/healthz")
printf '%s' "$health" | grep -qi 'presidio'
unauth=$(curl -sS -o /dev/null -w '%{http_code}' -H 'Content-Type: application/json' --data '{"text":"Call 212-555-5555","language":"en"}' "$base/analyze")
[ "$unauth" = "401" ]
analysis=$(curl -fsS --user "$BASIC_AUTH_USER:$BASIC_AUTH_PASSWORD" -H 'Content-Type: application/json' --data '{"text":"Call 212-555-5555","language":"en"}' "$base/analyze")
printf '%s' "$analysis" | grep -q 'PHONE_NUMBER'
anonymized=$(curl -fsS --user "$BASIC_AUTH_USER:$BASIC_AUTH_PASSWORD" -H 'Content-Type: application/json' --data "{\"text\":\"Call 212-555-5555\",\"analyzer_results\":$analysis,\"anonymizers\":{\"DEFAULT\":{\"type\":\"replace\",\"new_value\":\"<REDACTED>\"}}}" "$base/anonymize")
printf '%s' "$anonymized" | grep -q '<REDACTED>'
printf '%s' "$anonymized" | grep -vq '212-555-5555'
wrong=$(curl -sS -o /dev/null -w '%{http_code}' --user "$BASIC_AUTH_USER:not-the-password" -H 'Content-Type: application/json' --data '{"text":"probe","language":"en"}' "$base/analyze")
[ "$wrong" = "401" ]
printf '%s\n' 'Presidio smoke checks passed'
