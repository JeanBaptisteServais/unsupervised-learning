import matplotlib.pyplot as plt

class Visualisation:



    def ploting(self, x, y, x_title, y_title, title):

        # Size of the police.
        size = 12

        # Title of the data.
        plt.xlabel(x_title, size=size,)
        plt.ylabel(y_title, size=size)

        # Title of the graph.
        plt.title(title, 
                fontdict={'family': 'serif', 
                            'color' : 'black',
                            'weight': 'bold',
                            'size': 18})
        # Bar.
        plt.bar(x, y, width=0.95, color='blue')
        # Displaying.
        plt.show()



    def barre_graph_length(self, data, x_title, y_title, title):
        """Bar tool"""

        # X data.
        x = sorted(set(data))
        # Counter of the data.
        y = [data.count(i) for i in x]

        self.ploting(x, y, x_title, y_title, title)


    def graph_from_dict(self, dico1, dico2, x_title, y_title, title, min_support):

        abs_data = lambda key, dico: [str(k) if key else v for k, v in dico.items()]

        x1 = abs_data(True, dico1)
        y1 = abs_data(False, dico1)

        x2 = abs_data(True, dico2)
        y2 = abs_data(False, dico2)


        # Size of the police.
        size = 12

        # Title of the data.
        plt.xlabel(x_title, size=size,)
        plt.ylabel(y_title, size=size)

        # Title of the graph.
        plt.title(title, 
                fontdict={'family': 'serif', 
                            'color' : 'black',
                            'weight': 'bold',
                            'size': 18})
        # Bar.
        plt.bar(x1, y1, width=0.95, color='red')
        plt.bar(x2, y2, width=0.95, color='blue')

        plt.axhline(y=min_support - 0.05, color="red")

        # Displaying.
        plt.show()
