#!/usr/bin/env bash

if [ -d "mm_venv" ]; then
    source mm_venv/bin/activate
else
    virtualenv mm_venv
    source mm_venv/bin/activate
    pip3 install -r requirements.txt
fi

export FLASK_APP=$(pwd)/app/index.py
python3 -m flask run
