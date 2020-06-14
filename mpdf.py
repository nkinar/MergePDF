#!/usr/bin/env python3

"""
Copyright (c) 2020 Nicholas J. Kinar

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

"""
REFERENCES:
[1] https://stackoverflow.com/questions/3444645/merge-pdf-files
"""

from PyPDF2 import PdfFileMerger
import sys

PDF_EXT = '.pdf'


def print_usage():
    print('mpdf [file1] [file2] ... [output filename]')


def merge_pdfs(files, fn_out):
    if not fn_out.endswith('.pdf'):
        fn_out += PDF_EXT
    try:
        m = PdfFileMerger()
        for p in files:
            print('File: ' + p)
            m.append(p)
        m.write(fn_out)
        m.close()
        print('Output: ' + fn_out)
    except:
        print('An exception occurred, exiting...')


def main():
    if len(sys.argv) < 3:
        print_usage()
        return
    merge_pdfs(sys.argv[1:-1], sys.argv[-1])


if __name__ == '__main__':
    main()
