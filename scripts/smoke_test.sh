#!/usr/bin/env bash
# Quick checks against a running copy of the website (a container, staging or production).
# Usage: scripts/smoke_test.sh <base-url> [host-name]
# Example: scripts/smoke_test.sh http://localhost:8000 samparsa.se
set -euo pipefail

BASE_URL="${1:?give the base URL, for example http://localhost:8000}"
HOST="${2:-}"

# Behind Nginx the site only answers HTTPS requests, so the checks send the same
# header Nginx sends. The host name is only needed when the URL is not the real domain.
HEADERS=(-H "X-Forwarded-Proto: https")
if [ -n "$HOST" ]; then HEADERS+=(-H "Host: $HOST"); fi

FAILED=0

check() {
  local name="$1" result="$2" expected="$3"
  if [ "$result" = "$expected" ]; then
    echo "PASS  $name"
  else
    echo "FAIL  $name (expected $expected, got $result)"
    FAILED=1
  fi
}

status() { curl -s -o /dev/null -w '%{http_code}' "${HEADERS[@]}" "$@"; }

# Wait up to 30 seconds for the site to answer.
for _ in $(seq 1 30); do
  if [ "$(status "$BASE_URL/")" = "200" ]; then break; fi
  sleep 1
done

check "home page opens"        "$(status "$BASE_URL/")" "200"
check "projects page opens"    "$(status "$BASE_URL/projects/")" "200"
check "articles page opens"    "$(status "$BASE_URL/articles/")" "200"
check "unknown page gives 404" "$(status "$BASE_URL/this-page-does-not-exist/")" "404"

SV_PAGE="$(curl -s "${HEADERS[@]}" -H "Cookie: portfolio_lang=sv" "$BASE_URL/")"
check "Swedish page has 'Om mig'" "$(grep -c 'Om mig' <<<"$SV_PAGE")" "1"

CSS_PATH="$(curl -s "${HEADERS[@]}" "$BASE_URL/" | grep -o '/static/css/site[^"?]*' | head -1)"
check "stylesheet loads" "$(status "$BASE_URL$CSS_PATH")" "200"

if [ "$FAILED" -ne 0 ]; then
  echo "Smoke test FAILED"
  exit 1
fi
echo "Smoke test passed"
