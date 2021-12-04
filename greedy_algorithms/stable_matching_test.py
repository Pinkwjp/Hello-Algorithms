from typing import List, Tuple
from random import shuffle
from unittest import TestCase, main

from algorithms_refined.greedy_algorithms.stable_matching import (
    PersonBase, Man, Woman, stable_matching)


class PersonTestCase(TestCase):  
    def test_is_single(self):
        w = PersonBase(id_number=111, gender='female')
        self.assertTrue(w.is_single())
    
    def test_marry(self):
        w = PersonBase(id_number=33, gender='female')
        m = PersonBase(id_number=3, gender='male')
        w.marry(m)
        self.assertFalse(w.is_single())
        self.assertFalse(m.is_single())
        self.assertEqual(w, m.partner)
        self.assertEqual(m, w.partner)
    
    def test_divorce(self):
        w = PersonBase(id_number=22, gender='female')
        m = PersonBase(id_number=2, gender='male')
        w.marry(m)
        ex_husband = w.divorce()
        self.assertEqual(ex_husband, m)
        self.assertTrue(w.is_single())
        self.assertTrue(m.is_single())
        
    def test_like(self):
        w = PersonBase(id_number=777, gender='female')
        men = [attractive, less_attractive] = [PersonBase(id_number=7, gender='male'), 
                                               PersonBase(id_number=17, gender='male')]
        w.set_preference(men)
        w.marry(attractive)
        self.assertFalse(w.like(less_attractive))
        w.divorce()
        w.marry(less_attractive)
        self.assertTrue(w.like(attractive))
    
    def test_score(self):
        w = PersonBase(id_number=777, gender='female')
        men = [PersonBase(id_number=7, gender='male'), 
               PersonBase(id_number=17, gender='male')]
        w.set_preference(men)
        another_man = PersonBase(id_number=0, gender='male')
        self.assertRaises(KeyError, w._score, another_man)


class ManTestCase(TestCase):
    def test_add_proposed(self):
        w1 = Woman(id_number=1)
        w2 = Woman(id_number=2)
        m = Man(id_number=999)
        m.add_proposed(w1)
        pairs = [(m.has_proposed(w1), True), (m.has_proposed(w2), False)]
        for i, (result, expected_result) in enumerate(pairs):
            with self.subTest(f'iteration {i}'):
                self.assertEqual(result, expected_result)
    
    def test_like(self):
        m = Man(id_number=999)
        w1 = Woman(id_number=1)
        w2 = Woman(id_number=2)
        m.set_preference([w1, w2]) # [most-prefered ,..., least-prefered]
        m.marry(w2)
        self.assertTrue(m.like(w1))
        m.marry(w1)
        self.assertFalse(m.like(w1))
        m.divorce()
        self.assertTrue(m.like(w2))


class WomanTestCase(TestCase):  
    def test_is_single(self):
        w = Woman(id_number=111)
        self.assertTrue(w.is_single())
    
    def test_marry(self):
        w = Woman(id_number=33)
        m = Man(id_number=3)
        w.marry(m)
        self.assertFalse(w.is_single())
    
    def test_divorce(self):
        w = Woman(id_number=22)
        m = Man(id_number=2)
        w.marry(m)
        ex_husband = w.divorce()
        self.assertTrue(w.is_single())
        self.assertIsInstance(ex_husband, Man)
    
    def test_like(self):
        w = Woman(id_number=777)
        men = [attractive_man, less_attractive_man] = [Man(id_number=7), Man(id_number=17)]
        w.set_preference(men)
        w.marry(attractive_man)
        self.assertFalse(w.like(less_attractive_man))
        w.divorce()
        w.marry(less_attractive_man)
        self.assertTrue(w.like(attractive_man))


def is_stable(matching: List[Tuple[Man, Woman]]) -> bool:
    for (man, woman) in matching:
        for (other_man, other_woman) in matching:
            if (man, woman) is (other_man, other_woman):
                continue
            unstable_marriage = ((man.like(other_woman) and other_woman.like(man)) or
                                 (other_man.like(woman) and woman.like(other_man)))
            if unstable_marriage:
                return False
    return True 


class IsStableTestCase(TestCase):
    def test_not_stable(self):
        men = [m1, m2] = [Man(id_number=1), Man(id_number=2)]
        women = [w1, w2] = [Woman(id_number=1), Woman(id_number=2)]
        for m in men:
            m.set_preference(women)
        for w in women:
            w.set_preference(men)
        w1.marry(m2)
        w2.marry(m1)
        couples = [(m2, w1), (m1, w2)]
        self.assertFalse(is_stable(matching=couples))

    def test_stable(self):
        men = [m1, m2] = [Man(id_number=1), Man(id_number=2)]
        women = [w1, w2] = [Woman(id_number=1), Woman(id_number=2)]
        for m in men:
            m.set_preference(women)
        for w in women:
            w.set_preference(men)
        w1.marry(m1)
        w2.marry(m2)
        couples = [(m1, w1), (m2, w2)]
        self.assertTrue(is_stable(matching=couples))


class StableMatchingTestCase(TestCase):
    def test_random_preference(self):
        pair_number = 8
        men = [Man(id_number=i) for i in range(pair_number)]
        women = [Woman(id_number=i) for i in range(pair_number)]
        for m in men:
            w_preference = list(women)
            shuffle(w_preference)
            m.set_preference(preference=w_preference)
        for w in women:
            m_preference = list(men)
            shuffle(m_preference)
            w.set_preference(preference=m_preference)
        couples = stable_matching(men=men, women=women)
        self.assertTrue(is_stable(matching=couples))

    def test_men_with_same_preference(self):
        pair_number = 8
        men = [Man(id_number=i) for i in range(pair_number)]
        women = [Woman(id_number=i) for i in range(pair_number)]
        for m in men:
            m.set_preference(preference=list(women))
        for w in women:
            m_preference = list(men)
            shuffle(m_preference)
            w.set_preference(preference=m_preference)
        couples = stable_matching(men=men, women=women)
        self.assertTrue(is_stable(matching=couples))
    
    def test_men_women_with_same_preference(self):
        pair_number = 8
        men = [Man(id_number=i) for i in range(pair_number)]
        women = [Woman(id_number=i) for i in range(pair_number)]
        shuffle(men)
        shuffle(women)
        for m in men:
            m.set_preference(preference=list(women))
        for w in women:
            w.set_preference(preference=list(men))
        couples = stable_matching(men=men, women=women)
        self.assertTrue(is_stable(matching=couples))


if __name__ == '__main__':
    main()