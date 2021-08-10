from itertools import combinations


class Main:

    def __init__(self):

        self.min_support = 2
        self.confidence = 0.7
        self.k_item = 3

        self.data = [
            ["halo", "gta", "minecraft"],
            ["gear war", "gta", "call of"],
            ["halo", "gear war", "gta", "call of"],
            ["gear war", "call of"],
            ["halo", "gear war", "gta", "call of"],
 
        ]

        self.data = [
            ["I1", "I2", "I5"],
            ["I2", "I4"],
            ["I2", "I3"],
            ["I1", "I2", "I4"],
            ["I1", "I3"],
            ["I2", "I3"],
            ["I1", "I3"],
            ["I1", "I2", "I3", "I5"],
            ["I1", "I2", "I3"]
        ]


        self.scoring_item = {}


    def savegarding(self, data):
        """Savegarde itemset and list of item"""
        for k, v in data.items():
            self.scoring_item[k] = v


    def transform_data_to_horizontal(self):
        """Reverse data to item -> order"""

        [print(i) for i in self.data]
        print("")

        # Transform database in vertical data format.
        data_set = [item for line in self.data for item in line]
        itemset = {item: [] for item in sorted(set(data_set))}

        # Append TID coresponding to itemset.
        [itemset[item].append(f"T{index + 1}") for index, line in enumerate(self.data) for item in line]

        [print(k, v) for k, v in itemset.items()]
        print("")

        # Save dico score.
        self.savegarding(itemset)

        return itemset, data_set


    def intersection_of_items_first(self, data_set, itemset_dico, iteration):
        """Generate itemset of tuple with their order in common"""

        # First iteration. Transform item to doublon.
        data_set = sorted(list(set(data_set)))
        comb = sorted(set(list(combinations(data_set, iteration))))

        print(comb, "\n")

        data = {}
        for itemsets in comb:

            # Recuperate each item of the two itemset.
            liste = [i for item in itemsets for i in itemset_dico[item]]
            # Count them & filter them.
            liste = sorted([i for i in liste if liste.count(i) > 1])
            # Add to dictionnary.
            if len(liste) > self.min_support:
                data[itemsets] = sorted(set(liste))

        [print(k, v) for k, v in data.items()]

        # Save dico score
        self.savegarding(data)
 
        return data


    def intersection_of_items_other(self, data, itemset_dico, iteration):
        """Generate itemset of tuple with their order in common, len(tuple) > 1"""

        # Recuperate item on itemset.
        recuperate_to_matching = lambda k1, nb: tuple(list(k1)[:len(k1) - nb])


        print(iteration, "\n")
        [print(k, v) for k, v in data.items()]
        print("")

        # Recuperate the x line of the tree.
        # ex: (i1, i2), (i2, i3), (i1, i3) -> two branchs: (i1 & i2)
        to_combinate = {recuperate_to_matching(k1, 1): [] for k1, _ in data.items()}
        [to_combinate[recuperate_to_matching(k1, 1)].append(k1) for k1, _ in data.items()]
        to_combinate = {k: sorted(set([j for i in v for j in i])) for k, v in to_combinate.items() }

        print(to_combinate, "\n")


        container = []
        for k, v in to_combinate.items():

            # Make a combination of item of the branch.
            comb = sorted(set(list(combinations(v, iteration))))
            comb = [i for i in comb if recuperate_to_matching(i, 2) == k]
            print(comb, "\n")

            # For each tuple, recuperate length tuple - 1 item
            # (i1, i2) -> (i1) & (i2)
            # (i1, i2, i3) -> i3 & (i1, i2)
            #              -> i1 & (i3, i2)
 
            for line in comb:
                to_match = recuperate_to_matching(line, 1)

                for k, v in data.items():
  
                    if k == to_match:
                        not_in = tuple([i for i in line if i not in k])
                        not_in = not_in if len(not_in) > 1 else not_in[0]
                        container += [(line, not_in)]


        print("")
        [print(k, v) for k, v in self.scoring_item.items()]
        print("")

        # For each couple of tuple, recuperate their support.
        dico = {}
        for (item1, item2) in container:
            liste = self.scoring_item[recuperate_to_matching(item1, 1)] + self.scoring_item[item2]
            dico[item1] = {i: liste.count(i) for i in liste if liste.count(i) > 1}

        [print(k, v) for k, v in dico.items()]
        print("")

        # filtering it by the min support.
        dico = {k: v for k, v in dico.items() if len(v) >= self.min_support}

        [print(k, v) for k, v in dico.items()]
        print("")

        # Recuperate support.
        d = {k: [k1 for k1, v1 in v.items()] for k, v in dico.items()}

        # Save dico score
        self.savegarding(d)

        return d


    def support_data(self):
        """Recuperate support length of command / length of the support of the itemset"""

        support = {k if len(k) > 1 else k[0]: len(v) / len(self.data) for k, v in self.scoring_item.items()}
        [print(k, v) for k, v in support.items()]
        print("")


    def confidence_data(self):
        """Recuperate itemset, combination of the itemset, 
        and support length of itemset / support length combination of the itemset"""

        confidence = {}

        for k, v in self.scoring_item.items():
            k = k if len(k) > 1 else k[0]

            if type(k) == tuple:

                data = []
                for n in range(1, len(k)):
                    data += list(combinations(k, n))

                data = sorted(set(data))

                for i in data:
                    i = i if len(i) > 1 else i[0]

                    a = len(self.scoring_item[i])
                    b = len(self.scoring_item[k])

                    item = [j for j in k if j not in i]
                    r = [j for j in k if j not in item]

                    print(f"{r} -> {item} ==> { round(b / a, 2) }" )

            print("")


    def association_rules(self):
        
        self.support_data()
        self.confidence_data()


    def main(self):
        
        itemset, data = self.transform_data_to_horizontal()

        iteration = 2
        while len(data) > 0:
            if iteration == 2:
                data = self.intersection_of_items_first(data, itemset, iteration)
            else:
                data = self.intersection_of_items_other(data, itemset, iteration)

            print("")
            print("")

            iteration += 1

        self.association_rules()


if __name__ == "__main__":
    m = Main()
    m.main()
