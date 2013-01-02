#!/usr/bin/python
# -*- coding:utf-8 -*-
from fpdf import FPDF
import argparse

parser = argparse.ArgumentParser(description='OCR text background pdf generator')
parser.add_argument('file',metavar='file',type=argparse.FileType('r'),help='input text file (character encode utf-8 only!)')
parser.add_argument('outfile',metavar='outfile',type=str,help='output text file')
parser.add_argument('fontpath',metavar='fontpath',type=str,help='pdf fonts file path')
parser.add_argument('fontname',metavar='fontname',type=str,help='pdf font name')
args = parser.parse_args()

lines2 = args.file.readlines()
ocrstring = ""
for line in lines2:
	ocrstring = ocrstring + line.strip()
args.file.close()
pdf=FPDF()
pdf.add_page()
pdf.add_font(args.fontname,'',args.fontpath,uni=True)
pdf.set_font(args.fontname)
pdf.write(5,ocrstring)
pdf.output(args.outfile,'F')
