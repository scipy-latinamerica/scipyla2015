build: en pt es
	
en: announcement_en.html
	
pt: announcement_pt.html

es: announcement_es.html

%.html: %.md
	pandoc -f markdown -t html -o $@ $<
