# Reverse_the-Linkedlist-k-nodes
We sovle this problem of reversing the linked list uisng the recursion and pointer implementation  used the time complexity O(n) and space complexity O(n).


# Apporach to solve the problem 
1.Traverse the list to check if at least k nodes are available in linked list to reverse them. 

2.If fewer than k nodes exist → return the head as it is without revesing them as original list.

3.If the k nodes available  then apply the while loop to check the condition and Reverse the first k nodes

4.Recursively call the function for the remaining list

5.Connect the reversed part with the recursively processed list and return the reverse list 

# Time complexity O(n)
# Space complexity O(n)


