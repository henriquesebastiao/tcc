all: clean build

clean:
	find . -type f \( -name "*.aux" -o -name "*.acn" -o -name "*.ist" -o -name "*.brf" -o -name "*.glg" -o -name "*.glo" -o -name "*.gls" -o -name "*.xdy" -o -name "*.bbl" -o -name "*.blg" -o -name "*.log" -o -name "*.dvi" -o -name "*.lof" -o -name "*.lot" -o -name "*.out" -o -name "*.toc" -o -name "*.fls" -o -name "*.synctex.gz" -o -name "*.fdb_latexmk" -o -name "*.xdv" -o -name "tcc-html.pdf" \) -delete;

lint:
	find . -type f -name "*.tex" -exec tex-fmt --check {} \;

format:
	find . -type f \( -name "*.tex" -o -name "*.cls" -o -name "*.bib" \) -exec tex-fmt {} \;

build:
	latexmk -pdfxe tcc.tex

md:
	pandoc -s tcc.tex -o tcc.md --bibliography bibliografia.bib

html:
	pandoc tcc-html.tex -o index.html --metadata title="Trabalho de Conclusão de Curso" --css=style.css --standalone && ./format-html.sh index.html && prettier index.html style.css --write

.PHONY: all clean build lint format md html