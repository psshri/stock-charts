from pypdf import PdfMerger

pdfs = ['ohlc-charts/PDFs/output.pdf', 'ohlc-charts/PDFs/test1.pdf', 'ohlc-charts/PDFs/test2.pdf', 'ohlc-charts/PDFs/test3.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("ohlc-charts/PDFs/result.pdf")
merger.close()