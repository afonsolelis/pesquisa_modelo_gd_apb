.PHONY: pdf clean

TEX=tese

pdf:
	# Usa latexmk para orquestrar múltiplas passagens e BibTeX
	latexmk -pdf -interaction=nonstopmode -halt-on-error -bibtex $(TEX).tex

clean:
	latexmk -C $(TEX).tex
	rm -f $(TEX).bbl $(TEX).blg $(TEX).out $(TEX).toc

