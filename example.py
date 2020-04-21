from PyScrap import scrapper

PyScrap = scrapper.scrapper()

a_elements = PyScrap.find_elements_by_tag_name("http://emanuelepiatti.altervista.org", "h1")
print(a_elements)