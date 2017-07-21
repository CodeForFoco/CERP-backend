#!/bin/bash
convert \
	-verbose	\
	-density 150	\
	-trim	\
	INSERTPDFHERE.pdf	\
	-quality 100	\
	-flatten	\
	-sharpen 0x1.0 \
	OUTIMAGEHERE.jpg
