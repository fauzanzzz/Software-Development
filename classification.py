def group_people(data):
    groups = {
        "sex": {"male": [], "female": []},
        "age": {"under20": [], "older": []},
        "marriage": {"single": [], "double": []},
        "status": {"student": [], "employee": []}
    }
    
    for person in data:
        # Group by sex
        if person["sex"] == "male":
            groups["sex"]["male"].append(person["name"])
        elif person["sex"] == "female":
            groups["sex"]["female"].append(person["name"])
        
        # Group by age
        if person["age"] < 20:
            groups["age"]["under20"].append(person["name"])
        else:
            groups["age"]["older"].append(person["name"])
        
        # Group by marital status
        if person["marital"] == "single":
            groups["marriage"]["single"].append(person["name"])
        else:
            groups["marriage"]["double"].append(person["name"])
        
        # Group by job status
        if person["social"] == "student":
            groups["status"]["student"].append(person["name"])
        else:
            groups["status"]["employee"].append(person["name"])
    
    return groups

data = [
    {
        "name":"udin",
        "sex":"male",
        "age":10,
        "marital":"single",
        "social":"student"
    },
    {
        "name":"ujang",
        "sex":"male",
        "age":25,
        "marital":"married",
        "social":"employee"
    },
    {
        "name":"icih",
        "sex":"female",
        "age":10,
        "marital":"single",
        "social":"student"
    },
    {
        "name":"eneng",
        "sex":"female",
        "age":100,
        "marital":"married",
        "social":"employee"
    },
    {
        "name":"asep",
        "sex":"male",
        "age":20,
        "marital":"single",
        "social":"employee"
    }
]

result = group_people(data)
print(result)