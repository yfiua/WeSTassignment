This is the pdflatex version of the LaTeX class for creating lecture assignments,
in the corporate design of the
[Institute for Web Science and Technologies (WeST)](http://west.uni-koblenz.de/).
Its style was adapted by Lukas from a template package that Leon sent him.

Packages that are excluded (not compatable or not needed):

- polyglossia
- fontspec
- unicode-math
- lualatex-math

## Usage

Have a look at the [example_assignment.tex](example_assignment.tex) file for how
to use this class.

Currently the code can be build using PdfLaTeX.
For compilation [latexmk](https://www.ctan.org/pkg/latexmk/) is recommended, if
you have it installed you just have to perform:

    git clone https://github.com/Institute-Web-Science-and-Technologies/WeSTassignment.git
    cd WeSTassignment
    latexmk

Of course you can also compile this class by calling `lualatex` manually.

## ToDo

There is a lot left to be done before this thing can be considered stable,
pull requests are always welcome.

Bugs:

- Have better example content.

Additional Features:

- Rename "sections" to "tasks" so you can better reference them.
