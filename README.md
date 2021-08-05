# unsupervised-learning
suggestion techniques


      If the user buys pasta and butter, he will buy Gruyere.

      If the user buys a computer he will buy a mouse.

      If the user has to buy a mouse and a computer, he will buy a keyboard.

      -> So the user does not have to search the on site for a mouse !


<h1>fp_growth</h1>


![data](https://user-images.githubusercontent.com/54853371/128367219-94ae15cd-2d13-43f2-8018-5684ea4e975a.png)


![data](https://user-images.githubusercontent.com/54853371/128368064-5578e6a2-3e1b-4bd9-88d2-8c30b8f9c91b.png)

<br><br><br><br>



![data](https://user-images.githubusercontent.com/54853371/128367811-1c60d122-c3cd-4646-9b6c-919625588bce.png)

<br><br>

![data](https://user-images.githubusercontent.com/54853371/128367830-8fd18865-c49b-41d1-9695-bdafb5f0991d.png)

<br><br>

![data](https://user-images.githubusercontent.com/54853371/128367847-9f1329ff-4603-4a59-8341-92268b40fd6d.png)





![data](https://user-images.githubusercontent.com/54853371/128367424-945d56ac-bd17-4882-ab63-bddb1cab4f67.png)


![data](https://user-images.githubusercontent.com/54853371/128367619-05bf11d4-5e1a-405e-8015-2c4bc1b0d64f.png)










<h1> Apriori algorythm of Rakesh Agrawal </h1>


<details>

<br><br><br>

![data](https://user-images.githubusercontent.com/54853371/128016384-d91a96fd-c46f-4330-b742-e81c5ee94f54.png)

<i>Dataset of 9x4</i>


![data](https://user-images.githubusercontent.com/54853371/128015451-5d3908c9-a7cb-4776-a9ef-66b1197a05d9.png)

<i>Items count</i>

![data](https://user-images.githubusercontent.com/54853371/128017363-8d290b4e-d0c0-4da0-be9c-2f7718237f0e.png)

Theorem: R = 3^d + 2^(d+1) + 1 Here we have d = 5


<br><br><br>


![data](https://user-images.githubusercontent.com/54853371/128014211-16db7451-88f2-4ed0-82b1-f2c14bc06601.png)

<i>Red line's minimum support. Min support = 2</i>

Here of itemsets are >= 2




![data](https://user-images.githubusercontent.com/54853371/128016482-e2e24fe0-6d0d-4c09-86ae-78fda36e49f4.png)

<br><br>

![data](https://user-images.githubusercontent.com/54853371/128014300-7a57d1cd-3f34-42d2-8a6b-a43351e592c8.png)

<br><br><br>

![data](https://user-images.githubusercontent.com/54853371/128016545-013ea012-4904-45f0-8ce8-f11ac62b6759.png)

<br><br>

![data](https://user-images.githubusercontent.com/54853371/128039386-c1f7da68-f743-42c7-baeb-7b87df94e432.png)


<br><br><br>

![data](https://user-images.githubusercontent.com/54853371/128016618-c15973c8-491c-4d46-b566-4644fd725324.png)

<br><br>

![data](https://user-images.githubusercontent.com/54853371/128014419-b6a86cd2-87e7-41fe-b70e-c93507024235.png)

<br><br><br>

![data](https://user-images.githubusercontent.com/54853371/128016702-722417ef-5821-4c1b-b352-8951cde756a0.png)



<strong>Ci Phase: </strong> Phase of counting the itemset.

<strong>Fi Phase: </strong> Phase of filtering the itemset by the minimum support.



![data](https://user-images.githubusercontent.com/54853371/128038775-d3590c6a-413e-4d06-a218-46a16dd70fb0.png)

<strong>Support:</strong> Number of transaction contaning an item / total of transations
      
<strong>Confidence:</strong> (X -> Y) Number of transaction containing X & Y / Number of transaction X

<strong>Lift:</strong> Support (X, Y) / Suport (X) * Support (Y)


![data](https://user-images.githubusercontent.com/54853371/128016286-973137af-5a9f-4b69-b4ec-c8a10d83f0da.png)


Inconvenient
  
Very long:

      - k-Itemsets = x! / y! * (x - y)!
      
      where x = number data in the dataset
            y = number itemset
 


</details>
