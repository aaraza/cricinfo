#!/usr/bin/env bash
ruff check .
coverage run -m pytest  -v -s
coverage report -m