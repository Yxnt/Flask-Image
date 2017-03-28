#!/bin/bash
venv/bin/gunicorn run:app -c gunicorn.conf -k gaiohttp
