#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from optparse import OptionParser
from pdfrw import PdfReader, PdfWriter, IndirectPdfDict
import codecs

def PDF_string_encoding(unicode_string):
	return codecs.BOM_UTF16_BE + unicode_string.encode("utf-16be")

parser = OptionParser()
parser.add_option("-f","--file",dest="inputname",help="input file")
parser.add_option("-o","--output",dest="outputname",help="output file")
parser.add_option("-t","--title",dest="title",help="title name")
parser.add_option("-a","--author",dest="author",help="author name")
parser.add_option("-c","--creator",dest="creator",help="creator name")
parser.add_option("-s","--subject",dest="subject",help="subject")
(opts,args) = parser.parse_args()

inputs = opts.inputname
assert inputs
outfn = opts.outputname
assert outfn
writer = PdfWriter()
#for inpfn in inputs:
writer.addpages(PdfReader(inputs, decompress=False).pages)

writer.trailer.Info = IndirectPdfDict(
	Title = PDF_string_encoding(unicode(opts.title,encoding='utf-8')),
	Author = PDF_string_encoding(unicode(opts.author,encoding='utf-8')),
	Subject = PDF_string_encoding(unicode(opts.subject,encoding='utf-8')),
	Creator = PDF_string_encoding(unicode(opts.creator,encoding='utf-8')),
)
writer.write(outfn)
