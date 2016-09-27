#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SaveGeeklist - save a geeklist from BoardGameGeek, spanning multiple pages, to a PDF or HTML file.

Copyright (c) 2016 BGG-Tools <https://github.com/bgg-tools>

released under the GNU General Public License v3.0

SaveGeeklist is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

SaveGeeklist is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with SaveGeeklist.  If not, see <http://www.gnu.org/licenses/>.
"""

### utf-8 shenanigans
# https://stackoverflow.com/a/21190382

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

### PDF conversion
# https://pypi.python.org/pypi/pdfkit
# https://stackoverflow.com/a/23761093

try:
	import pdfkit

	options = {
		'quiet': '',
		'page-size': 'A4',
	}

	# pdfkit configuration, see https://pypi.python.org/pypi/pdfkit#configuration
	#
	# I need to use a binary as I'm on Ubuntu, or otherwise links in PDF won't work
	# You can get pre-compiled binaries from http://wkhtmltopdf.org/downloads.html

	config = pdfkit.configuration(wkhtmltopdf='/opt/wkhtmltopdf-static/wkhtmltopdf')
except:
	pass	# in that case, we'll just save things as HTML

### simple method to load web pages
# https://stackoverflow.com/a/28040508

from six.moves.urllib.request import urlopen

### shortcut to extract text (don't parse the DOM)
# based on https://stackoverflow.com/a/3368991

def submatch(s, prefix, suffix):
	'''Return substring from string s, starting and including "prefix", until "suffix".'''
	try:
		start = s.index(prefix)
		end = s.index(suffix, start+len(prefix))
		return s[start:end]
	except ValueError:
		return ""

### the actual program, it's a bit chatty - using the logging module instead of "print" and
### determining the number of pages in the geeklist programmatically is left as an exercise

def geeklistpages(geeklist, first, last):
	'''Download pages from a geeklist on BGG and concatenate them

	Keyword arguments:
	geeklist -- the ID number of the geeklist on BGG
	first -- number of the first page to be included
	last -- number of the last page to be included
	'''

	# get header and geeklist items from first page

	page = urlopen('https://boardgamegeek.com/geeklist/%d/page/%d' % (geeklist, first)).read()
	print 'Loaded first page %d of geeklist #%d...' % (first, geeklist)

	html = u"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
	<html>
	   <head><base href="https://boardgamegeek.com/">"""	# replace original header with our custom one with BASE HREF tag
	html += submatch(page, "<!--[if lte IE 8]>", "<td width='120' valign='top'><div id='simpleCarousel'>")
	html += submatch(page, "<td valign='top' style='padding-left:10px;'>", "<div class='pager'>")
	html += submatch(page, "<div class='pager'>", "<div class='pager'>")

	# prepare status line to have good padding parameters

	status = 'Added page #%'+str(len(str(last)))+'d (%'+str(len(str(1+last-first)))+'d/'+str(1+last-first)+'), %s percent done...'

	# append geeklist items from the other pages

	for i in xrange(1+first, 1+last):
		page = urlopen('https://boardgamegeek.com/geeklist/%d/page/%d' % (geeklist, i)).read()
		html += submatch(page, "<div class='pager'>", "<div class='pager'>")
		print status % (i, 1+i-first, '{:.1%}'.format(float(i)/last))

	# please note: the HTML is truncated at this point, but most browsers and pdfkit don't care about that, they render it fine
	return html

### demo usage of the program if called from the command line
### the code can be imported as a module just as well,
### if somebody wants to build a command line parser around it

if __name__ == '__main__':
	# initialization with demo parameters
	(geeklist, first, last) = (19015, 1, 2)

	# collect pages
	selection = geeklistpages(geeklist, first, last)

	# output to disk, feel free to change this part to fit your needs
	try:
		pdfkit.from_string(selection, '%d.pdf' % (geeklist), options=options, configuration=config)
		print 'Saved as PDF'
	except IOError:
		with open('%d.html' % (geeklist), 'w') as output:
			output.write(selection)
		print 'Saved as HTML'
	print 'done!'
