# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            ItemWrapper(item).update()


class ItemWrapper:
    def __init__(self, item):
        self.item = item

    def update(self):
        if self.item.name == "Sulfuras, Hand of Ragnaros":
            return
        self.update_sell_in()
        self.update_quality()

    def update_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def update_quality(self):
        if self.item.name == "Aged Brie":
            self.increase_quality()
            if self.item.sell_in < 0:
                self.increase_quality()
        elif self.item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.increase_quality()
            if self.item.sell_in + 1 < 11:
                self.increase_quality()
            if self.item.sell_in + 1 < 6:
                self.increase_quality()
            if self.item.sell_in < 0:
                self.item.quality = self.item.quality - self.item.quality
        elif self.item.name.split()[0] == "Conjured":
            self.decrease_quality()
            self.decrease_quality()
            if self.item.sell_in < 0:
                self.decrease_quality()
                self.decrease_quality()
        else:
            self.decrease_quality()
            if self.item.sell_in < 0:
                self.decrease_quality()

    def increase_quality(self):
        if self.item.quality < 50:
            self.item.quality = self.item.quality + 1

    def decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
