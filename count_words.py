from dataclasses import dataclass
import regex

@dataclass
class OneWordStatistics:
    total_count: int
    counts_by_line: list[int]

WordStatistics = dict[str, OneWordStatistics]

def count_words(text: str) -> WordStatistics:
    results: WordStatistics = {}

    # Не уверен надо ли по ТЗ, но хочется не учитывать знаки препинания
    # Поэтому регулярка вместо split()
    word_regex = regex.compile('[[:alpha:]]+')

    lines = text.splitlines()
    for line_number, line in enumerate(lines):
        words = word_regex.findall(line)
        for word_with_case in words:
            word = word_with_case.lower()

            results.setdefault(word, OneWordStatistics(0, [0] * len(lines)))
            
            results[word].total_count += 1
            results[word].counts_by_line[line_number] += 1

    return results
