import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Bilal</name>
  <phone type="intl">+92 324 0003300</phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Phone:', tree.find('phone').text)
print('Attr:', tree.find('email').get('hide'))
