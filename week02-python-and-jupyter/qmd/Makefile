NOTEBOOKS = ../1-introduction.ipynb     \
           ../2-quick-python-tour.ipynb \
           ../3-python-packages.ipynb   \
           ../4-plot-ligo-data.ipynb

all: $(NOTEBOOKS)

../%.ipynb: %.qmd
	quarto convert $< --output $@

.PHONY: clean
clean:
	rm -f $(NOTEBOOKS)
	rm -f *.ipynb *.html
	rm -rf *_files
