# save-geeklist
Save a geeklist from BoardGameGeek, spanning multiple pages, to a PDF or HTML file.

## Prerequisites

This is mostly pretty simple code which just scrapes a website and should be usable directly with any current [Python](https://www.python.org/) installation, but to make things easier, more readable, and especially: compatible across Python versions (2.x/3.x), I am using the six library.

Getting six is mandatory, the other two dependencies can be skipped if you're ok with outputting to HTML only instead of PDF.

The code has been tested to work with Python 2.6 and 2.7.

### six

Get [six](https://pypi.python.org/pypi/six/), a compatibility module for Python 2 and 3. For example like this:
> pip install six

Or manually: just download the `six.py` from the [official repository](https://bitbucket.org/gutworth/six/src) and put it in the same directory as `SaveGeeklist.py`. 

### pdfkit

Get [pdfkit](https://pypi.python.org/pypi/pdfkit/), a python wrapper for the wkhtmltopdf program which converts to PDF. For example like this:
> pip install pdfkit

Or manually: Download an [archive of the module](https://pypi.python.org/pypi/pdfkit#downloads) and extract the `pdfkit` folder (without version suffix!) into the same directory as `SaveGeeklist.py`. 

### wkhtmltopdf

Get [wkhtmltopdf](http://wkhtmltopdf.org/) itself, for example from the [official download page](http://wkhtmltopdf.org/downloads.html). If necessary, edit the `pdfkit.configuration()` line in the `SaveGeeklist.py` source code to match your setup then.

## Usage

I am assuming that you are familiar with using the command line. This way, you'll be sure to keep track of the progress when running the program, and more importantly, see any error messages if something turns out to not be working like intended.

If all is set up, then you simply start the program:

> python SaveGeeklist.py

This will start the program with the default parameters so you can check if it is working correctly.

If you want to download a specific geeklist, you'll do it by editing the line in `SaveGeeklist.py` which reads
> (geeklist, first, last) = (19015, 1, 2)

* *geeklist* is the ID number for the geeklist on BGG
* *first* is the first page you want to include
* *last* is the last page you want to include

### Advanced usage

Play around with the `options`. You can use all the [wkhtmltopdf parameters](http://wkhtmltopdf.org/usage/wkhtmltopdf.txt), of which there are plenty.

## Help

For discussion or support requests with this code, go to https://boardgamegeek.com/thread/1644823
