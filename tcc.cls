\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{tcc}

\LoadClass[12pt]{article}

\RequirePackage[brazil]{babel}
\RequirePackage{changepage}
\RequirePackage{csquotes}
\RequirePackage{fontspec}
\RequirePackage[a4paper, left=3cm, right=2.5cm, top=3cm, bottom=2cm]{geometry}
\RequirePackage[hyphens]{url}
\RequirePackage[
  pdfauthor={
    Emanuel Chagas Pinheiro Mattos,
    Henrique Sebastião da Silva Rosa,
    Lucas Sousa de Deus,
    Valério Gonçalves Vieira Jr.,
    Wanderson Amorim Pinheiro,
  },
  pdftitle={Desenvolvimento De Um Sistema De Comunicação Com
  Criptografia De Ponta A Ponta},
  pdfsubject={Trabalho de Curso para obtenção do título de graduação
  em Ciência da Computação apresentado à Universidade Paulista},
  pdfkeywords={criptografia, comunicação, privacidade,
  desenvolvimento, software},
  pdfproducer={Latex with hyperref},
  pdfcreator={xelatex},
]{hyperref}
\RequirePackage[none]{hyphenat}
\RequirePackage{indentfirst}
\RequirePackage[utf8]{inputenc}
\RequirePackage{microtype}
\RequirePackage{sectsty}
\RequirePackage{setspace}
\RequirePackage{tocloft}
\RequirePackage[xindy, toc, section=section]{glossaries}
\RequirePackage[alf, abnt-full-initials=yes, abnt-emphasize=bf]{abntex2cite}
\RequirePackage[nottoc,notlot,notlof]{tocbibind}
\RequirePackage{etaremune}
\RequirePackage{enumitem}
\RequirePackage[printonlyused, withpage]{acronym}
\RequirePackage{titlesec}
\RequirePackage[flushmargin]{footmisc}
\RequirePackage{graphicx}
\RequirePackage{float}

% Configurações
\setmainfont{times-new-roman}[
  Path = ./fontes/,
  UprightFont = *-regular,
  BoldFont = *-bold,
  ItalicFont = *-italic,
  BoldItalicFont = *-bolditalic,
]
\setstretch{1.5}
\setlength{\parindent}{1.25cm}
\pagestyle{myheadings}
\sectionfont{\fontsize{12}{15}\selectfont}

% Renomeia e formata o título do sumário
\addto\captionsbrazil{\renewcommand{\contentsname}{\textbf{SUMÁRIO}}}
\renewcommand{\cfttoctitlefont}{\hfil}

% Renomeia e formata o título da seção de referências
\addto\captionsbrazil{\renewcommand{\refname}{\hfil REFERÊNCIAS}}

% Renomeia e formata o título da seção de lista de figuras
\addto\captionsbrazil{\renewcommand\listfigurename{\hfil LISTA DE FIGURAS}}

% Configura identação dos itens do sumário
\cftsetindents{section}{0em}{3em}
\cftsetindents{subsection}{0em}{3em}
\cftsetindents{subsubsection}{0em}{3em}

\titleformat*{\section}{\large\bfseries}
\titleformat*{\subsection}{\large\bfseries}
\titleformat*{\subsubsection}{\large\bfseries}
\titleformat*{\paragraph}{\large\bfseries}
\titleformat*{\subparagraph}{\large\bfseries}

% Modo de alterar espaçamento acima e abaixo dos subtítulos:
% \titlespacing*{\section} {0pt}{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}
% \titlespacing*{\subsection} {0pt}{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}

% Adiciona linhas com pontos ao sumário
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}

\addtolength{\footnotesep}{2mm}

\hypersetup{
  colorlinks,
  citecolor=blue,
  filecolor=black,
  linkcolor=black,
  urlcolor=black
}

% Carrega e configura glossário
\makeglossaries
\loadglsentries{glossario}
\setglossarystyle{list}
\setlist[description]{leftmargin=0pt}
