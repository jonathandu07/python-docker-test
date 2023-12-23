import docker

client = docker.from_env()

container = client.create_container(
    image="python:3.11",
    command=["python", "main.py"],
)

container.start()
