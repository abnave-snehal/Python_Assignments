import math

# Dataset
data=[
    ("A",1,2,"Red"),
    ("B",2,3,"Red"),
    ("C",3,1,"Blue"),
    ("D",6,5,"Blue")
]
# input from user
X=int(input("Enter X coordiante : "))
Y=int(input("Enter Y coordinate : "))
K=3

distances=[]

# Step 1 Compute Euclidean distance
for point in data:
    name,px,py,label=point
    distance=math.sqrt((px-X) **2 + (py-Y) ** 2)
    distances.append((name,distance,label))

# Step 2 sort distance
distances.sort(key=lambda d:d[1])

# Setp 3 selece K nearest neighbor
neighbor=distances[:K]

print("\nNearest Neighbour")

for n in neighbor:
    print(f"{n[0]}- Distance {round(n[1],2)}")

# Step 4 Majoring votes
votes={}

for n in neighbor:
    label=n[2]
    votes[label]=votes.get(label,0) + 1

predicted_class=max(votes,key=votes.get)

print("\nPredicted Class : ",predicted_class)


