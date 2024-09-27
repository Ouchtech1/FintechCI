from locust import HttpUser, task

class LoadTestUser(HttpUser):
    @task
    def index(self):
        self.client.get("/")
