# -*- coding: utf-8 -*-
import unittest

from legacy_gilded_rose import LegacyGildedRose
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def setup_items(self):
        return [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49
            ),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]

    def test_no_regression(self):
        items = self.setup_items()

        gilded_rose = GildedRose(items)
        for day in range(7):
            gilded_rose.update_quality()

        names = [item.name for item in items]
        sell_ins = [item.sell_in for item in items]
        qualities = [item.quality for item in items]

        # PRINTED RESULT OF TEXTTEST_FIXTURE (Param used : 7)
        # -------- day 7 --------
        # name, sellIn, quality
        # +5 Dexterity Vest, 3, 13
        # Aged Brie, -5, 12
        # Elixir of the Mongoose, -2, 0
        # Sulfuras, Hand of Ragnaros, 0, 80
        # Sulfuras, Hand of Ragnaros, -1, 80
        # Backstage passes to a TAFKAL80ETC concert, 8, 29
        # Backstage passes to a TAFKAL80ETC concert, 3, 50
        # Backstage passes to a TAFKAL80ETC concert, -2, 0
        # Conjured Mana Cake, -4, 0

        self.assertEqual(
            names,
            [
                "+5 Dexterity Vest",
                "Aged Brie",
                "Elixir of the Mongoose",
                "Sulfuras, Hand of Ragnaros",
                "Sulfuras, Hand of Ragnaros",
                "Backstage passes to a TAFKAL80ETC concert",
                "Backstage passes to a TAFKAL80ETC concert",
                "Backstage passes to a TAFKAL80ETC concert",
                "Conjured Mana Cake",
            ],
        )
        self.assertEqual(sell_ins, [3, -5, -2, 0, -1, 8, 3, -2, -4])
        self.assertEqual(qualities, [13, 12, 0, 80, 80, 29, 50, 0, 0])

        for day in range(8):
            gilded_rose.update_quality()

        names = [item.name for item in items]
        sell_ins = [item.sell_in for item in items]
        qualities = [item.quality for item in items]

        # PRINTED RESULT OF TEXTTEST_FIXTURE (Param used : 15)
        # -------- day 15 --------
        # name, sellIn, quality
        # +5 Dexterity Vest, -5, 0
        # Aged Brie, -13, 28
        # Elixir of the Mongoose, -10, 0
        # Sulfuras, Hand of Ragnaros, 0, 80
        # Sulfuras, Hand of Ragnaros, -1, 80
        # Backstage passes to a TAFKAL80ETC concert, 0, 50
        # Backstage passes to a TAFKAL80ETC concert, -5, 0
        # Backstage passes to a TAFKAL80ETC concert, -10, 0
        # Conjured Mana Cake, -12, 0

        self.assertEqual(
            names,
            [
                "+5 Dexterity Vest",
                "Aged Brie",
                "Elixir of the Mongoose",
                "Sulfuras, Hand of Ragnaros",
                "Sulfuras, Hand of Ragnaros",
                "Backstage passes to a TAFKAL80ETC concert",
                "Backstage passes to a TAFKAL80ETC concert",
                "Backstage passes to a TAFKAL80ETC concert",
                "Conjured Mana Cake",
            ],
        )
        self.assertEqual(sell_ins, [-5, -13, -10, 0, -1, 0, -5, -10, -12])
        self.assertEqual(qualities, [0, 28, 0, 80, 80, 50, 0, 0, 0])

    # - At the end of each day our system lowers both values for every item
    def test_default_item_quality_decays_by_one_every_day(self):
        items = [Item("Default Item", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)

    def test_default_item_sell_in_decays_by_one_every_day(self):
        items = [Item("Default Item", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].sell_in)

    # - The Quality of an item is never more than 50
    def test_quality_never_more_than_50(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    # - The Quality of an item is never negative
    def test_quality_never_negative(self):
        items = [Item("Default Item", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    # - Once the sell by date has passed, Quality degrades twice as fast
    def test_default_item_quality_degrades_twice_as_fast_after_sell_by_date(self):
        items = [Item("Default Item", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    # - "Aged Brie" actually increases in Quality the older it gets
    #   -> increases twice when sell_in < 0, inferred by legacy code review
    def test_aged_brie_quality_increases_as_it_ages(self):
        items = [Item("Aged Brie", 2, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)

    def test_aged_brie_quality_increases_twice_after_sell_by_date(self):
        items = [Item("Aged Brie", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)

    # - "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    def test_sulfuras_no_sell_in_no_quality_decrease(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        for day in range(7):
            gilded_rose.update_quality()
            self.assertEqual(0, items[0].sell_in)
            self.assertEqual(80, items[0].quality)

    # - "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
    # Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    # Quality drops to 0 after the concert
    def test_backstage_quality_increases_as_it_ages(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)

    def test_backstage_quality_increases_by_2_under_10_days_of_sell_in(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)

    def test_backstage_quality_increases_by_3_under_5_days_of_sell_in(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)

    def test_backstage_quality_is_0_after_sell_by_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    # - "Conjured" items degrade in Quality twice as fast as normal items
    def test_conjured_quality_degrades_twice_as_fast_as_default_item(self):
        items = [Item("Conjured Item", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

    def test_conjured_quality_degrades_four_times_as_fast_after_sell_by_date(self):
        items = [Item("Conjured Item", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)


if __name__ == "__main__":
    unittest.main()
