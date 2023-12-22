REQUIREMENT_FILE = "../requirements.txt"


def get_requirements_list():

    with open(REQUIREMENT_FILE, "r") as file:
        requirements = [req.replace("\n", "") for req in file.readlines()]
        requirements.remove('-e .')
    return requirements


if __name__ == "__main__":
    requirements = get_requirements_list()
    print(requirements)