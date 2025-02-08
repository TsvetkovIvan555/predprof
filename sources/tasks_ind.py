import os

task = [[[] for _ in range(27)] for _ in range(3)]

folder_path = "tasks"
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        file = os.path.join(root, file_name)

        if file[file.find(".") + 1:] == "txt" and file.find("_") == file.rfind("_"):
            f = open(file, 'r', encoding='utf-8')
            a = file.find("_") + 1; b = file.find(".")
            id = file[a:b]
            type = f.readline().replace("\n", "")
            diff = f.readline().replace("\n", "")
            f.close()

            task[int(diff) - 1][int(type) - 1].append(id)
print(task)