info = {"Name" : "Oluwanifemi Akinloose", "Age": "18", "School": "University Of Leicester", "College" : "Computing", "Favourite fruits": ["Mango", "Bannana", "Orange"] }
info.update({"Languages":["English", "Yoruba", "Pidgin"] })
info.pop("Age")
del info["College"]
print(len(info))
print(info.items())