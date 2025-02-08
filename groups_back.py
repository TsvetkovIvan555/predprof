from flask import Flask

app = Flask(__name__)

def make_ind(ind):
    return "0"*(5 - len(str(ind))) + str(ind)

def make_tests_for_groups(ind):
    ans = []
    name = "sources/groups/test/group_" + make_ind(ind) + ".txt"
    with open(name) as file:
        for index_of_test in file:
            name_of_test = "sources/tests/test_" + make_ind(index_of_test) + ".txt"
            with open(name_of_test) as test_file:
                title = test_file.readline().replace("\n", "")
                deadline = test_file.readline().replace("\n", "")
                description = test_file.readline().replace("\n", "")
                test_link = test_file.readline().replace("\n", "")
                results_link = test_file.readline().replace("\n", "")
            data = {"title": title, "due_date": deadline, "description": description, "test_link": test_link, "results_link": results_link}
            ans.append(data)
    return ans



if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

