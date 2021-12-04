"""
find a stable matching between of a group of men and a group of women with same size
where each member has a preference for his or her partner
"""

from __future__ import annotations
from typing import Dict, List, Optional, Set, Tuple, Any


class PersonBase:
    """
    a dating-orienated base class 

    assume: coupling happens between opposite sexes

    note: subclasses need to re-type-hint self.partner
    """

    genders = {'male', 'female'}
    partner: Any = None

    def __init__(self, id_number: int, gender: str) -> None:
        if gender.lower() not in self.genders:
            raise ValueError(f'{gender} is not a valid gender.')
        self.id_number = id_number
        self.gender = gender

    def __repr__(self) -> str:
        return f'{self.gender}: {self.id_number}'
    
    def is_single(self) -> bool:
        return (self.partner is None)
    
    def set_preference(self, preference: List[Any]) -> None:
        """most prefered to least prefered"""
        self.preference = tuple(preference)
        self._set_preference_score()
    
    def _set_preference_score(self) -> None:
        scores = [i for i in range(len(self.preference)+1, 0, -1)]
        self.preference_scores: Dict[Any, int] = dict(zip(self.preference, scores))
    
    def _score(self, person: Any) -> int:
        try:
            return self.preference_scores[person]
        except:
            raise KeyError(f'{person} is not in {self.gender} {self.id_number} \'s preference list.')
 
    def like(self, person: Any) -> bool:
        if self.partner is None:
            return True
        if self._score(person) > self._score(self.partner):
            return True
        return False
    
    def marry(self, person: Any) -> None:
        self.partner = person
        person.partner = self
    
    def divorce(self) -> Any:
        if not self.partner:
            raise ValueError(f'{self.gender} {self.id_number} has no partner to divorce.')
        ex_partner = self.partner
        self.partner = None
        ex_partner.partner = None
        return ex_partner


class Man(PersonBase):
    def __init__(self, id_number: int, gender: str = 'male') -> None:
        super().__init__(id_number, gender)
        self.proposed_women: Set[Woman] = set()
        self.partner: Optional[Woman] = None
    
    def has_proposed(self, w: Woman) -> bool:
        return (w in self.proposed_women)
    
    def add_proposed(self, w: Woman) -> None:
        self.proposed_women.add(w)
    

class Woman(PersonBase):
    def __init__(self, id_number: int, gender: str = 'female') -> None:
        super().__init__(id_number, gender)
        self.partner: Optional[Man] = None
    
    
def stable_matching(men: List[Man], women: List[Woman]) -> List[Tuple[Man, Woman]]:
    """return a stable matching"""
    while men:
        man = men.pop()
        for woman in man.preference:
            if man.has_proposed(woman):
                continue
            man.add_proposed(woman)
            if woman.is_single():
                woman.marry(man)
            elif woman.like(man):
                ex_husband = woman.divorce()
                men.append(ex_husband)
                woman.marry(man)
            else:
                men.append(man)
    return [(w.partner, w) for w in women if w.partner]
