dictionary1 = {
    "person1": {
        "first_name": "Slava",
        "last_name": "Serebrianniy"
    },
    "person2": {
        "first_name": "Daniel",
        "last_name": "Tchorni"
    }
}

print(dictionary1["person1"])
print(dictionary1.get("person1"))

print(dictionary1.get("person3"))
print(dictionary1["person3"])