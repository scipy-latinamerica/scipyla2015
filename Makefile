
all: sponsors.pdf

%.pdf: %.tex
	pdflatex -shell-escape -synctex=1 -interaction=nonstopmode -8bit $^

