from apriori_algo import Apriori_algo
from visualisation import Visualisation
import numpy as np
import pandas as pd

# graph
#https://www.kaggle.com/nandinibagga/apriori-algorithm

# Explication
#https://www.kaggle.com/getting-started/157119#879319

# pas compris
#https://www.kaggle.com/heeraldedhia/market-basket-analysis-using-apriori-algorithm



class Main:
    """Main program calling the appriori algo"""

    def __init__(self, path):
        """Constructor of the class creating instance & allocution in the memory of the computer."""

        self.visualisation = Visualisation() # Visualisation of data.
        self.path = path # Path of the file.
        self.minimum_support = 2 # Thresholding of the association rules.


    def main(self):
        """Main function"""

        # Recuperate data from database.
        data = [line.replace("\n", "").replace('"', "").split(",") for line in open(self.path, "r")]


        data = [
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

        # Visualisation under a dataframe.
        df = pd.DataFrame(data)
        print(df, "\n")
        print("Shape:", df.shape, "\n")

        # Visualisation of the data f(data) = number of data.
        self.visualisation.barre_graph_length([feature for line in data for feature in line], "Items", "Items count", "Number item in commands")

        # Theorem R = 3**d + 2**(d+1) + 1.
        count_association_rules = len(list(set([j for i in data for j in i])))
        print(count_association_rules)
        print(f"There are: {3**count_association_rules - 2**(count_association_rules+1) + 1} associations possibles.")

        # Max data length with min support > 0.
        max_length = max(len(i) for i in data)
        print(f"maximum size of a frquent itemset's: {max_length} with min support > 0\n")

        # Minimum support.
        print(f"Minimum support's {self.minimum_support}")

        # Association rules.
        apriori = Apriori_algo(minimum_support=2)
        data = apriori.apriori_algorithme(data, len(data))
        #[print(i) for i in data]




if __name__ == "__main__":

    path_shopping = r"C:\Users\jeanbaptiste\Desktop\suggestion data science\unsupervised\appriori\GroceryStoreDataSet.csv"
    
    m = Main(path_shopping)
    m.main()



