# SOVCScraper

The data for the 2016 Larimer County General Election Statement of Votes Cast (SOVC) is available as a PDF. The PDF contains scanned images of document with the data. This directory and document serves as a place to experiment and take notes with scraping data from the PDF.

While there are several possible approaches the current method is as follows:

1. Rotate the PDF.
1. Convert the PDF to images, or scrape the images out of the PDF.
1. Use optical character recognition(OCR) 

## PDF To Image

We have been looking at two tools:

**Convert** - The convert program is a member of the ImageMagick(1) suite of tools. Use it to convert between image formats as well as resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and muchmore.

**PDFImages** - Portable Document Format (PDF) image extractor.

Not only are these conversion tools useful for turning the PDF into a series of images but they will be useful for preparing the images for OCR. 

## OCR

We primarily have been looking at `Tesseract` to conduct OCR.

