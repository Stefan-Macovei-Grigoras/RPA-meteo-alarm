import xml.etree.ElementTree as ET
import pandas as pd
from io import StringIO


def process_xml(xml_string):
    # Parse XML directly from string
    root = ET.fromstring(xml_string)

    # Define namespaces
    namespaces = {'cap': 'urn:oasis:names:tc:emergency:cap:1.2'}

    # Extract regions
    regions = []
    for area in root.findall('.//cap:areaDesc', namespaces):
        regions.append(area.text)

    if not regions:
        return False

    # Write to Excel
    df = pd.DataFrame({'Region': regions})
    df.to_excel('regions.xlsx', index=False)

    return True


if __name__ == '__main__':
    pass
