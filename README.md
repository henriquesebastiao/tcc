# Trabalho de Curso - Ciência da Computação

[![Lint](https://github.com/henriquesebastiao/tcc/actions/workflows/lint.yml/badge.svg)](https://github.com/henriquesebastiao/tcc/actions/workflows/lint.yml)
[![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat&logo=latex&logoColor=white)](https://www.latex-project.org/)

Projeto de TCC para a graduação em Ciência da Computação.

### Links úteis ao trabalhar com LaTeX

- [Gerador de Tabelas](https://www.tablesgenerator.com/)
- [Fórum TEX](https://tex.stackexchange.com/)
- [Documentação do Overleaf](https://www.overleaf.com/learn)
- [Guia de LaTeX](https://latex-tutorial.com/tutorials/)
- [Template TCC FGA-UnB](https://github.com/fga-unb/template-latex-tcc) - Provavelmente nosso trabalho se parecerá com isso :) .
- [Vídeo de como instalar o LaTeX no Windows](https://youtu.be/EYVUYopYgyA).

## 🛠️ Ferramentas auxiliares

[GNU Make](https://www.gnu.org/software/make/) - Utilizaremos o make para automatizar comandos grandes que podem
nos ajudar em alguns momento como formatar o código e remover arquivos desnecessários. Veja os exemplos abaixo.

- `make format` - formata o código.
- `make lint` - verifica se o código está formatado mas não aplica mudanças.
- `make clean` - apaga arquivos desnecessários gerados durante o build do PDF.

### Formatador de código

Para formatar o código LaTeX vamos utilizar o [tex-fmt](https://github.com/WGUNDERWOOD/tex-fmt),
ele nos ajudará a manter a sanidade do código, corrigindo identação e quebrando linhas muito compridas.

> O arquivo [tex-fmt.toml](tex-fmt.toml) na raíz do projeto é o arquivo de configuração dessa ferramenta.

Para executar o formatador basta executar o comando abaixo, ele irá procurar e formatar todos os arquivos `.tex`, `.bib`, `.cls` e `.sty` do projeto.

```shell
make format
```

> [!NOTE]
> Sempre antes de realizar um commit é import executar o formatador para garantir que está tudo certo,
> pois ao realizar um pull request para a branch principal, um workflow será executado para verificar se o código está formatado
> e caso não esteja, o check do workflow irá falhar.

### Extensão LaTeX Workshop

Vamos utilizar a extensão [LaTeX Workshop](https://github.com/James-Yu/LaTeX-Workshop) no VS Code para diversas coisas como geração automática do PDF, sugestão de código e umpouco mais.

> [!IMPORTANT]
> Como vamos gerar um PDF com fontes customizadas pela extensão no VS Code, precisamos configurar a variável [`latex-workshop.latex.recipes`](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#latex-recipes) no arquivo JSON de configuração do VS Code para usar o compilador compatível com fontes customizadas, como no seguinte exemplo:
> ```json
> "latex-workshop.latex.recipes": [
>   {
>     "name": "latexmk (xelatex)",
>     "tools": [
>       "xelatexmk"
>     ]
>   }
> ]
>```
