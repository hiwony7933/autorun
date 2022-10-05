#!/bin/bash
cd /0.python/kan_naver/

echo "" >> debuglog.log
date +%Y-%m-%d_%T >> debuglog.log
echo "***** Start *****" >> debuglog.log
python3 main.py >> debuglog.log
echo "***** End *****" >> debuglog.log
