import math

# Dataset
data=[
    ("A",1,2,"Red"),
    ("B",2,3,"Red"),
    ("C",3,1,"Blue"),
    ("D",6,5,"Blue")
]
# New points
X=2
Y=2

distances=[]

# Step 1 Compute Euclidean distance
for point in data:
    name,px,py,label=point
    distance=math.sqrt((px-X) **2 + (py-Y) ** 2)
    distances.append((name,distance,label))

# Step 2 sort distance
distances.sort(key=lambda x: x[1])

# Setp 3 selece K nearest neighbor
k_values=[1,3,5]

print("Prdicted Values : ")

for k in k_values:
    neighbour=distances[:k]

    votes = {}
    for n in neighbour:
        label = n[2]
        votes[label] = votes.get(label,0)+1
    
    prediction = max(votes, key=votes.get)
    
    print("K =",k,"→",prediction)