import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    response.raise_for_status()

    print("✅ API request successful.")
  
    data = response.json()  # Convert response to Python list/dict
    print(f"📊 Total records fetched: {len(data)}")

    print("\n🔍 Sample Records:\n", data[:2])

    user_posts = [post for post in data if post["userId"] == 1]

    print(f"\n📝 Posts by userId=1 (Total: {len(user_posts)}):")
    for post in user_posts[:3]:  # Show first 3
        print(f"ID: {post['id']} | Title: {post['title']}")

except requests.exceptions.HTTPError as http_err:
    print("❌ HTTP error occurred:", http_err)
except requests.exceptions.ConnectionError:
    print("❌ Connection error. Check your internet.")
except requests.exceptions.Timeout:
    print("❌ Request timed out.")
except Exception as e:
    print("❌ An error occurred:", e)
