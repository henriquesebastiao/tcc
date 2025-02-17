OS := $(shell uname 2>/dev/null || echo Windows)

ifeq ($(OS),Windows)
    FIND = powershell -Command "Get-ChildItem -Path . -Include *.aux,*.bbl,*.blg,*.log,*.dvi,*.lof,*.lot,*.out,*.toc,*.fls,*.synctex.gz,*.fdb_latexmk,*.xdv -Recurse | Remove-Item -Force"
    LINT = powershell -Command "Get-ChildItem -Path . -Filter *.tex -Recurse | ForEach-Object { tex-fmt --check $_.FullName }"
    FORMAT = powershell -Command "Get-ChildItem -Path . -Filter *.tex -Recurse | ForEach-Object { tex-fmt $_.FullName }"
else
    FIND = find . -type f \( -name "*.aux" -o -name "*.bbl" -o -name "*.blg" -o -name "*.log" -o -name "*.dvi" -o -name "*.lof" -o -name "*.lot" -o -name "*.out" -o -name "*.toc" -o -name "*.fls" -o -name "*.synctex.gz" -o -name "*.fdb_latexmk" -o -name "*.xdv" \) -delete
    LINT = find . -type f -name "*.tex" -exec tex-fmt --check {} \;
    FORMAT = find . -type f -name "*.tex" -exec tex-fmt {} \;
endif

clean:
	@echo "Limpando arquivos temporários..."
	@$(FIND)

lint:
	@echo "Verificando formatação dos arquivos .tex..."
	@$(LINT)

format:
	@echo "Formatando arquivos .tex..."
	@$(FORMAT)
