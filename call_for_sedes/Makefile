all: es.html

%.html: %.md
	 pandoc -t html  $^ | iconv -t utf-8 > $@
    # | iconv -f utf-8 > es.html

re: clean all

clean:
	rm -rf *.html
