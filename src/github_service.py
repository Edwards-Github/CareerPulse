import httpx
import asyncio

async def fetch_user_repos(username: str):
	headers = {"User-agent": "CareerPulse-App"}
	async with httpx.AsyncClient() as client:
		url = f"https://api.github.com/users/{username}/repos"
		response = await client.get(url, headers=headers)
		return response.json() # Returns a list of repo dicts

# 1. Wrap your "Top Level" code in an async function
async def main():
	username = "Edwards-Github"
	repos = await fetch_user_repos("Edwards-Github")

	print(f"--- Found {len(repos)} Repositories ---")

	for repo in repos:
	    name = repo['name']
	    url = repo['html_url']
	    stars = repo['stargazers_count']
	    
	    print(f"🚀 {name} | ⭐ Stars: {stars}")
	    print(f"🔗 Link: {url}\n")

if __name__ == "__main__":
	asyncio.run(main())