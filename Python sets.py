# Python sets
#1) It is a collection of unique data
#2) data are immutable 
#3)non-index un-ordered
#4)Elements can't be duplicate  
#5)Elements can be of different types but mutable elements like list ,dictionary can't be elements  

# LETS STARTS CREATION

id = {110,35,894,61,29,"Jitesh",15.0}
#print(id)
setdemo = set(["a","b","c","d","e"])
print(setdemo)
# how to add elements 

setdemo.add("Welcome add new name")
print(setdemo)

# how to remove an element

setdemo.discard("Jitesh")
print(setdemo)


# how to update python sets 

companies = {"x","y"}
tech = ["r","s","t"]
companies.update(tech)
print(companies)







