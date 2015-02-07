
all: build

build: es pt en

es:
	pdflatex -shell-escape -synctex=1 -interaction=nonstopmode -8bit sponsors_es.tex

pt:
	pdflatex -shell-escape -synctex=1 -interaction=nonstopmode -8bit sponsors_pt.tex

en:
	pdflatex -shell-escape -synctex=1 -interaction=nonstopmode -8bit sponsors_en.tex

clean:
	rm -rf *.log *.out *.synctex.gz *.aux


