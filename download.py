import os, requests, json

os.system("cls")

def main():
	with open("data.json", "r", encoding="UTF-8") as f:
		data = json.loads(f.read())

	used = []

	for i in range(1, len(data)):
		url = data[str(i)]["links"]["attribute"]

		if url not in used:
			used.append(url)
			img = requests.get(data[str(i)]["links"]["attribute"])

			with open(f"imgs/attribute/{str(i)}.png", "wb") as f:
				f.write(img.content)

if __name__ == "__main__":
	main()