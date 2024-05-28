#!/usr/bin/env python3
'''3. Serializing and Deserializing with XML'''


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    '''serialize the dictionary into XML and\\
        save it to the given filename'''
    root=ET.Element("data")
    for key, value in dictionary.items():
        enfant = ET.Element(key)
        child.text = str(value)
        root.append(enfant)

    arbre = ET.ElementTree(root)

    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def deserialize_from_xml(filename):
    ET.parse(filename)
    root = tree.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    return data
