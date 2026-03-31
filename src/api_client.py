import httpx
import asyncio

async def check_github():
	# Use 'async with' to properly open and close the client
	async with httpx.AsyncClient() as client:
		# Now you can use the 'client' variable to make calls
		response = await client.get("https://api.github.com/")
		print(f"GitHub API Status: {response.status_code}")

if __name__ == "__main__":
	asyncio.run(check_github())