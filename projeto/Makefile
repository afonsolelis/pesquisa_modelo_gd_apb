.PHONY: pdf clean

TEX=tese

pdf:
	# Usa latexmk quando disponível; caso contrário, fallback para pdflatex/bibtex
	@if command -v latexmk >/dev/null 2>&1; then \
	  echo "[build] Usando latexmk"; \
	  latexmk -pdf -interaction=nonstopmode -halt-on-error -bibtex $(TEX).tex; \
	else \
	  echo "[build] latexmk não encontrado; usando pdflatex + bibtex"; \
	  pdflatex -interaction=nonstopmode -halt-on-error $(TEX).tex; \
	  if [ -f $(TEX).aux ]; then bibtex $(TEX); fi; \
	  pdflatex -interaction=nonstopmode -halt-on-error $(TEX).tex; \
	  pdflatex -interaction=nonstopmode -halt-on-error $(TEX).tex; \
	fi

clean:
	@if command -v latexmk >/dev/null 2>&1; then \
	  latexmk -C $(TEX).tex; \
	else \
	  echo "[clean] latexmk não encontrado; removendo artefatos padrão"; \
	fi
	rm -f $(TEX).aux $(TEX).bbl $(TEX).blg $(TEX).lof $(TEX).log $(TEX).lot $(TEX).out $(TEX).toc $(TEX).fls $(TEX).fdb_latexmk $(TEX).synctex.gz
