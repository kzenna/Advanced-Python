# Домашнее задание к лекции 1.2
# «Iterators. Generators. Yield»
#
# Кокурникова Лилия Фаритовна, 01.05.19
#

import json
import wikipedia
import hashlib

class FindCountry:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    if self.a <= len(json_data):
      country = json_data[self.a]['name']['common']
      ny = wikipedia.page(country)
      country_dict[country] = ny.url
      self.a += 1
      return country_dict
    else:
      raise StopIteration

def getMD5sum(fileName):
  m = hashlib.md5()
  fd = open(fileName, 'rb')
  b = fd.read()
  m.update(b)
  fd.close()
  return print(m.hexdigest())

if __name__ == '__main__':
  with open("countries.json") as datafile:
    json_data = json.load(datafile)
  myiter = iter(FindCountry())
  country_dict = {}
  for ny in myiter:
    ny
  with open("countries_url", "w", encoding="utf-8") as file:
    json.dump(country_dict, file)
  with open("countries_url") as datafile:
    json_data_url = json.load(datafile)
  getMD5sum('countries_url')