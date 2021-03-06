import requests
base_url = "http://id.bits-hyderabad.ac.in/moodle/"


def get_user_token(username, password):
    api_point = "login/token.php?service=moodle_mobile_app&username={0}&password={1}".format(username, password)
    retry = 0
    cms_token = None
    while retry <= 3:
        r = requests.get(base_url + api_point, timeout=3)
        if r.status_code == 200:
            cms_token = r.json()["token"]
            # print(cms_token)
            return cms_token
        else:
            print("Retrying...")
            retry += 1
    return cms_token


def get_user_id(cms_token):
    api_point = "webservice/rest/server.php?wsfunction=core_webservice_get_site_info&moodlewsrest" \
                + "format=json&wstoken={0}".format(cms_token)
    retry = 0
    user_id = None
    while retry <= 3:
        r = requests.get(base_url + api_point, timeout=3)
        if r.status_code == 200:
            user_id = r.json()["userid"]
            return user_id
        else:
            print("Retrying...")
            retry += 1
    return user_id


def get_enrolled_course_list(cms_token, user_id):
    api_point = "webservice/rest/server.php?wsfunction=core_enrol_get_users_courses&moodlewsrestformat=json" + \
                "&wstoken={0}&userid={1}".format(cms_token, user_id)
    # print(base_url + api_point)
    retry = 0
    course_names = []
    while retry <= 3:
        r = requests.get(base_url + api_point, timeout=3)
        if r.status_code == 200:
            res = r.json()
            for each in res:
                if each["fullname"]:
                    course_names.append(str(each["fullname"]))
            return course_names
        else:
            print("Retrying...")
            retry += 1
    return course_names


def get_assignments(cms_token):
    api_point = "webservice/rest/server.php?wsfunction=mod_assign_get_assignments&moodlewsrestformat=json" + \
                "&wstoken={0}".format(cms_token)
    # print(base_url + api_point)
    retry = 0
    assignments_names = []
    while retry <= 3:
        r = requests.get(base_url + api_point, timeout=3)
        if r.status_code == 200:
            res = r.json()
            for each in res["courses"]:
                if each["assignments"]:
                    for each_assign in each["assignments"]:
                        assignments_names.append([str(each_assign["name"]), str(each["fullname"]),
                                                  each_assign["duedate"], str(each_assign["intro"])])
            # print(assignments_names)
            return assignments_names
        else:
            # print("Retrying...")
            retry += 1
    return assignments_names

if __name__ == "__main__":
    token = get_user_token("f2014750", "1sanu@Silu")
    print(get_assignments(token))