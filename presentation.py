from count_words import WordStatistics
import xlsxwriter
import io

def word_counts_to_xlsx(data: WordStatistics) -> bytes:
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    worksheet.write(0, 0, 'Словоформа')
    worksheet.write(0, 1, 'Общее кол-во')
    worksheet.write(0, 2, 'Кол-во по строкам')

    for i, (word, word_data) in enumerate(data.items()):
        worksheet.write(i + 1, 0, word)
        worksheet.write(i + 1, 1, word_data.total_count)
        worksheet.write(i + 1, 2, ','.join(str(count) for count in word_data.counts_by_line))
    
    workbook.close()
    output.seek(0)
    return output.getvalue()
