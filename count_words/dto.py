from dataclasses import dataclass

@dataclass
class OneWordCounts:
    total_count: int
    counts_by_line: list[int]

WordCounts = dict[str, OneWordCounts]
