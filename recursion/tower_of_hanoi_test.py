from unittest import TestCase, main

from tower_of_hanoi import Disk, Rod, move_disks, tower_of_hanoi


class DiskTestCase(TestCase):
    def setUp(self) -> None:
        self.all_disks = [Disk(size=i) for i in range(5)]

    def test_size(self) -> None:
        size = 0
        for disk in self.all_disks:
            with self.subTest():
                self.assertEqual(disk.size, size)
                size += 1

    def test_repr(self) -> None:
        for i in range(5):
            with self.subTest():
                disk = Disk(size=i)
                self.assertEqual(disk.__repr__(), f'Disk: {i}')
    
    def test_total_ordering(self) -> None:
        disk_a = Disk(1)
        disk_b = Disk(1)
        disk_c = Disk(2) 
        conditions = (disk_a == disk_b, 
                      disk_a >= disk_b,
                      disk_a <= disk_b,
                      disk_a < disk_c,

                      disk_b == disk_a, 
                      disk_b >= disk_a,
                      disk_b <= disk_a,
                      disk_b < disk_c,

                      disk_c > disk_a,
                      disk_c >= disk_a,
                      disk_c > disk_b,
                      disk_c >= disk_b)
        for condition in conditions:
            with self.subTest():
                self.assertTrue(condition)
    
    def test_eq_raise_error(self) -> None:
        disk = Disk(5)
        self.assertRaises(ValueError, disk.__eq__, 5)

    def test_lt_raise_error(self) -> None:
        disk = Disk(8)
        self.assertRaises(ValueError, disk.__lt__, 100)


class RodTestCase(TestCase):
    def test_repr_passing(self) -> None:
        rod = Rod()
        self.assertEqual(rod.__repr__(), f'Rod: []')
    
    def test_is_empty(self) -> None:
        rod = Rod()
        self.assertTrue(rod.is_empty())
    
    def test_add_disk(self) -> None:
        rod = Rod()
        for i in range(5, 1, -1):
            with self.subTest():
                rod.add_disk(Disk(i))
    
    def test_add_disk_raise_error(self) -> None:
        rod = Rod()
        rod.add_disk(Disk(1))
        self.assertRaises(ValueError, rod.add_disk, Disk(11))

    def test_pop_top_disk_raise_error(self) -> None:
        rod = Rod()
        self.assertRaises(ValueError, rod.pop_top_disk)
    
    def test_pop_top_disk(self) -> None:
        rod = Rod()
        rod.add_disk(Disk(5))
        self.assertEqual(rod.pop_top_disk(), Disk(5))


class HanoiTestCase(TestCase):
    def test_move_disks(self):
        A, B, C = (Rod() for _ in range(3))
        A.add_disk(Disk(2))
        A.add_disk(Disk(1))
        move_disks(2, A, B, C)
        self.assertEqual(C.get_disk_number(), 2)
    
    def test(self):
        tower_of_hanoi(num_disc=8)

if __name__ == '__main__':
    main()