import os, json, re


def save(path: str, pwd: str, email: str):
    data = {"email": email, "password": pwd}
    filename = f"{path}/{email}.json"
    try:
        write(filename, data)
    except FileNotFoundError:
        os.makedirs(path)
        write(filename, data)
    except Exception as error:
        print(error)


def write(path: str, data: any):
    with open(path, "w") as file:
        json.dump(data, file)


def check_pwd(pwd: str) -> bool:
    if re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", pwd):
        return True
    return False


def check_email(email: str) -> bool:
    if re.match(r"^[a-z0-9]+[._]?[a-z0-9]+@\w+[.]\w{2,3}$", email):
        return True
    return False


if __name__ == "__main__":
    while True:
        pwd = input("Enter your password: ")
        if check_pwd(pwd):
            print("Success")
            break
        else:
            print("Error")
    while True:
        email = input("Enter your email: ")
        if check_email(email):
            print("Success")
            break
        else:
            print("Error")
    save("less17/data", pwd, email)
