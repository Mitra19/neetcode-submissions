from typing import List, Dict
from collections import defaultdict

def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:
    ans = {}
    for name, score in zip(names, scores):
        ans[name] = score
    return ans


# do not modify below this line
print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))
