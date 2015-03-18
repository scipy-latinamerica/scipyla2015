build: en pt es

en: hotels_en.html

pt: hotels_pt.html

es: hotels_es.html

%.html: %.md
	pandoc -f markdown -t html -o $@ $<

clean:
	rm -rf *.html
