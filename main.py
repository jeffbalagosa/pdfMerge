from PyPDF2 import PdfMerger
import os

output_file_name = 'output/0_merged_output.pdf'

# merge all pdf files in the /input folder
merger = PdfMerger()
for filename in os.listdir('input'):
    if filename.endswith('.pdf'):
        merger.append('input/' + filename)

merger.write(output_file_name)
merger.close()
