from flask import Flask

app = Flask(__name__)

def make_ind(ind, cnt):
    return "0"*(cnt - len(str(ind))) + str(ind)

def make_tests_for_groups(ind):
    ans = []
    name = "sources/groups/test/group_" + make_ind(ind, 5) + ".txt"
    with open(name) as file:
        for index_of_test in file:
            index_of_test = index_of_test.replace("\n", "")
            data = {"test_link" : ("/test/" + str(index_of_test)), "results_link" : "/statistic"}
            ans.append(data)
    return ans

def add_group(data, groups_cnt, user_now):
    name = "sources/groups/main_information/group_" + make_ind(groups_cnt, 5) + ".txt"
    file = open(name, mode = 'w', encoding='utf-8')
    file.write(data['group_name'] + "\n")
    file.write(data['group_description'] + "\n")
    file.write(str(user_now) + "\n")
    file.close()
    name = "sources/groups/lectures/group_" + make_ind(groups_cnt, 5) + ".txt"
    file = open(name, mode = 'w', encoding='utf-8')
    file.close()
    name = "sources/groups/test/group_" + make_ind(groups_cnt, 5) + ".txt"
    file = open(name, mode='w', encoding='utf-8')
    file.close()
    name = "sources/groups/users/group_" + make_ind(groups_cnt, 5) + ".txt"
    file = open(name, mode='w', encoding='utf-8')
    file.write(str(user_now) + "\n")
    file.close()
    name = "sources/users/groups/user_" + make_ind(user_now, 3) + ".txt"
    file = open(name, mode='a', encoding='utf-8')
    file.write(str(groups_cnt) + "\n")
    file.close()
    return make_ind(groups_cnt, 5)

def add_new_user_to_group(data, user_token):
    group_token = data["groupCode"]
    name = "sources/groups/users/group_" + make_ind(group_token, 5) + ".txt"
    file = open(name, mode='a', encoding='utf-8')
    file.write(str(user_token) + "\n")
    file.close()
    name = "sources/users/groups/user_" + make_ind(user_token, 3) + ".txt"
    file = open(name, mode='a', encoding='utf-8')
    file.write(str(group_token) + "\n")
    file.close()

def add_test(data, ind):
    index = make_ind(ind, 5)
    name = "sources/groups/test/group_" + index + ".txt"
    file = open(name, mode='a', encoding='UTF-8')
    file.write(data['token'] + "\n")

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

