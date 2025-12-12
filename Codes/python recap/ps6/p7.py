post = input("Write your post: ")

# Normalize both strings to lowercase for comparison
if "aditya" in post.lower():
    index = post.lower().index("aditya")
    print(f"Yes, it talks about '{post}' at index {index}")
else:
    print("No mention of Aditya found.")