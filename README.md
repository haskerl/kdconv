kdconv
====================

DESCRIPTION
--------------------

kdconv is a program for converting a PDF document into a Kindle and/or
Sony Reader(PRS-G1) friendly format.

Kindle2/3 and Sony Reader can display PDF documents, but, especially if
the documents holds data as image format, these devices are hard to
display it with good readability.

This program converts a PDF document into Kindle2/3 or Sony Reader
friendly paper size and improves readability.Also, you can automatically
 embed searchable text by OCR features and to remove the margin.

Usually these processes reduce file-size, so you can store more documents
into your device.


PLATFORM
--------------------
This program will run on:

* Ubuntu 12.10

Some users report me they can run it on Linux and/or FreeBSD.

This program supports these devices:

* Sony Reader PRS-G1

PREPARATION
--------------------
This program depends on below programs.  Please install them into a
directory where in your PATH with using MacPorts so on.

* ghostscript(9.06 higher)
* ImageMagick(6.7.7 higher)
* pdftk(1.44)
* Python(2.7)
   * pdfrw(0.1)
   * fpdf(1.7)
* perl(5.14.2)

After finishing installing related programs,you'd like to install:

    $ sudo make install


USAGE
--------------------
Convert foo.pdf to bar.pdf for SonyReader:

    $ kdconv foo.pdf bar.pdf

See manual pages which is included this package for more details and/or
available options.


SPECIAL THANKS
--------------------
We like to thank the original MIYOKAWA Nobuyoshi prepared this script.
I appreciate follow people who contribute useful information and/or
patch for enhancing script.

Noriaki Mitsunaga-san, @toplut-san, cinq-san.

AUTHOR
--------------------
Shin HATTORI
* E-Mail: toplut@gmail.com

MIYOKAWA, Nobuyoshi

* E-Mail: n-miyo@tempus.org
* Twitter: nmiyo
* Blog: http://blogger.tempus.org/


COPYRIGHT
--------------------
Copyright (c) 2012-2013 Shin HATTORI. All rights reserved.
Copyright (c) 2010-2011 MIYOKAWA, Nobuyoshi.  All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHORS ''AS IS'' AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
