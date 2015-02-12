build: en pt
	
en: call_for_papers_en.html
	
pt: call_for_papers_pt.html

%.html: %.md
	pandoc -f markdown -t html -o $@ $<
