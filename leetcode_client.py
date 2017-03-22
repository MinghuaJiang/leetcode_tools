import requests
import time
from random import randint

class LeetcodeClient:
    def __init__(self):
        self.problem_url = "https://leetcode.com/api/problems/algorithms/"
        self.cache = {}

    def get_response_json(self, url):
        response = requests.get(url)
        result = response.json()
        return result

    def get_random_problem(self):
        leetcode_url = "http://leetcode.com/problems/"
        cur_date = time.strftime("%d/%m/%Y")
        if cur_date in self.cache:
            problems = self.cache[cur_date]
        else:
            result = self.get_response_json(self.problem_url)
            problems = [each["stat"]["question__title_slug"] for each in result["stat_status_pairs"]]
            self.cache[cur_date] = problems

        length = len(problems)
        index = randint(0, length - 1)
        return leetcode_url + problems[index]

if __name__ == '__main__':
    client = LeetcodeClient()
    print(client.get_random_problem())
