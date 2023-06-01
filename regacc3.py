from time import sleep
import requests
import json
import urllib.parse
import subprocess
import random

class RegAcc:
    def __init__(self, num_emails):
        self.taikhoan = ""
        self.matkhau = "lequanggminhhofficial"
        self.sdt = "0328774559"
        self.email = ""
        self.accessToken = ""
        self.refreshToken = ""
        self.cookies = ""
        self.num_emails = num_emails
        self.domains = ['gmail.com', 'outlook.com', 'hotmail.com', 'lequanggminhhofficial.com', 'trickerlqm.com', 'ytb.lequanggminhhofficial.com', 'spamcallsms.click', 'yahoo.com', 'outlook.com.vn', 'outlook.kr']
        self.success_count = 0

    def generate_emails(self):
        emails = []
        for _ in range(self.num_emails):
            email = f"{domain_mail}{random.randint(1, 99999999)}@{random.choice(self.domains)}"
            emails.append(email)
        return emails

    def save_emails_to_file(self, emails):
        with open("taikhoan.txt", "w") as file:
            for email in emails:
                file.write(email + "\n")
        print(f"{self.num_emails} email(s) have been saved to taikhoan.txt.")

    def reg(self):
        headers = {
            'authority': 'metahome.digital',
            'accept': 'application/json',
            'accept-language': 'ko',
            'content-type': 'application/json',
            'origin': 'https://metahome.digital',
            'referer': 'https://metahome.digital/sign-up',
            'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
        }

        json_data = {
            'email': self.taikhoan,
            'password': self.matkhau,
            'confirmPassword': self.matkhau,
            'ageTerms': True,
            'termsOfUse': True,
            'privacy': True,
            'readRisk': True,
            'referralCode': code,
        }

        response = requests.post('https://metahome.digital/api/sign-up', headers=headers, json=json_data).text
        return response

    def login(self):
        cookies2 = {
            'account': '%7B%22account%22%3Anull%7D',
        }

        headers2 = {
            'authority': 'metahome.digital',
            'accept': 'application/json',
            'accept-language': 'ko',
            'content-type': 'application/json',
            'cookie': 'account=%7B%22account%22%3Anull%7D',
            'origin': 'https://metahome.digital',
            'referer': 'https://metahome.digital/sign-in',
            'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
        }

        json_data2 = {
            'email': self.taikhoan,
            'password': self.matkhau,
        }

        login = requests.post('https://metahome.digital/api/login', cookies=cookies2, headers=headers2, json=json_data2)
        self.email = login.get("email")
        if self.email is not None:
            self.accessToken = login["accessToken"]
            self.refreshToken = login["refreshToken"]
            cookiesacc = json.dumps({
                "account": {
                    "email": self.email,
                    "accessToken": self.accessToken,
                    "name": None
                }
            })
            self.cookies = urllib.parse.quote(cookiesacc)


    def set(self):
        headers1 = {
            'authority': 'metahome.digital',
            'accept': 'application/json',
            'accept-language': 'ko',
            'authorization': self.refreshToken,
            'content-type': 'application/json',
            'cookie': f'account={self.cookies}',
            'origin': 'https://metahome.digital',
            'referer': 'https://metahome.digital/mypage',
            'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
        }

        json_data1 = {
            'name': 'Lê Quang Minh',
            'country': 'KOREA',
            'phoneNumber': self.sdt,
        }

        response = requests.post('https://metahome.digital/api/account/phone-number', headers=headers1, json=json_data1).text
        self.success_count += 1
        print(f"Thành Công ({self.success_count}/{self.num_emails}) |Mã: {code} Tài Khoản: {self.taikhoan} | Mật Khẩu: {self.matkhau}")
        with open("thanhcong.txt", "a") as file:
            file.write(f"{self.taikhoan} | {self.matkhau}" + "\n")

    def run(self):
        emails = self.generate_emails()
        self.save_emails_to_file(emails)
        for taikhoan in emails:
            self.taikhoan = taikhoan.strip()
            response = self.reg()
            self.login()
            self.set()

num_emails = int(input("Nhập số lượng email muốn tạo: "))
code = input("Mã giới thiệu: ")
domain_mail = input("Nhập tên mail: ")
main = RegAcc(num_emails)
main.run()
