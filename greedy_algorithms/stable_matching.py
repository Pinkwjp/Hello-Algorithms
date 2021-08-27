"""
find the stable matchinig between two groups of men and women
where each member has a preference for each member in the other group
"""

from __future__ import annotations
from random import shuffle
from typing import List, Optional, Set, Tuple, Any


class Base():
    def __init__(self, id_num: int) -> None:
        self.id_num = id_num

    def set_preference(self, potential_partners: List[Any]) -> None:
        self.preference_list = list(potential_partners)
        shuffle(self.preference_list)


class Man(Base):
    def __init__(self, id_num: int) -> None:
        super().__init__(id_num)
        self.proposed_women: Set[Woman] = set()
    
    def set_preference(self, potential_partners: List[Woman]) -> None:
        super().set_preference(potential_partners)
        

class Woman(Base):
    def __init__(self, id_num: int) -> None:
        super().__init__(id_num)
        self.husband: Optional[Man1] = None 
    
    def set_preference(self, potential_partners: List[Man]) -> None:
        super().set_preference(potential_partners)
        self.preference_score = {man: score for (score, man)
                                in enumerate(self.preference_list)}


def stable_matching(num_pairs: int) -> List[Tuple[int, int]]:
    """return the stable matching pairs of man, woman"""
    # initialize
    men = [Man(id_num=i) for i in range(num_pairs)]
    women = [Woman(id_num=i) for i in range(num_pairs)]
    for man in men:
        man.set_preference(women)
    for woman in women: 
        woman.set_preference(men)
    # perform matching
    while men:
        m = men.pop() 
        for w in m.preference_list: 
            if w in m.proposed_women:
                continue
            m.proposed_women.add(w)
            h = w.husband
            # woman single?
            if h is None:
                w.husband = m
                break
            # choose one man
            else:
                if w.preference_score[m] > w.preference_score[h]:
                    w.husband = m
                    men.append(h) 
                    break
        # no match
        else: 
            men.append(m)
    # result
    pairs: List[Tuple[int, int]] = []
    for w in women:
        if m := w.husband:
            pairs.append((m.id_num, w.id_num))
    return pairs


# mypy stable_matching.py
if __name__ == '__main__':
    num_pairs = 5
    pairs = stable_matching(num_pairs)
    print(pairs)
