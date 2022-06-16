FILE = poc
$(FILE).pdf: $(FILE).tex header.tex abstract.tex intro.tex prelim.tex back.tex algo.tex evaluation.tex concl.tex related.tex
	pdflatex $(FILE)

newcite: refined.bib $(FILE).pdf 
	bibtex $(FILE)
	pdflatex $(FILE)
	pdflatex $(FILE)
	
force:
	pdflatex $(FILE)
	bibtex $(FILE)
	pdflatex $(FILE)
	pdflatex $(FILE)
	
clean:
	rm -f $(FILE).aux $(FILE).bbl $(FILE).blg $(FILE).dvi $(FILE).log $(FILE).pdf $(FILE).ps
