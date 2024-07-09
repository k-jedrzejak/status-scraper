#!/bin/bash

cd /path/to/checkStatus/
source /path/to/checkStatus/myenv/bin/activate
python3 statusScraper.py >> /path/to/checkStatus/cron.log 2>&1
