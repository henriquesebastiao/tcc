#!/bin/bash

# Script simples para substituir capa no HTML
# Uso: ./replace_capa.sh <arquivo_html> [arquivo_saida]

if [ $# -lt 1 ]; then
    echo "Uso: $0 <arquivo_html> [arquivo_saida]"
    exit 1
fi

HTML_FILE="$1"
OUTPUT_FILE="${2:-$HTML_FILE}"
CAPA_FILE="capa.html"

# Verificar se arquivos existem
[ ! -f "$HTML_FILE" ] && echo "Erro: $HTML_FILE não encontrado" && exit 1
[ ! -f "$CAPA_FILE" ] && echo "Erro: $CAPA_FILE não encontrado" && exit 1

# Encontrar linhas de início e fim
START_LINE=$(grep -n "<p>Universidade Paulista - UNIP</p>" "$HTML_FILE" | head -1 | cut -d: -f1)
END_LINE=$(grep -n "<p><strong>RESUMO</strong></p>" "$HTML_FILE" | tail -1 | cut -d: -f1)

# Verificar se encontrou as linhas
[ -z "$START_LINE" ] && echo "Erro: início não encontrado" && exit 1
[ -z "$END_LINE" ] && echo "Erro: fim não encontrado" && exit 1

# Ajustar linha de fim para incluir fechamento
END_LINE=$((END_LINE + 2))

# Criar arquivo temporário
TEMP_FILE=$(mktemp)

# Fazer a substituição
sed -n "1,$((START_LINE - 1))p" "$HTML_FILE" > "$TEMP_FILE"
cat "$CAPA_FILE" >> "$TEMP_FILE"
sed -n "$((END_LINE - 2)),\$p" "$HTML_FILE" >> "$TEMP_FILE"

# Mover para arquivo final
mv "$TEMP_FILE" "$OUTPUT_FILE"