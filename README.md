# save-geeklist
Save a geeklist from BoardGameGeek, spanning multiple pages, to a PDF or HTML file.

It should be possible to use this code directly with any Python 2.x and 3.x installation (for HTML output) via:

> python SaveGeeklist.py

To be able to output to PDF, you will need to install pdfkit first: https://pypi.python.org/pypi/pdfkit<br/>
Make sure to edit or just comment out the line #49 where pdfkit.configuration() is called in that case.

For discussion or support requests with this code, go to https://boardgamegeek.com/thread/1644823
