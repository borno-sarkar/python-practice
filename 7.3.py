with open("practice.txt", "r") as f:
    data = f.read()
    if "learning" in data:  # এখানে কোটেশন দিতে হবে
        print("Found")
    else:
        print("Not found")
