from locust import HttpUser, task, between

#
attacked_hosts = (
    "http://example.com/",
    "https://uol.unifor.br/",
    "https://ead.unifor.br/",
    "https://www.unifor.br/",
)


class WebsiteUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def attack_via_python(self):
        for host in attacked_hosts:
            self.client.get(f"http://api-python:5000/api/{host}", verify=False)
