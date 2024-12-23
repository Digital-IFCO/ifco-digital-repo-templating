#!/bin/sh
set -e
REPODIR=/app/scripts

##Testing
echo "Running Unit Tests"
bash $REPODIR/run_tests.sh || {
  echo "Unit tests failed."
  exit 1
}

echo "Running Flake8 Tests"
cd /app/src
flake8 --output-file="flake8.txt" || {
  echo "Flake8 tests failed."
  cat flake8.txt
  exit 1
}
