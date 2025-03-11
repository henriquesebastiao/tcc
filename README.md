# Trabalho de Curso - Ciência da Computação

Projeto de TCC para a graduação em Ciência da Computação.

### Links úteis ao trabalhar com LaTeX

- [Gerador de Tabelas](https://www.tablesgenerator.com/)
- [Fórum TEX](https://tex.stackexchange.com/)
- [Documentação do Overleaf](https://www.overleaf.com/learn)
- [Guia de LaTeX](https://latex-tutorial.com/tutorials/)
- [Template TCC FGA-UnB](https://github.com/fga-unb/template-latex-tcc) - provavelmente nosso trabalho se parecerá com isso :) .
- [Vídeo de como instalar o LaTeX no Windows](https://youtu.be/EYVUYopYgyA).

### 📦 Pacotes LaTeX usados

Uma breve explicação do que faz cada pacote adicionado ao arquivo `tcc.tex` e os links de referência para a documentação oficial do pacote:

- [babel](https://br.mirrors.cicku.me/ctan/macros/latex/required/babel/base/babel-code.pdf) - define o idioma do documento.
- [changepage](https://br.mirrors.cicku.me/ctan/macros/latex/contrib/changepage/changepage.pdf) - permite alterar a largura das margens de partes específicas do texto.
- [csquotes](https://br.mirrors.cicku.me/ctan/macros/latex/contrib/csquotes/csquotes.pdf) - para colocar texto entre aspas corretamente.
- [fontspec](https://linorg.usp.br/CTAN/macros/unicodetex/latex/fontspec/fontspec.pdf) - permite utilizar fontes customizadas (fontes do sistema).
- [geometry](https://linorg.usp.br/CTAN/macros/latex/contrib/geometry/geometry.pdf) - permite ajustar o layout do documento, definindo as dimensões das margens.
- [hyperref](https://linorg.usp.br/CTAN/macros/latex/contrib/hyperref/doc/hyperref-doc.pdf) - permite criar links clicáveis no documento.
- [hyphenat](https://linorg.usp.br/CTAN/macros/latex/contrib/hyphenat/hyphenat.pdf) - impede a hifenização automática das palavras no texto.
- [microtype](https://br.mirrors.cicku.me/ctan/macros/latex/contrib/microtype/microtype.pdf) - para melhorias de justificação do texto.
- [indentfirst](https://linorg.usp.br/CTAN/macros/latex/required/tools/indentfirst.pdf) - indenta o primeiro parágrafo de cada seção.
- [inputenc](https://br.mirrors.cicku.me/ctan/macros/latex/base/inputenc.pdf) - codificacao do documento (conversão automática dos acentos).
- [sectsty](https://br.mirrors.cicku.me/ctan/macros/latex/contrib/sectsty/sectsty.pdf) - usado para definir tamanho 12 para os títulos de seções.
- [setspace](https://br.mirrors.cicku.me/ctan/macros/latex/contrib/setspace/setspace-doc.pdf) - define o espaçamento entre linhas.
- [tocloft](https://br.mirrors.cicku.me/ctan/macros/latex/contrib/tocloft/tocloft.pdf) - permite personalizar a aparência do sumário.
- [abntex2cite](https://tug.ctan.org/macros/latex/contrib/abntex2/doc/abntex2cite.pdf) - formata citações e referências de acordo com a ABNT.
- [tocbibind](https://br.mirrors.cicku.me/ctan/macros/latex/contrib/tocbibind/tocbibind.pdf) - para adicionar as referências ao sumário.

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
