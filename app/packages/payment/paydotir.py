import requests


class PayDotIR():
    host = "https://pay.ir"

    def __init__(self,
                 api,
                 amount,
                 redirect,
                 mobile=None,
                 factorNumber=None,
                 description=None,
                 ):

        self.info = {
                    "api": api,
                    "amount": amount,
                    "redirect": redirect,
                    "mobile": mobile,
                    "factorNumber": factorNumber,
                    "description": description,
        }

    @staticmethod
    def _api_request(endpoint,
                     verb='get',
                     json=None,
                     headers=None,
                     data=None,
                     params=None,
                     redirect=False,
                     ):
        response = getattr(requests, verb)(PayDotIR.host + endpoint,
                                           json=json,
                                           headers=headers,
                                           data=data,
                                           params=params, )
        print('{} {}'.format(response.status_code, response.reason))
        if not redirect:
            data = response.json()
            print('{}'.format(response.content))
        else:
            print("redirecting...")
            return {
                    "status_code": response.status_code,
                    "reason": response.reason,
                    "url": response.url,
                }
        if isinstance(data, dict):
            messages = data.pop("messages", None)
            if messages:
                print(json.dumps(messages, indent=4))
        try:
            response.raise_for_status()
        except Exception as e:
            print(e)
            return None
        else:
            return data

    def start(self, endpoint="/pg/send"):
        response = PayDotIR._api_request(endpoint, verb="post", data=self.info)
        return response

    def do_payment(self, token, redirect=True):
        endpoint = "/pg/{0}".format(token)
        response = PayDotIR._api_request(endpoint, redirect=redirect)
        return response

    @staticmethod
    def check(token, endpoint="/pg/verify"):
        data = {"token": token, "api": "test", }
        response = PayDotIR._api_request(endpoint, verb='post', data=data)
        return response
