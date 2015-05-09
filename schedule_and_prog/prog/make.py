#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import codecs

import requests
import bs4
import sh


PATH = os.path.abspath(os.path.dirname(__file__))

URL = "http://conf.scipyla.org/schedule"
ID = "scrap-program-here"
STYLE = "scrap-style"

TEMP_DIR = os.path.join(PATH, "_temp")
BUILD_DIR = os.path.join(PATH, "_build")
RES_DIR = os.path.join(PATH, "res")

HTML_PATH = os.path.join(TEMP_DIR, "scrap.html")
PDF_PATH = os.path.join(TEMP_DIR, "scrap.pdf")
PUBS_PATH = os.path.join(RES_DIR, "pubs.pdf")
PROG_PATH = os.path.join(BUILD_DIR, "prog.pdf")


if os.path.isdir(TEMP_DIR):
    shutil.rmtree(TEMP_DIR)
if os.path.isdir(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)


os.makedirs(TEMP_DIR)
os.makedirs(BUILD_DIR)


response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text)

prog = unicode(soup.find("span", {"id": ID}))

style = u"""
* {
    font-family: "Times", Sans-serif, sans-serif;
    font-size: 11px;
    color: black;
}

table {
    border-collapse: collapse;
}

table, th, td {
    border: 1px solid black;
}

h2:nth-of-type(1), h2:nth-of-type(2), h1,
table:nth-of-type(1), table:nth-of-type(2) {
    display: none;
}

#maintitle {
    color: black;
    font-size: 16px;
    display: block;
    text-align: center;
}

em {
    color: black;
    font-size: 0.9em;
}

"""

prog = u"""
<html>
    <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    </head>
    <body>
        <h1 id="maintitle">SciPy Latin America 2015<br>Schedule</h1>
        {prog}
        <style>{style}</style>
    </body>
</html>""".format(style=style, prog=prog)

with codecs.open(HTML_PATH, "w", encoding="utf8") as fp:
    fp.write(prog)

sh.wkhtmltopdf(HTML_PATH, PDF_PATH)
sh.pdftk(PDF_PATH, PUBS_PATH, "cat", "output", PROG_PATH)



