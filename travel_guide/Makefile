build: en pt es

en: htt_en.html

pt: htt_pt.html

es: htt_es.html

%.html: %.md
	pandoc -f markdown -t html -o $@ $<

clean:
	rm -rf *.html
