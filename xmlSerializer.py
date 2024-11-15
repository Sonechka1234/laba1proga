from xml.etree.ElementTree import Element, SubElement, tostring, fromstring
from serializer import Serializer

class XmlSerializer(Serializer):
    def to_format(self, users: dict) -> str:
        root = Element("items")
        for item in users:
            item_element = SubElement(root, "item")
            for key, value in item.items():
                element = SubElement(item_element, key)
                element.text = str(value)
        return tostring(root, encoding="unicode")

    def from_format(data: dict) -> any:
        root = fromstring(data)
        result = []
        for item_element in root:
            item_dict = {}
            for element in item_element:
                item_dict[element.tag] = element.text
            result.append(item_dict)
        return result