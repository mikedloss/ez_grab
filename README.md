# ez_grab
Simple tool written in python to download things from websites

To use, you'll need to have lxml installed. Can be found here: http://lxml.de/

Usage
-----
Give it links in the url.txt file, with filetypes you want to download in the filetype.txt file. The tool simply looks at every link and searches for links with the given filetypes, and then downloads them in a somewhat structured subfolder. Its essentially an attempt at being a general scraper without needing to download a library.
