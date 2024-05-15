from locust import HttpUser, task, between

#
attacked_hosts = (
    "https://uol.unifor.br/",
    "https://ead.unifor.br/",
    "https://www.unifor.br/",
    "https://www.youtube.com/",
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://www.instagram.com/",
    "https://www.twitter.com/",
    "https://www.linkedin.com/",
    "https://www.github.com/",
)


class WebsiteUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def attack(self):
        for host in attacked_hosts:
            self.client.get(f"/api/{host}")
