
all: build

build: es pt en

sponsor-render:
	bash scripts/xcf2png.sh -f img/sponsors.xcf

es: sponsor-render
	rst2pdf flyer_es.rst -s style.json -o flyer_es.pdf --use-floating-images --fit-background scale;

pt: sponsor-render
	rst2pdf flyer_pt.rst -s style.json -o flyer_pt.pdf --use-floating-images --fit-background scale;

en: sponsor-render
	rst2pdf flyer_en.rst -s style.json -o flyer_en.pdf --use-floating-images --fit-background scale;

clean:
	rm -rf *.log *.out *.synctex.gz *.aux


