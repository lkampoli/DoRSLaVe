# Design of Rockets and Space Launch Vehicles

This repository hosts the lecture materials for my "Design of Rockets and Space
Launch Vehicles" courses (coded AERO3261) at The University of Sydney. Go to
[the main website](https://github.com/lkampoli/DoRSLaVe) to view the generated
website and slides.

To render these slides yourself, you'll need [Quarto](https://quarto.org) and
Python (e.g. the [Anaconda](https://www.anaconda.com/download) installation, or
similar).

Firstly, create a Python environment with all the packages from
`scripts/requirements.in` installed. E.g. with `conda` you can run:

```shell
conda create -n ai python=3.11
conda activate DoRSLaVe
pip install -r scripts/requirements.in
```

Also, in the command-line `cd` to the main directory and run:

```shell
quarto install extension andrie/reveal-auto-agenda
```

This is to automatically generate the `agenda' slides inside the reveal.js
slides (cf. [that extension's
docs](https://github.com/andrie/reveal-auto-agenda#readme)).

To generate the entire website and slides for the whole project, just run

```shell
quarto render
```

or more targeted versions for specific lectures, like

```shell
quarto render Lecture0/lecture0.qmd
```
