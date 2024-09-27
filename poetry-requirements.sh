#!/bin/sh
poetry export --without-hashes | cut -f1 -d";" | sed 's/ *$//g' > requirements.txt
