all: clean build

clean:
	find . -type f \( -name "*.aux" -o -name "*.acn" -o -name "*.ist" -o -name "*.brf" -o -name "*.glg" -o -name "*.glo" -o -name "*.gls" -o -name "*.xdy" -o -name "*.bbl" -o -name "*.blg" -o -name "*.log" -o -name "*.dvi" -o -name "*.lof" -o -name "*.lot" -o -name "*.out" -o -name "*.toc" -o -name "*.fls" -o -name "*.synctex.gz" -o -name "*.fdb_latexmk" -o -name "*.xdv" -o -name "tcc-html.pdf" \) -delete;

lint:
	find . -type f -name "*.tex" -exec tex-fmt --check {} \;

format:
	find . -type f \( -name "*.tex" -o -name "*.cls" -o -name "*.bib" \) -exec tex-fmt {} \;
	prettier "**/*.{css,html}" --write;

build:
	latexmk -pdfxe tcc.tex

html:
	pandoc tcc-html.tex -o index.html --metadata title="Trabalho de Conclusão de Curso" --css=style.css --standalone && ./format-html.sh index.html && prettier index.html style.css --write

mermaid:
	mmdc -i mermaid/fluxo-1.mmd -o imagens/fluxo-1.png -b transparent;
	mmdc -i mermaid/fluxo-2.mmd -o imagens/fluxo-2.png -b transparent;
	mmdc -i mermaid/fluxo-3.mmd -o imagens/fluxo-3.png -b transparent;

.PHONY: all clean build lint format html mermaid