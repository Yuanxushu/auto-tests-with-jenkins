from os import path

API_ISSUE_LOG = "api_issue_log"


def get_api_issue_log():
    result = {}

    if path.exists(API_ISSUE_LOG):
        with open(API_ISSUE_LOG, "r") as f:
            for line in f:
                temp = line.split(" ", maxsplit=1)
                if len(temp) == 2:
                    result[temp[0]] = result.get(temp[0], "") + temp[1]

    return result


print(get_api_issue_log())
