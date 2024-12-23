#!/bin/bash
result=0
coverage erase
coverage run -m pytest /app/tests/
if [[ $? -ne 0 ]]; then
  result=1
fi
coverage report -m
coverage xml -o /app/coverage.xml
exit $result

