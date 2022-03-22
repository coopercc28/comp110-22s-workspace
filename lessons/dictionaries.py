"""Demonstrations of dictionary capabilities."""

# Declaring the type of a dictionary
schools: dict[str, int]


# INitialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools ["NCSU"] = 26150

#print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookiup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key.
schools.pop("Duke")

#Test for existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

print(schools)

# Empty dictioonary literal
schools = {} # same as dict()
print(schools)

# Alternatively, intitialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# What happens whena key does not exist
print(schools["UNCC"])