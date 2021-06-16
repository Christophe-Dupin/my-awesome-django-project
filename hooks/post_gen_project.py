import os
import shutil


def remove_docker_files():
    docker_files = [
        "Dockerfile",
        "Dockerfile.prod",
        "entrypoint.prod.sh",
        "entrypoint.sh",
    ]
    for item in docker_files:
        backend_docker_files = os.path.join("backend", item)
        nginx_docker_files = os.path.join("nginx", "Dockerfile")
        os.remove(backend_docker_files)
        os.remove(nginx_docker_files)
    os.remove("docker-compose.yml")
    os.remove("docker-compose.prod.yml")


def remove_drf_starter_files():
    os.remove(os.path.join("backend", "config", "api_router.py"))
    shutil.rmtree(os.path.join("backend", "users", "api"))


def remove_traeffik_starter_files():
    os.remove(os.path.join("traeffik"))
    shutil.rmtree(os.path.join("traeffik", "users", "api"))


def main():
    if "{{ cookiecutter.use_docker }}".lower() == "n":
        remove_docker_files()
    if "{{ cookiecutter.use_drf }}".lower() == "n":
        remove_drf_starter_files()
    if "{{ cookiecutter.use_traefik }}".lower() == "n":
        remove_traeffik_starter_files()


if __name__ == "__main__":
    main()