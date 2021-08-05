from itertools import combinations
import matplotlib.pyplot as plt

class Main:
    """ Main class """
    def __init__(self):
        """ Constructor """

        self.min_support = 2 # Minimum support.
        self.k_item_set = 3

    def barre_graph_length(self, data):

        data = [j for i in data for j in i]
        x = list(set(data))
        y = [data.count(i) for i in x]
        plt.bar(x, y, width=1, color='black')
        plt.bar(x, y, width=0.95, color='blue')
        #plt.show()


    def have_same_value_counting_sorted_by_name(self, liste, sorting_data):
        """ In the case where several items have the same value, sort them by name."""

        # Recuperate items with the same value.
        data = {i: sorting_data[i] for i in liste}
        container = {i: [] for i in [v for k, v in data.items()]}

        [container[v].append(k) for k, v in data.items() if v in container]

        # Sort the container.
        for k, v in container.items():
            container[k] = sorted(container[k])

        return [i for k, v in container.items() for i in v]


    def data_sorted_by_values(self, database, sorting_data):
        """recovery of all data. counting of all items. reorganization of items by their number in the database"""

        container = []

        for line in database:

            # Sort of all items by their number in the database.
            number_in_database_and_item = [(sorting_data[i], i) for i in line]
            line_sorted = [i for (s, i) in sorted(number_in_database_and_item, reverse=True)]

            # Sort items by name in the case where several items have the same value.
            line = self.have_same_value_counting_sorted_by_name(line_sorted, sorting_data)

            container += [line]

        return container


    def recursivity_in_branch(self, dico, branch):
        """Create a tree"""

        if len(branch) > 0:

            node = branch[0]
            branch = branch[1:]

            # New node.
            if node not in dico:
                dico[node] = {"passage": 0}
                self.recursivity_in_branch(dico[node], branch)

            elif node in dico:
                dico[node]["passage"] = 0
                self.recursivity_in_branch(dico[node], branch)


    def counter_passage_on_the_node(self, dico, branch):
        """Count the passage on the node"""

        if len(branch) > 0:

            node = branch[0]
            branch = branch[1:]

            dico[node]["passage"] = dico[node]["passage"] + 1
            self.counter_passage_on_the_node(dico[node], branch)




    def have_found_node_interest(self, node, item_search, dico_step, savegarde):
        """Recovery last node of the branch visited if we get the item_search"""

        liste = []
        for _, road in dico_step.items():

            if len(road) > 0:
                liste += [road[-1]]
                if road[-1][0] == node:
                    break

        savegarde += [liste]



    def go_to_search_end_road(self, node, branch, item_search, savegarde, dico_step, nb):

        if type(branch) == dict:

            for k, v in branch.items():

                if k != "passage":

                    dico_step[nb + 1] += [(k, branch[k]["passage"])]

                    # Recuperate the road if we find the node interest.
                    if k == item_search:
                        self.have_found_node_interest(k, item_search, dico_step, savegarde)
                    
                    # Keep looking in the tree.
                    else:
                        self.go_to_search_end_road(k, v, item_search, savegarde, dico_step, nb + 1)



    def recuperrate_branch_and_node_scored(self, database, tree_dict):
        """From all items in the database, recuperate their road"""

        savegarde = []

        # All items in the database.
        items = sorted(set([item for line in database for item in line]), reverse=True)
        max_length_of_a_branch = max([len(i) for i in database])

        for item_search in items:

            # Make a dictionary of each node. 
            dico_branch = {n: [] for n in range(max_length_of_a_branch)}

            # In the tree savegarde road
            for node, branch in tree_dict.items():

                if node != "passage":
                    dico_branch[0] += [(node, tree_dict[node]["passage"])]

                # Recuperate the road if we find the node interest.
                if node == item_search:
                    self.have_found_node_interest(node, item_search, dico_branch, savegarde)

                # keep looking in the tree.
                else:
                    self.go_to_search_end_road(node, branch, item_search, savegarde, dico_branch, 0)


        return savegarde


    def last_node_to_key_road_to_value(self, savegarde):
        """Transform list line to dictionnary: final node: road"""

        dico = {road[-1]: [] for road in savegarde}

        for line in savegarde:

            last_node = line[-1]
            road = line[:-1]

            if len(road) > 0:
                dico[last_node] += [road]

        return {k: v for k, v in dico.items() if len(v) > 0}


    def first_step_conditional_pattern_base(self, dico):
        """Regroup roads with finish node score"""

        # Dictionnary whose key's the endpoint and which has the value of routes. 
        conditional_pattern_base = {k: [] for (k, score), v in dico.items()}

        # Recuperate endpoint: road
        for (endpoint, score), routes in dico.items():
            [conditional_pattern_base[endpoint].append(([node for (node, _) in road], score)) for road in routes]

        # Recovery the node without his scorage.
        data = []
        for endpoint, routes in conditional_pattern_base.items():
            d = {road[0]: [] for (road, score) in routes}
            [d[road[0]].append((road, score)) for (road, score) in routes]
            data += [{endpoint: d}]

        return data


    def second_step_conditional_fp_tree(self, conditional_pattern_base):
        """Recuperate of the nodes in common of differents routes from an endpoint"""

        print("\nself.min_support", self.min_support)

        conditional_fp_tree = {node_depature: [] for line in conditional_pattern_base for node_depature, branch in line.items()}

        for line in conditional_pattern_base:

            for node_depature, branch in line.items():

                for k, v in branch.items():

                    d = {i: 0 for i in [j for (i, score) in v for j in i]}

                    for (i, score) in v:
                        for j in i:
                            d[j] += score

                    d = {k: v for k, v in d.items() if v >= self.min_support}

                    conditional_fp_tree[node_depature] += [d]

        return conditional_fp_tree



    def third_step_frequent_patterns_generated(self, conditional_fp_tree):
        """Recuperate the minimum score of the combination of the road"""

        frequent_patterns_generated = {k: [] for k,v in conditional_fp_tree.items()}

        for k, v in conditional_fp_tree.items():

            for line in v:

                liste = [k] + [k for k, v in line.items()]

                comb = []
                for n in range(2, len(liste) + 1):
                    comb += list(combinations(liste, n))

                comb = [i for i in comb if k in i]

                dd = {i: [] for i in comb}

                for i in comb:
                    dd[i] = min([line[j] for j in i if j != k])

                frequent_patterns_generated[k] += [dd]

        return frequent_patterns_generated



    def association_rules(self, frequent_patterns_generated, supp_count):
        """Recuperate the confidence of a combination of an items (k-items): items score / items"""

        dico_support = {tuple(sorted(k1)): v1 for k, v in frequent_patterns_generated.items() for i in v for k1, v1 in i.items()}

        for k, v in supp_count.items():
            dico_support[(k, )] = v


        rules_association = []

        for k, v in frequent_patterns_generated.items():

            for line in v:

                for k, _ in line.items():

                    if len(k) == self.k_item_set:

                        comb = [list(combinations(k, n)) for n in range(1, len(k) + 1)]
                        comb = sorted(tuple(sorted(j)) for i in comb for j in i)

                        for s in comb:
                            l = tuple(sorted(i for i in k if i not in s))
                            if len(l) > 0:
                                support_s = dico_support[tuple(sorted(s))]
                                support_l = dico_support[tuple(sorted(k))]

                                confidence = round(support_l / support_s, 2)
                                print(f"{s} -> {l}     {support_l} / {support_s}      = ", confidence, "Accepted: ", confidence >= 0.6)

                print("")





    def first_part(self, data):
        """Treatment of the data & counting"""

        self.barre_graph_length(data)

        counting_items = [j for i in data for j in list(set(i))]
        counting_items = {i: counting_items.count(i) for i in sorted(counting_items)}
        print(counting_items, "\n")

        counting_items = {k: v for k, v in counting_items.items()}

        sorting_data = dict(sorted(counting_items.items(), key=lambda item: item[1], reverse=True))
        print(sorting_data, "\n")

        # Filter from the minimum support.
        data = [[j for j in i if counting_items[j] >= self.min_support] for i in data]


        sorting_data = self.data_sorted_by_values(data, sorting_data)
        [print(i) for i in sorting_data]
        print("")

        return sorting_data, counting_items


    def second_part(self, sorting_data, data):
        """Create a tree of the routes"""

        dico = {}
        # Create tree.
        [self.recursivity_in_branch(dico, branch) for branch in sorting_data]
        #print(dico)

        # Count passage on the node.
        [self.counter_passage_on_the_node(dico, branch) for branch in sorting_data]
        #print(dico)

        # association rules.
        print("dico")
        [print(k, v) for k, v in dico.items()]
        print("")
        print("")

        savegarde = self.recuperrate_branch_and_node_scored(data, dico)
        print("savegarde")
        [print(i) for i in savegarde]
        print("")

        dico = self.last_node_to_key_road_to_value(savegarde)
        print("dico")
        [print(k, v) for k, v in dico.items()]
        print("")

        return dico


    def third_part(self, dico, sorting_data, counting_items):
        """The differents steps of the FP-growth"""

        conditional_pattern_base = self.first_step_conditional_pattern_base(dico)
        print("conditional_pattern_base")
        [print(i) for i in conditional_pattern_base]

        conditional_fp_tree = self.second_step_conditional_fp_tree(conditional_pattern_base)

        print("")
        print("conditional_fp_tree")
        for k, v in conditional_fp_tree.items():
            print(k, v)

        frequent_patterns_generated = self.third_step_frequent_patterns_generated(conditional_fp_tree)

        print("")
        print("frequent_patterns_generated")
        for k, v in frequent_patterns_generated.items():
            print(k, v)

        print("")
        self.association_rules(frequent_patterns_generated, counting_items)






    def main(self):

        data = [
            ["I1", "I2", "I5"],
            ["I2", "I4"],
            ["I2", "I3"],
            ["I1", "I2", "I4"],
            ["I1", "I3"],
            ["I2", "I3"],
            ["I1", "I3"],
            ["I1", "I2", "I3", "I5"],
            ["I1", "I2", "I3"],
        ]

        """
        data = [
            ["M", "O", "N", "K", "E", "Y"],
            ["D", "O", "N", "K", "E", "Y"],
            ["M", "A", "K", "E"],
            ["M", "U", "C", "K", "Y"],
            ["C", "O", "O", "K", "I", "E"],

        ]
        self.min_support = 3
        """


        sorting_data, counting_items = self.first_part(data)
        dico = self.second_part(sorting_data, data)
        self.third_part(dico, sorting_data, counting_items)






         

if __name__ == "__main__":

    m = Main()
    m.main()