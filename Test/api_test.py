import requests

class AcademicAPI:
    def __init__(self, username:str, password:str):
        self.username = username
        self.password = password
        self.academic_sys_url = "https://jwjx.gxnu.edu.cn/wfw/manage"

        # Start session
        self.web_session =  requests.session()
        self.initial_response = self.web_session.get(self.academic_sys_url)
        self.sso_referer_url = self.initial_response.url


    def get_all_score(self):
        pass


if __name__ == "__main__":
    username = "12345"
    password = "12345"
    aca_info = AcademicAPI(username, password)
    aca_info.get_all_score()