# MergePDF
## Nicholas J. Kinar

## What is it?

This is a *very* simple utility written in `python 3` that will merge PDF files
on the command line.  It is easy to use and doesn't require much configuration.
There are more complex tools out there for more complex work with PDFs. This
is just an easy utility to use.

Although simple, I use this script for

Binaries be generated for Mac OS X, Windows and Linux using the
Powershell `build.ps1` script.

## Getting Started
* Use the binaries provided by this project (download under [releases](https://github.com/nkinar/MergePDF/releases) above).

*or*

* Add `mpdf.py` to your path and ensure that `python 3` and `PyPDF2` are installed.

>In the first place, I think there's going to be more and more *merging* of art and science. Scientists are already studying the creative process, and I think the whole line between art and science will break down and that scientists, I hope, will become more creative and writers more scientific. And I see no reason why the artistic world can't absolutely *merge* with Madison Avenue. Pop art is a move in that direction. Why can't we have advertisements with beautiful words and beautiful images?

> William S. Burroughs

![Photo](merge.jpg)

Photo by [pine watt](https://unsplash.com/@pinewatt?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/)


## USAGE

For Mac OS X or Windows, the binary or the script can be added to your `PATH`.

Using a binary:

```
mpdf [file1] [file2] ... [output filename]
```

or to run as a `python3` script:

```
python3 mpdf.py [file1] [file2] ... [output filename]
```

Alternately, to run directly from the command line:

```
mpdf.py [file1] [file2] ... [output filename]
```

## EXAMPLE
Suppose that you have three PDF files in a directory.  To merge all of them
into `out.pdf` use the following command:

```
mpdf 1.pdf 2.pdf 3.pdf out.pdf
```
That's all, folks!

## Authors
* **Nicholas J. Kinar**

## Built With
* python 3
* PyPDF2
* Pyinstaller
