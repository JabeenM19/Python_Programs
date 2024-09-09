#  application should run from the command line, so cli 
# accept github user name:The user should be able to: Provide the GitHub username as an argument when running the CLI

#Making API Requests to GitHub: You'll need to fetch data from the GitHub API using requests or another HTTP library.
# fetch user's recent activity using github API and display it in the terminal: You can use the following endpoint to fetch the user’s activity:
# https://api.github.com/users/<username>/events
# Example: https://api.github.com/users/kamranahmedse/events


#you don't need Flask for this task.
'''Your CLI tool only needs to fetch data from the GitHub API and display it in the terminal. Flask is a web framework used for building web applications, 
but this task is strictly about building a command-line interface (CLI) tool, so Flask is unnecessary here.'''

import argparse # cli it will parse our arguments:This will allow the user to pass their GitHub username as an argument from the command line.
import requests # to make http requests
import sys # to exit the script safely

class user_ins():
    def __init__(self,user_name):
        self.user_name= user_name
        self.api_url = f'https://api.github.com/users/{self.user_name}/events'

    def get_recent_acts(self):
        try:
            response = requests.get(self.api_url)
            return response.json() # Parse the json response
        except requests.exceptions.RequestException as e:
            print(f"Error: Unable to connect to GitHub API. {e}")
            sys.exit(1)
    
    def display_recent_acts(self):
        events = self.get_recent_acts()
        if events:
            print(f"Recent GitHub Activity for user: {self.user_name}")
            print("\n")
            for event in events[:10]: #display the most recent 10 events 
                event_type = event['type']  # all this data is requested from us through github api
                repo_name = event['repo']['name']
                created_at = event['created_at']
                print(f"Event: {event_type} | Repo: {repo_name} | Date: {created_at}")
        else:
            print(f"No recent activity found for user '{self.user_name}'.")

def main():
        parser = argparse.ArgumentParser(description="Fetch a user's recent GitHub activity.")
        parser.add_argument("username",help="GitHub username") # ye wo arguments hain jinko hamein parse karna hai: CLI example mein, jab aap argument parse karte hain, iska matlab hota hai input ko samajhna aur usko alag-alag arguments ke roop mein tod kar use karna.
        args = parser.parse_args()
        # Create an instance of user_ins class with the provided username
        fetcher = user_ins(args.username)
        
        # Fetch and display the recent activity
        fetcher.display_recent_acts()
if __name__ == "__main__":
    main()


'''sample output:
Event: PushEvent | Repo: user/repo1 | Date: 2024-09-07T12:34:56Z
Event: PullRequestEvent | Repo: user/repo2 | Date: 2024-09-07T11:25:42Z
Event: ForkEvent | Repo: user/repo3 | Date: 2024-09-06T18:15:10Z
Event: IssuesEvent | Repo: user/repo4 | Date: 2024-09-06T14:08:23Z
Event: WatchEvent | Repo: user/repo5 | Date: 2024-09-06T09:47:35Z
Event: CreateEvent | Repo: user/repo6 | Date: 2024-09-05T22:39:51Z
Event: DeleteEvent | Repo: user/repo7 | Date: 2024-09-05T20:20:34Z
Event: ReleaseEvent | Repo: user/repo8 | Date: 2024-09-05T16:11:07Z
Event: MemberEvent | Repo: user/repo9 | Date: 2024-09-05T13:55:17Z
Event: GollumEvent | Repo: user/repo10 | Date: 2024-09-05T09:22:18Z
'''

'''parse ka matlab:
"Parse" ka matlab hai kisi cheez ko analyze karna ya uske different parts ko samajhna. Programming mein, jab hum "parse" bolte hain, iska matlab hota hai data ko ek specific format se lekar usse readable ya usable form mein convert karna.

Ek example lete hain: Agar aapke paas ek string hai "age=25", aur aap usko "parse" karte hain, to aap usko do parts mein tod kar samajhte hain — ek "age" jo key hai, aur "25" jo value hai.

CLI example mein, jab aap argument parse karte hain, iska matlab hota hai input ko samajhna aur usko alag-alag arguments ke roop mein tod kar use karna.
'''
