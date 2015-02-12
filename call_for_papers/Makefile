build: en pt es
	
en: call_for_papers_en.html
	
pt: call_for_papers_pt.html

es: call_for_papers_es.html

%.html: %.md
	pandoc -f markdown -t html -o $@ $<
