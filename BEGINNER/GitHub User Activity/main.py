import requests
import sys



def main():

    if len(sys.argv) != 2:
        print("Error in username\n. Try: python main.py <username>.")
        return
    else:
        username = sys.argv[1]


    url = f"https://api.github.com/users/{username}/events"

    response = requests.get(url)

    #.. to get a better view of the data I created the data in a .json file (not necessary)
    #.. with open("data.json", "w") as f:
    #..     json.dump(data, f, indent=4)
    data = response.json()


    for event in data:
        type = event["type"]
        repo_name = event["repo"]["name"]

        if type == "PushEvent":
            num_commits = len(event["payload"]["commits"])
            print(f"Pushed {num_commits} commit{"s" if num_commits != 1 else ""} to {repo_name}")

        elif type == "WatchEvent":
            print(f"Starred {repo_name}")
        elif type == "CreateEvent":
            if event["payload"]["ref_type"] == "repository":
                print(f"Created a new repository: {repo_name}")
        elif type == "ForkEvent":
            print(f"Forked {repo_name}")

if __name__ == "__main__":
    main()