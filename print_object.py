def print_object_data(data):
    for i, obj in enumerate(data):
        print(f"{i+1}. Nama: {obj['name']}, usia: {obj['age']}")

data = [
    {
        "name": "Udin",
        "age": 10
    },
    {
        "name": "Ujang",
        "age": 11
    },
    {
        "name": "Asep",
        "age": 12
    }
]

print_object_data(data)