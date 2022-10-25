import os

img_fem = "img/profile-pics/female"
img_male = "img/profile-pics/male"

race_fem = []
race_male = []

for file in os.listdir(img_fem):
    race_fem.append(os.path.join(img_fem, file).replace("\\", "/"))

for file in os.listdir(img_male):
    race_male.append(os.path.join(img_male, file).replace("\\", "/"))

path_pics_fem = []
path_pics_male = []

names_fem = []
names_male = []

for race in race_fem:
    for pic in os.listdir(race):
        path_pics_fem.append(os.path.join(race, str(pic)).replace("\\", "/"))

for race in race_male:
    for pic in os.listdir(race):
        path_pics_male.append(os.path.join(race, str(pic)).replace("\\", "/"))

for i in range(0, len(path_pics_fem)):
    path_pics_fem[i] = "../" + path_pics_fem[i]

for i in range(0, len(path_pics_male)):
    path_pics_male[i] = "../" + path_pics_male[i]

fem_dict = {}
male_dict = {}

i = 0

fem_obj = "Females = {"
for path in path_pics_fem:
    id = str(i)
    if len(id) > 2:
        id = id
    elif len(id) > 1:
        id = "0" + id
    elif len(id) == 1:
        id = "00" + id

    name = path.rsplit("/")[-1].replace(".png", "")

    species = path.split("/")[-2]
    species = species[:-1]
    species = species[0].upper() + species[1:]

    fem_obj += f"\n\tF{id}: {{\n\t\tname: '{name.capitalize()}',\n\t\timage: '{path}',\n\t\tspecies: '{species}'\n\t}},"
    i += 1

fem_obj += "\n}"


i = 0
male_obj = "Males = {"
for path in path_pics_male:
    id = str(i)
    if len(id) > 2:
        id = id
    elif len(id) > 1:
        id = "0" + id
    elif len(id) == 1:
        id = "00" + id

    name = path.rsplit("/")[-1].replace(".png", "")

    species = path.split("/")[-2]
    species = species[:-1]
    species = species[0].upper() + species[1:]

    male_obj += f"\n\tM{id}: {{\n\t\tname: '{name.capitalize()}',\n\t\timage: '{path}',\n\t\tspecies: '{species}'\n\t}},"
    i += 1


male_obj += "\n}"

print(male_obj)