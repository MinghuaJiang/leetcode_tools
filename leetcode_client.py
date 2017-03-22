import requests
import time
from random import randint

class LeetcodeClient:
    def __init__(self):
        self.url = "https://leetcode.com/api/problems/algorithms/"
        self.cache = {}

    def get_response_json(self):
        response = requests.get(self.url)
        result = response.json()
        problems = [each["stat"]["question__title_slug"] for each in result["stat_status_pairs"]]
        cur_date = time.strftime("%d/%m/%Y")
        self.cache[cur_date] = problems
        return problems

    def get_random_problem(self):
        leetcode_url = "http://leetcode.com/problems/"
        cur_date = time.strftime("%d/%m/%Y")
        if cur_date in self.cache:
            problems = self.cache[cur_date]
        else:
            problems = self.get_response_json()
        length = len(problems)
        index = randint(0, length - 1)
        return leetcode_url + problems[index]

if __name__ == '__main__':
    client = LeetcodeClient()
    print(client.get_random_problem())
