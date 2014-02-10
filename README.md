Varnish Purge (Python)
=============

This script is to help the developer purge Varnish cache.

## Requirements
- Python 2.7

## Usage

### For small sites
1. To purge a single path run:
	```
	python varnishPurge.py
	```
3. Enter the information you are being asked.

### For large sites
1. Edit varnishSteppedPurge.py ,  and edit the list called **listPurgeDirs** .
2. Add or remove the paths you want to flush in sequence. By default, it will purge one directory per hour.
3. Run the script with
	```
	python varnishSteppedPurge.py
	```
4. Enter the information you are being asked.

It is very important *NOT* to flush the entire Varnish cache for a very large/high traffic web site, since this could potentially bring the site down.


