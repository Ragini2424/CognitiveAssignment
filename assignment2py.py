#ques1 create a list L defined as = [10,20,30,40,50,60,70,80]
# i) WAP to add 200 and 300 to L
L = [10,20,30,40,50,60,70,80]
L.append(200)
L.append(300)
print(L)
# ii) remove 10 and 30 from L
L.remove(10)
L.remove(30)
print(L)
# iii) sort L in ascending order
L.sort()
print(L)
#iv) sort L in descending order
L.sort(reverse = True)
print(L)

#ques2 create a tuple score = (45,89.5,76,45.4,89,92,58,45)
score = (45,89.5,76,45.4,89,92,58,45)
print(score)
# i)identify highest score and index in the tuple
print(max(score))
print(score.index(max(score)))
# ii)identify lowest score and count how many time it appears
print(min(score))
print(score.count(min(score)))
# iii) reverse a tuple and return it as a list
print(list(reversed(score)))
# iv)check if a specific score '76' (input by user) is present in the tuple and print its first occurence index, or message saying it's not present
x = int(input('enter a number'))
if x in score:
    print(score.index(x))
else:
    print('not present')

#ques3 Write a Program to create a list of 100 random num between 100 and 900.
import random
def is_prime(n):
  if n <= 1:
    return False
  for i in range (2,int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

L = [random.randint(100,900) for _ in range(100)]
print(L)
# i) count and print odd number from the list
odd_num = [num for num in L if num%2 != 0]
odd_count = len(odd_num)
print(odd_count)
print(odd_num)
# ii) count and print even number from the list
even_num = [num for num in L if num%2 == 0]
even_count = len(even_num)
print(even_count)
print(even_num)
# iii) count and print prime number from the list
prime_num = [num for num in L if is_prime(num)]
prime_count = len(prime_num)
print(prime_num)
print(prime_count)

#ques4 Consider the following two sets, A and B, represen ng scores of two teams in multiple matches.  A = {34, 56, 78, 90}  and B = {78, 45, 90, 23} 
#WAP to perform the following operations using set functions:
# i) Find the unique scores achieved by both teams (union of sets).
A = {36,56,78,90}
B = {78,45,90,23}
unique = A.union(B)
print(unique)
# ii) Identify the scores that are common to both teams (intersection of sets).
common = A.intersection(B)
print(common)
#iii)Find the scores that are exclusive to each team (symmetric difference). 
exclusive = A.symmetric_difference(B)
print(exclusive)
#iv)Check if the scores of team A are a subset of team B, and if team B's scores are  a superset of team A. 
is_subset = A.issubset(B)
is_superset = B.issuperset(A)
print(is_subset)
print(is_superset)
#v) Remove a specific score 𝑋 (input by the user) from set A if it exists. If not, print a message saying it is not present.
x = int(input('enter a score to remove: '))
if x in A:
  A.remove(x)
  print('score is removed')
else:
  print('score is not valid')
print(A)

# ques5 Write a program to rename a key city to a location in the following dictonary.
sample_dict = {
    "name" : "Kelly",
    "age" : 25,
    "salary" : 8000,
    "city" : "New York"
}
sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)
