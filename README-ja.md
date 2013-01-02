kdconv
====================


DESCRIPTION
--------------------
kdconv は PDF を Kindle2/3、Sony Reader(PRS-350)で読みやすいサイズへ変換
する為のプログラムです。

Kindle2/3、Sony Reader では PDF を表示出来ますが、特にデータが画像として
埋め込まれたファイルの場合、サイズによっては綺麗に表示されないことがあり
ます。

このプログラムは、指定された PDF を Kindle2/3、Sony Reader に適したサイズ
へ変換し、視認性を高めた後、出力します。また、余白を取り除く機能やOCRによる
検索可能なテキストを自動で埋め込む事が出来ます。

出力されたファイルのサイズはオリジナルファイルよりも小さくなることから、
単一デバイスへ複数のファイルを格納する際にも便利です。


PLATFORM
--------------------
サポートしているOSは以下の通りです。

* Ubuntu 12.10

また Linux や FreeBSD での動作報告もいただいています。

サポートしているデバイスは以下の通りです。

* Sony Reader PRS-G1


PREPARATION
--------------------
このプログラムは、以下の外部プログラムへ依存しています。MacPorts などを用
いて path の通っているディレクトリへインストールしてください。

* ghostscript(9.06以上)
* ImageMagick(6.7.7-10以上)
* pdftk(1.44)
* Python(2.7)
   * pdfrw(0.1)
   * fpdf(1.7)
* perl(5.14.2)

外部プログラムのインストールが済んだらmake にてインストールを行います。

    $ sudo make install


USAGE
--------------------
foo.pdf を sonyreader 用に変換し bar.pdf として出力するには:

    $ kdconv foo.pdf bar.pdf

オプション指定など、その他細かな使い方は、同梱のマニュアルページを参照してください。


SPECIAL THANKS
--------------------
このスクリプトを作製元のMIYOKAWA , Nobuyoshi様に感謝を致します。

以下の方々から有益なご指摘やパッチを頂き、より使いやすいスクリプトにする
ことが出来ました。感謝いたします。

Noriaki Mitsunaga さん、@toplut さん、cinq さん。


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
