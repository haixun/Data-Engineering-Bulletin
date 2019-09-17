# Makefile for LaTeX files

LATEX	= pdflatex
BIBTEX	= bibtex
MAKEINDEX = makeindex

RERUN = "(There were undefined references|Rerun to get (cross-references|the bars) right)"
RERUNBIB = "No file.*\.bbl|Citation.*undefined"
MAKEIDX = "^[^%]*\\makeindex"
MPRINT = "^[^%]*print"
USETHUMBS = "^[^%]*thumbpdf"

SRC	:= $(shell egrep -l '^[^%]*\\begin\{document\}' *.tex)
BIBFILE := $(shell perl -ne '($$_)=/^[^%]*\\bibliography\{(.*?)\}/;@_=split /,/;foreach $$b (@_) {print "$$b.bib "}' $(SRC))

PDFPICS := $(shell perl -ne '@foo=/^[^%]*\\(includegraphics)(\[.*?\])?\{(.*?)\}/g;if (defined($$foo[2])) { if ($$foo[2] =~ /.pdf$$/) { print "$$foo[2] "; } else { print "$$foo[2].pdf "; }}' *.tex)
DEP	= *.tex

TRG	= $(SRC:%.tex=%.pdf)

COPY = if test -r $(<:%.tex=%.toc); then cp $(<:%.tex=%.toc) $(<:%.tex=%.toc.bak); fi 
RM = rm -f
OUTDATED = echo "EPS-file is out-of-date!" && false


all 	: $(TRG)

define run-latex
	  $(COPY);$(LATEX) $<
	  egrep -q $(MAKEIDX) $< && ($(MAKEINDEX) $(<:%.tex=%);$(COPY);$(LATEX) $<) ; true
	  egrep -c $(RERUNBIB) $(<:%.tex=%.log) && ($(BIBTEX) $(<:%.tex=%);$(COPY);$(LATEX) $<) ; true
	  egrep -q $(RERUN) $(<:%.tex=%.log) && ($(COPY);$(LATEX) $<) ; true
	  egrep -q $(RERUN) $(<:%.tex=%.log) && ($(COPY);$(LATEX) $<) ; true
	  if cmp -s $(<:%.tex=%.toc) $(<:%.tex=%.toc.bak); then true ;else $(LATEX) $< ; fi
	  $(RM) $(<:%.tex=%.toc.bak)
	  # Display relevant warnings
	  egrep -i "(Reference|Citation).*undefined" $(<:%.tex=%.log) ; true
endef

$(TRG)	: %.pdf : %.tex $(DEP) $(PDFPICS) $(BIBFILE)
	  @$(run-latex)

clean	:
	  -rm -f $(TRG) $(PSF) $(PDF) $(TRG:%.pdf=%.aux) $(TRG:%.pdf=%.bbl) $(TRG:%.pdf=%.blg) $(TRG:%.pdf=%.log) $(TRG:%.pdf=%.out) $(TRG:%.pdf=%.dvi) $(TRG:%.pdf=%.synctex.gz)

.PHONY	: all show clean ps pdf showps stylecheck spellcheck

view:
	acroread $(PDF)

osx:
	open $(PDF)

combined:
	pdfunite cover.pdf storage.pdf combined.pdf

# Check style:
stylecheck:
	printf "weasel words: "
	sh ./scripts/weasel *.tex
	printf "\npassive voice: "
	sh ./scripts/passive *.tex
	printf "\nduplicates: "
	perl ./scripts/dups *.tex
	printf "\ndone\n"

# Check spelling with aspell
spellcheck:
	find . -name "*.tex" -exec aspell --lang=en --mode=tex --dont-suggest --personal=./.aspell.en.pws check "{}" \;

######################################################################
# Define rules for PDF source files.
%.pdf: %.eps
	epstopdf $< > $(<:%.eps=%.pdf)
