This is the pdflatex version of the LaTeX class for creating lecture assignments,
in the corporate design of the
[Institute for Web Science and Technologies (WeST)](http://west.uni-koblenz.de/).
Its style was adapted by Lukas from a template package that Leon sent him.
The pdflatex version was adapted by Jun from the lualatex version,
and is about 30% faster.

Packages that are excluded (not compatible or not needed):

- `polyglossia`
- `fontspec`
- `unicode-math`
- `lualatex-math`

## Usage

Have a look at the exemplary [assignment.tex](assignment.tex) file for how
to use this class.

Use
    
    %solution-start
    stuffs that you do not want students to see
    %solution-end
    
to mark your solutions. You don't need to manually create the .tex file for students.

Put the dependencies into [dep.assignment](dep.assignment) and
[dep.assignment-for-students](dep.assignment-for-students).

## Compilation

For compilation [Stu](https://github.com/kunegis/stu) is recommended, if
you have it installed you just have to perform:

    stu

Stu generates three files automatically:

- `assignment.pdf`: PDF with solutions
- `assignment-for-students.pdf`: PDF without solutions
- `assignment_X.zip`: uploadable zipball for students

Of course you can also compile this class by calling `pdflatex` manually.

    pdflatex assignment.tex

## ToDo

There is a lot left to be done before this thing can be considered stable,
pull requests are always welcome.

Additional Features:

- Rename "sections" to "tasks" so you can better reference them.
