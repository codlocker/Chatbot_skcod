import requests


base_url = "http://id.bits-hyderabad.ac.in/moodle/"


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


def main_function(variables):
    output = [{
        "include": ["web"],
        "text": ["Sorry I couldn't understand :( ."]
    }]
    if variables["templateKey"] == "first_time_login":
        output = [{
            "include": ["web"],
            "text": [
                "You are successfully logged in. " +
                "I can tell you about your assignments in your registered courses."]
        }]
    elif variables["templateKey"] == "courses_not_specified":
        assignment_details = get_assignments(variables["consumerDataStore"]["cms_token"])
        text = "Your assignments are: \n"
        if not assignment_details:
            output = [{
                "include": ["web"],
                "text": "Sorry I am facing troubles getting the data. Please try me after some time"
            }]
            return output
        for i in assignment_details:
            text = text + "Course name: " + i[1] + "\n"
            if len(i[-1]) > 0:
                text = text + "Problem statement: " + i[-1] + "\n"
        output = [{
            "include": ["web"],
            "text": [text]
        }]
    elif variables["templateKey"] == "list_courses":
        course_details = get_enrolled_course_list(variables["consumerDataStore"]["cms_token"], variables["consumerDataStore"]["user_id"])
        text = "Your courses are: \n"
        c = 1
        if not course_details:
            output = [{
                "include": ["web"],
                "text": "Sorry I am facing troubles getting the data. Please try me after some time"
            }]
            return output
        for i in course_details:
            text = text + str(c) + i + "\n"
            c += 1
        output = [{
            "include": ["web"],
            "text": [text]
        }]
    elif variables["templateKey"] == "error":
        output = [{
            "include": ["web"],
            "text": ["Sorry I couldn't understand :( ."]
        }]
    # if variables['templateKey'] == 'pushreminder':
    #     output = [{"include":["web"],"text": [""]}]
    # elif (variables['templateKey'] == "give_time_interval"):
    #     output = [{"include":["web"],"text": ["Give me a valid time interval"]}]
    return output