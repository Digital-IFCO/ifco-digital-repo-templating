#!/bin/sh
set -e
REPODIR=/app/scripts

##Testing
echo "Running Unit Tests"
bash $REPODIR/run_tests.sh || {
  echo "Unit tests failed."
  exit 1
}
