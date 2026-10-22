coding_club = {101, 102, 103, 104, 105}
robotics_club = {104, 105, 106, 107}

union_result=coding_club | robotics_club
common_elements=coding_club & robotics_club
Diff_result=coding_club-robotics_club
print("Disjoint Status : ",coding_club.isdisjoint(robotics_club))
print("Subset Status : ",robotics_club.issubset(coding_club))
print("Union : ",union_result)
print("Intersection : ",common_elements)
print("Difference : ",Diff_result)