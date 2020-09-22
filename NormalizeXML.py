import os
import xml.etree.ElementTree as ET

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def normalize_tags(root):
    root.tag = root.tag.lower()
    for child in root:
        normalize_tags(child)


def normalize_attr(root):
    ListAttr = []
    for attr, value in root.attrib.items():
        _row = {"attr": attr, "value": value}
        ListAttr.append(_row)
    for el in ListAttr:
        root.attrib.pop(el.get("attr"))

        value = el.get("value")
        attr = el.get("attr").lower()
        # Additional conversion of values
        if attr == 'catalogid' or attr == 'DocumentId' or attr == 'spid':
            value = value.lower()
        root.set(attr, value)
    for child in root:
        normalize_attr(child)


def main():
    print(f"{bcolors.OKBLUE}Work dir: {os.getcwd()}")
    for in_file in os.listdir(os.getcwd()):
        if os.path.isfile(in_file) and in_file.endswith(".xml"):
            print(f"{bcolors.HEADER}Input: {in_file}")
            tree = ET.parse(in_file)
            root = tree.getroot()

            normalize_tags(root)
            normalize_attr(root)
            filename, file_extension = os.path.splitext(in_file)
            out_file = f"{filename}_new{file_extension}"
            print(f"{bcolors.OKGREEN}Output: {out_file}")
            if os.path.isfile(out_file):
                os.remove(out_file)
            _xml_tree = ET.ElementTree(root)  # записываем дерево в файл
            _xml_tree.write(out_file, encoding='utf-8', xml_declaration=True)  # сохраняем файл

if __name__ == '__main__':
    main()