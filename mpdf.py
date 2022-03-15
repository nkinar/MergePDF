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

import fitz
import sys
from tqdm import tqdm
PDF_EXT = '.pdf'


def print_usage():
    print('mpdf [file1] [file2] ... [output filename]')


def merge_pdfs(files, fn_out):
    if not fn_out.endswith(PDF_EXT):
        fn_out += PDF_EXT
    try:
        out_doc = fitz.open()
        for k in tqdm(range(len(files))):
            file = files[k]
            doc_in = fitz.open(file)
            out_doc.insert_pdf(doc_in)
            doc_in.close()
        out_doc.save(fn_out)
    except Exception as e:
        print(e)


def main():
    if len(sys.argv) < 3:
        print_usage()
        return
    merge_pdfs(sys.argv[1:-1], sys.argv[-1])


if __name__ == '__main__':
    main()
