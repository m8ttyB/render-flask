import mechanicalsoup


def check_bikes(data):
  for k in data.keys():
    url = data[k]["url"]
    data[k]["in_stock"] = _is_bike_available(url)
  return data


def _is_bike_available(url):
  browser = mechanicalsoup.Browser()
  page = browser.get(url)
  tag = page.soup.select(".btn-full")[0]
  return 'Out Of Stock' != tag.text
