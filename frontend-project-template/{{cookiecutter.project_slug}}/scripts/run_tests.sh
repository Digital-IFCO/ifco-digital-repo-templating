#!/bin/bash
result=0
coverage erase
coverage run -m unittest discover /app
if [[ $? -ne 0 ]]; then
    result=1
fi
coverage report -m
coverage xml -o /app/coverage.xml
exit $result