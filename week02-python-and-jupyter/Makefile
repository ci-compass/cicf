NOTEBOOKS = 1-introduction.ipynb 2-quick-python-tour.ipynb 3-python-packages.ipynb 4-plot-ligo-data.ipynb

all: $(NOTEBOOKS)

%.ipynb: qmd/%.qmd
	quarto convert $< --output $@
