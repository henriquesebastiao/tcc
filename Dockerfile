FROM debian:12-slim

LABEL maintainer="Henrique Sebastião <contato@henriquesebastiao.com>"
LABEL version="0.1.0"
LABEL description="Docker image for compiling XeLaTeX documents"
LABEL licenses="GPL-3.0"
LABEL title="henriquesebastiao/xelatex"
LABEL source="https://github.com/henriquesebastiao/tcc/blob/main/Dockerfile"

ENV DEBIAN_FRONTEND="noninteractive"

RUN apt update && \
  apt-get install -y --no-install-recommends \
  #   ca-certificates \
  #   html2text \
  #   inotify-tools \
  make \
  texlive-xetex \
  texlive-lang-portuguese \
  texlive-lang-english \
  texlive-fonts-recommended \
  texlive-publishers \
  texlive-extra-utils \
  texlive-plain-generic \
  latexmk \
  xindy && \
  apt-get autoclean && apt-get --purge --yes autoremove && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /home/latex
