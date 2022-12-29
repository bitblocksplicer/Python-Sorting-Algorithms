# Python Sorting Algorithms #
This repo includes sorting algorithms such as:
1. Bogo sort
2. Selection sort
3. Bubble sort

## Bogo Sort
Bogo sort is basically reshuffling the list until it's sorted. It's not an efficient algorithm to use (O((n+1)!)).
![resim](images/bogo.png)

## Selection Sort
Finding the current minimum number of the list, adding it to the first index of unsorted list, and keep doing it until it's completely sorted. It can be done either swapping indexes or creating a new list. In *selection.py*, you can see an example of list creating method
![resim](images/selection.png)
[*image source*](https://www.programiz.com/dsa/selection-sort)