from itertools import combinations
from visualisation import Visualisation


class Apriori_algo:
    """Technic of suggestion: https://www.youtube.com/watch?v=a6YqMvYI9Ps"""

    def __init__(self, minimum_support):
        """Constructor"""

        # Remove article number < to minimum_support
        self.minimum_support = minimum_support
        self.visualisation = Visualisation() # Visualisation of data.

    def count(self, data, command):
        """Counting itemset"""

        data_set = list(set(data))
        dico = {i: 0 for i in data_set}

        for i in data_set:
            for co in command:
                if sum([1 for j in i if j in co]) == len(i):
                    dico[i] += 1
        return dico


    def remove(self, data):
        """Removing itemset who's < to the minimum support"""
        return {k: v for k, v in data.items() if v >= self.minimum_support}


    def couple(self, data, n):
        """Generate combination of itemset"""
        liste = list(set([j for i in data.keys() for j in i]))
        return list(set(sorted(list(combinations(liste, n)))))


    def displaying_turn(self, remover, n, label):
        """Displaying frequency of the itemset"""
        if len(remover) > 0:
            print(f"Table {label}{n}")
            print("Itemset | Frequency \n")
            [print(f"{k} : {v}") for k, v in remover.items()]
            print("")


    def recuperate_max_set(self, data):
        """Recuperate of the maximum length of the itemset"""
        max_length_itemset = max(len(j) for i in data for j in i)
        return [j for i in data for j in i if len(j) == max_length_itemset]


    def recuperate_sous_itemset(self, data, max_itemset):
        """Generate combination of itemset"""
        liste = [i for i in max_itemset]

        for i in max_itemset:
            for n in range(1, len(i)):
                sous_itemset = list(combinations(list(i), n))
                liste += [i for i in sous_itemset]

        return liste


    def recuperate_set(self, data, transaction, length_data):
        """Association rules"""

        max_itemset = self.recuperate_max_set(data)
        itemset = self.recuperate_sous_itemset(data, max_itemset)

        data = [[] for _ in range(max(len(j) for i in data for j in i))]
        [data[len(i) - 1].append(i) for i in itemset]

        # Generate subsets of itemsets.
        itemset_contains_subset = {}
        for line in data:
            for itemset in line:
                subsets = [subset for n in range(1, len(itemset)) for subset in list(combinations(itemset, n))]
                itemset_contains_subset[itemset] = [subset for subset in subsets]

        for itemsets, susbsets in itemset_contains_subset.items():

            for item in susbsets:
                # item: (I1, I2) not_in: I1 is_in I2
                not_in = tuple([i for i in itemsets if i not in item])
                is_in = tuple([i for i in itemsets if i in item])

                conf = round(transaction[itemsets] / transaction[not_in], 3)
                lift = round((transaction[itemsets] / transaction[not_in]) / (transaction[is_in] / length_data), 3)
                support = round(transaction[itemsets] / length_data, 3)

                print(not_in, "->", is_in)
                print(f"conf: {conf} supp: {support} lift: {lift}\n")

            print("")



    def apriori_algorithme(self, commands, length_data):
        """Algorythm of the appriori"""

        # Generate first itemset.
        data = [(j, ) for i in commands for j in i]

        save = []
        save_transaction = {}
        count_occurence = []

        n = 1
        while len(data) > 0:

            # CIn table
            counter = self.count(data, commands)
            self.displaying_turn(counter, n, "C")

            # FIn table
            remover = self.remove(counter)
            self.displaying_turn(remover, n, "L")

            self.visualisation.graph_from_dict(counter, remover, "Items", "Items count", "Items & min. support", self.minimum_support)

            save += [remover]
            for k, v in remover.items():
                save_transaction[k] = v

            # Generate itemset.
            couples = self.couple(remover, n+1)

            # Reinit data.
            data = [tuple(sorted(i)) for i in couples if i not in data]

            # Count iteration.
            n += 1

        # Association rules.
        self.recuperate_set(save, save_transaction, length_data)

        return save










if __name__ == "__main__":


    path3 = r"C:\Users\jeanbaptiste\Desktop\suggestion\data_focus_user\fake data\emotion_apriori.csv"
    path3 = r"C:\Users\jeanbaptiste\Desktop\suggestion\data_focus_user\magasin\course.csv"
    
    minimum_support = 2

    apriori = Apriori_algo(path3, minimum_support, sep=",")
    a = apriori.apriori_algorithme()
    for i in a:
        print(i)
    #apriori = Apriori_algo(path3, minimum_support, sep=",")
    #apriori.apriori_algorithme()
