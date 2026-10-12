from requests import get
a = get("https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.st.com/en/development-tools/stm32cubeide.html&ved=2ahUKEwjggajQ7aKXAxVqQvEDHTRVJZQQFnoECA8QAQ&usg=AOvVaw17XOKEGK4FjDzWT8PhSQf4")
f = open("data.html", "w")
f.write(a.text)