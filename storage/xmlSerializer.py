from xml.etree.ElementTree import Element, SubElement, tostring, fromstring
from xml.dom.minidom import parseString
from storage.serializer import Serializer

class XmlSerializer(Serializer):
    def to_format(self, users) -> str:
        root = Element("Users")
        for  user in users:
            user_element = Element(user.__class__.__name__)
            user_id_element = SubElement(user_element, "user_id")
            user_id_element.text = str(user.user_id)
            name_element = SubElement(user_element, "name")
            name_element.text = user.name
            email_element = SubElement(user_element, "email")
            email_element.text = user.email
            age_element = SubElement(user_element, "age")
            age_element.text = str(user.age)
            root.append(user_element)
        raw_xml = tostring(root, encoding='unicode')

        dom = parseString(raw_xml)
        pretty_xml = dom.toprettyxml(indent = '     ')
        return pretty_xml

    def from_format(self, data) -> list:
        root = fromstring(data)
        users = []
        for user_element in root:
            user_type = user_element.tag
            user_id = int(user_element.find('user_id').text)
            email = user_element.find('email').text
            name = user_element.find('name').text
            age = int(user_element.find('age').text)
            
            user_data = {
                "type": user_type,
                "user_id": user_id,
                "name": name,
                "email": email,
                "age": age,
            }
            users.append(user_data)
        return users
    
    def get_format(self) -> str:
        return 'xml'