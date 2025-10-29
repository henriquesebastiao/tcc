# Desenvolvimento de um Sistema de Comunicação com Criptografia de Ponta a Ponta

[![Build PDF](https://github.com/henriquesebastiao/tcc/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/henriquesebastiao/tcc/actions/workflows/build-pdf.yml)
[![Lint](https://github.com/henriquesebastiao/tcc/actions/workflows/lint.yml/badge.svg)](https://github.com/henriquesebastiao/tcc/actions/workflows/lint.yml)
[![GitHub License](https://img.shields.io/github/license/henriquesebastiao/tcc?color=blue)](https://github.com/henriquesebastiao/tcc/blob/main/LICENSE)
[![Visitors](https://api.visitorbadge.io/api/visitors?path=henriquesebastiao%2Ftcc&label=repository%20visits&countColor=%231182c3&style=flat)](https://github.com/henriquesebastiao/tcc)

> Trabalho de Conclusão de Curso (TCC) do curso de Ciência da Computação

## 📖 Sobre o Projeto

Este repositório contém o Trabalho de Conclusão de Curso desenvolvido como requisito para a obtenção do grau de Bacharel em Ciência da Computação. O trabalho aborda o desenvolvimento de um sistema de comunicação digital que utiliza **criptografia de ponta a ponta (E2EE)** para garantir a privacidade e a segurança das mensagens trocadas entre os usuários.

### 🎯 Tema

**Desenvolvimento de um Sistema de Comunicação com Criptografia de Ponta a Ponta**

Em um cenário marcado por crescentes preocupações com a proteção de dados pessoais e a vigilância digital, soluções que asseguram a confidencialidade das comunicações tornam-se cada vez mais relevantes. Este projeto apresenta uma solução prática e acessível para comunicação segura, utilizando técnicas modernas de criptografia.

### 🔍 Contexto e Motivação

Com o crescimento vertiginoso das interações online e o aumento de crimes cibernéticos, vazamentos de dados e fraudes, surge a necessidade de sistemas que priorizem a segurança e privacidade do usuário final. O projeto foi motivado por:

- **Vulnerabilidades cibernéticas**: Ataques como "Man-in-the-Middle" têm comprometido dados de milhões de usuários
- **Importância da privacidade**: A comunicação digital precisa garantir confidencialidade e autenticidade
- **Software livre**: Possibilitar que qualquer pessoa audite o código-fonte e verifique a segurança da aplicação

### 🎯 Objetivos

**Objetivo Principal:**
Desenvolver um sistema de comunicação de software livre, utilizando um modelo híbrido de criptografia simétrica e assimétrica para assegurar a privacidade na troca de mensagens, além da implementação do não repúdio, garantindo a autenticidade da comunicação.

**Objetivos Específicos:**
- Implementar criptografia híbrida utilizando algoritmos RSA (assimétrica) e AES (simétrica)
- Desenvolver arquitetura cliente-servidor com protocolo WebSocket para comunicação em tempo real
- Implementar o conceito de Perfect Forward Secrecy (PFS) para garantir sigilo efêmero
- Criar interface amigável ao usuário
- Realizar testes de segurança e usabilidade

### 🛠️ Tecnologias Utilizadas

O sistema foi desenvolvido utilizando tecnologias modernas e amplamente adotadas:

- **Linguagem**: Python
- **Protocolo de Comunicação**: WebSocket (comunicação bidirecional em tempo real)
- **Criptografia**: 
  - RSA (2048 bits) para troca segura de chaves
  - AES (256 bits) para criptografia de mensagens
  - Perfect Forward Secrecy (PFS) para sigilo efêmero
- **Bibliotecas**: Cryptography, Typer, Flask
- **Frontend**: HTML, CSS, JavaScript

### 📊 Resultados e Contribuições

O projeto alcançou resultados significativos:

- ✅ **Sistema funcional**: Plataforma operacional de troca de mensagens com criptografia E2EE
- ✅ **Segurança robusta**: Implementação de PFS garante que chaves comprometidas não afetam sessões anteriores
- ✅ **Arquitetura eficiente**: Servidor intermediário apenas roteia mensagens, sem acesso ao conteúdo descriptografado
- ✅ **Código aberto**: Todo o código-fonte disponível para auditoria e contribuições
- ✅ **Documentação completa**: Trabalho acadêmico detalhando fundamentos teóricos e práticos

**Principais contribuições:**
- Disseminação do conhecimento sobre criptografia aplicada
- Demonstração prática de que é possível construir plataformas seguras mesmo com recursos limitados
- Reforço da importância da proteção da privacidade em sistemas de comunicação
- Material de referência para estudos futuros em segurança da informação

### 👥 Autores

- Emanuel Chagas Pinheiro Mattos
- Henrique Sebastião Silva Rosa
- Lucas Souza de Deus
- Valério Gonçalves Vieira Junior
- Wanderson Amorim Pinheiro

### 📄 Palavras-chave

Comunicação, Criptografia, Privacidade, Segurança, Desenvolvimento de Software, Python, E2EE, Perfect Forward Secrecy, WebSocket.

---

## 🚀 Como Utilizar este Repositório

Este repositório contém todo o código LaTeX necessário para compilar o documento do TCC em PDF. Abaixo, você encontrará informações sobre as ferramentas e pacotes utilizados.

### 🔗 Links úteis ao trabalhar com LaTeX

**Ferramentas e Geradores:**
- [Gerador de Tabelas](https://www.tablesgenerator.com/) - Crie tabelas LaTeX facilmente
- [Mathpix Snip](https://mathpix.com/) - Converta equações de imagens para LaTeX
- [Detexify](https://detexify.kirelabs.org/classify.html) - Encontre símbolos LaTeX desenhando-os
- [LaTeX Equation Editor](https://latexeditor.lagrida.com/) - Editor visual de equações

**Documentação e Tutoriais:**
- [Fórum TEX](https://tex.stackexchange.com/) - Comunidade para dúvidas sobre LaTeX
- [Documentação do Overleaf](https://www.overleaf.com/learn) - Tutoriais completos e exemplos
- [Guia de LaTeX](https://latex-tutorial.com/tutorials/) - Tutorial passo a passo
- [CTAN - Comprehensive TeX Archive Network](https://ctan.org/) - Repositório oficial de pacotes LaTeX
- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX) - Guia completo e colaborativo

**Templates e Referências:**
- [Template TCC FGA-UnB](https://github.com/fga-unb/template-latex-tcc) - Template de referência
- [AbnTeX2](https://www.abntex.net.br/) - Documentação sobre normas ABNT em LaTeX
- [Gallery Overleaf](https://www.overleaf.com/latex/templates) - Galeria de templates

**Instalação e Configuração:**
- [Vídeo de como instalar o LaTeX no Windows](https://youtu.be/EYVUYopYgyA)
- [TeX Live](https://tug.org/texlive/) - Distribuição LaTeX multiplataforma
- [MiKTeX](https://miktex.org/) - Distribuição LaTeX para Windows

### 📦 Pacotes LaTeX Utilizados

Abaixo está uma explicação dos principais pacotes LaTeX utilizados no documento e links para suas documentações oficiais:

**Configuração de Idioma e Codificação:**
- [babel](https://ctan.org/pkg/babel) - Define o idioma do documento (português brasileiro)
- [inputenc](https://ctan.org/pkg/inputenc) - Codificação do documento (conversão automática de acentos)
- [fontspec](https://ctan.org/pkg/fontspec) - Permite utilizar fontes customizadas do sistema (requer XeLaTeX ou LuaLaTeX)

**Formatação de Texto:**
- [microtype](https://ctan.org/pkg/microtype) - Melhorias tipográficas e justificação do texto
- [indentfirst](https://ctan.org/pkg/indentfirst) - Indenta o primeiro parágrafo de cada seção
- [setspace](https://ctan.org/pkg/setspace) - Define o espaçamento entre linhas
- [hyphenat](https://ctan.org/pkg/hyphenat) - Controla a hifenização automática de palavras
- [csquotes](https://ctan.org/pkg/csquotes) - Formatação correta de aspas e citações

**Layout e Estrutura:**
- [geometry](https://ctan.org/pkg/geometry) - Ajusta o layout do documento e dimensões das margens
- [changepage](https://ctan.org/pkg/changepage) - Permite alterar margens em partes específicas do texto
- [sectsty](https://ctan.org/pkg/sectsty) - Define estilos para títulos de seções
- [titlesec](https://ctan.org/pkg/titlesec) - Personaliza tamanho de fonte e espaçamento de títulos e subtítulos

**Sumário e Listas:**
- [tocloft](https://ctan.org/pkg/tocloft) - Personaliza a aparência do sumário
- [tocbibind](https://ctan.org/pkg/tocbibind) - Adiciona referências e outros elementos ao sumário
- [enumitem](https://ctan.org/pkg/enumitem) - Controla formatação de listas e remove indentação
- [etaremune](https://ctan.org/pkg/etaremune) - Cria listas enumeradas em ordem decrescente

**Referências e Citações (ABNT):**
- [abntex2cite](https://ctan.org/pkg/abntex2) - Formata citações e referências de acordo com as normas ABNT

**Recursos Adicionais:**
- [hyperref](https://ctan.org/pkg/hyperref) - Cria links clicáveis no documento (referências internas e URLs)
- [glossaries](https://ctan.org/pkg/glossaries) - Gerencia glossário de termos técnicos
- [acronym](https://ctan.org/pkg/acronym) - Gera lista de acrônimos e siglas

> **Nota:** Para visualizar a lista completa de pacotes e suas configurações, consulte o arquivo `tcc.cls` no repositório.

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
>"latex-workshop.latex.tools": [
>        {
>            "name": "latexmk",
>            "command": "latexmk",
>            "args": [
>              "-synctex=1",
>              "-interaction=nonstopmode",
>              "-file-line-error",
>              "-pdfxe",
>              "-outdir=%OUTDIR%",
>              "%DOC%"
>            ],
>            "env": {}
>          },
>    ],
>    "latex-workshop.latex.recipes": [
>        {
>            "name": "latexmk (xelatex)",
>            "tools": [
>                "latexmk"
>            ]
>        },
>    ],
>```
