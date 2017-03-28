#!/bin/bash
kill `cat logs/flask-image.pid` && ./start.sh
