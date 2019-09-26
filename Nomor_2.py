from bs4 import BeautifulSoup
import requests
import pandas as pd 

r = requests.get("http://digidb.io/digimon-list")
soup = BeautifulSoup(r.content, 'html.parser')
data = soup.select('tbody tr')

no = []
digimon = []
image = []
stage = []
typex = []
attribute = []
memory = []
equip_slot = []
hp = []
sp = []
atk = []
defx = []
intx = []
spd = []
for row in data:
    no.append((row.td.text)[1:])
    digimon.append(row.td.find_next_sibling().a.text.capitalize())
    image.append(row.td.find_next_sibling().img['src'])
    stage.append(row.td.find_next_sibling().find_next_sibling().text)
    typex.append(row.td.find_next_sibling().find_next_sibling().find_next_sibling().text)
    attribute.append(row.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
    memory.append(row.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
    equip_slot.append(row.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
    hp.append(row.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
    sp.append(row.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
    atk.append(row.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
    defx.append(row.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
    intx.append(row.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)
    spd.append(row.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().text)

df = pd.DataFrame({
    'no' : no,
    'digimon' : digimon,
    'image' : image,
    'stage' : stage,
    'type' : typex,
    'attribute' : attribute,
    'memory' : memory,
    'equip slots' : equip_slot,
    'hp' : hp,
    'sp' : sp,
    'atk' : atk,
    'def' : defx,
    'int' : intx,
    'spd' : spd

})
df.to_json('digimon.json', orient='records')