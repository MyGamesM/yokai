import os #, requests, json
# from bs4 import BeautifulSoup as bs

os.system("cls")

def main():
	pass
	# with open("data.json", "r", encoding="UTF-8") as f:
	# 	data = json.loads(f.read())
	
	# used = []

	# for i in range(1, len(data)):
	# 	item = data[str(i)]["links"]["attribute"]
	# 	if item not in used:
	# 		print(item[57:-9])
	# 		used.append(item)

	### WRITE DATA.JSON
	# foods, links, names = [], [], []
	# data2 = {}

	# with open("txts/foods.txt", "r", encoding="UTF-8") as f:
	# 	foods = f.read().splitlines()

	# with open("txts/links.txt", "r", encoding="UTF-8") as f:
	# 	links = f.read().splitlines()

	# with open("txts/names.txt", "r", encoding="UTF-8") as f:
	# 	names = f.read().splitlines()
	
	# with open("data.json", "r", encoding="UTF-8") as f:
	# 	data = json.loads(f.read())
	
	# for i in range(len(foods)):
	# 	data2[str(i + 1)] = {
	# 			"name": names[i],
	# 			"food": foods[i],
	# 			"rank": data[str(i + 1)]["links"]["rank"][62:-9],
	# 			"tribe": data[str(i + 1)]["links"]["tribe"][57:-10],
	# 			"attribute": data[str(i + 1)]["links"]["attribute"][57:-9],
	# 		}
		
	# for i in range(len(links)):
	# 	if i == 223: break
	# 	i = i * 4
	# 	data2[f"{(int(i / 4)) + 1}"]["links"] = {
	# 		"icon": links[i],
	# 		"rank": links[i + 1],
	# 		"tribe": links[i + 2],
	# 		"attribute": links[i + 3]
	# 	}
		
	# data2 = str(data)

	# data2 = data.replace("'", '"')

	# with open("data2.json", "w", encoding="UTF-8") as f:
	# 	f.write(json.dumps(data2))

	# url = "https://yokaiwatch.fandom.com/wiki/List_of_Yo-kai_by_Medallium_Number_(Yo-kai_Watch)"

	# soup = bs(requests.get(url).text, 'html.parser')

	### NAMES/FOODS

	# foods = []

	# tables = soup.find_all("table", class_="main roundy")

	# for table in tables:
	# 	trs = table.find_all("tr")
	# 	trs.pop(0)
	# 	for tr in trs:
	# 		foods.append(tr.find_all("td")[2].text)

	# with open("names.txt", "w") as f:
	# 	for food in foods:
	# 		f.write(food)

	### USED TO GET LINKS
	# tables = soup.find_all("table", class_="main roundy")

	# with open("a.html", "r", encoding="UTF-8") as f:
	# 	soup = bs(f.read(), "html.parser")

	# href = []

	# for img in soup.find_all("img"):
	# 	if img.get("data-src") != None:
	# 		href.append(img.get("data-src"))
	# 	else:
	# 		href.append(img.get("src"))

	# with open("links.txt", "w", encoding="UTF-8") as f:
	# 	for link in href:
	# 		f.write(f"{str(link)}\n")

if __name__ == "__main__":
	main()