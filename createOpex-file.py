import csv
import xml.etree.ElementTree as ET

# Define the XML namespace
namespace = 'http://www.openpreservationexchange.org/opex/v1.2'
oai_schema = 'http://www.openarchives.org/OAI/2.0/oai_dc/ oai_dc.xsd'
dc_namespace = 'http://purl.org/dc/elements/1.1/'
oai_namespace = 'http://www.openarchives.org/OAI/2.0/oai_dc/'
xml_namespace = 'http://www.w3.org/2001/XMLSchema-instance'

# Open the CSV file
with open('PHIL-20200930-Deliverable.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # Skip the header row
    header = next(csv_reader)

    # Loop through each row in the CSV file
    for row in csv_reader:
        # Get the values from columns A and B
        box = row[0]
        description = row[1]

        # Create a new XML element with a fixed name
        element1 = ET.Element('opex:SourceID')

        # Set the text of the element to the first value
        element1.text = box

        # Create a new XML element with a fixed name and value that includes the first value
        element2 = ET.Element('dc:title')
        element2.text = 'Box ' + box

        # Create a new XML element with a fixed name and text of the second value
        element3 = ET.Element('dc:description')
        element3.text = description

        # Create a new XML parent element with a fixed name
        brother_element = ET.Element('opex:Transfer')

        # Create a new XML parent element with a fixed name
        sister_element = ET.Element('opex:DescriptiveMetadata')

        little_sister_element = ET.Element('oai_dc:dc', attrib={'xsi:schemaLocation': oai_schema, 'xmlns:dc':dc_namespace, 'xmlns:oai_dc':oai_namespace, 'xmlns:xsi':xml_namespace})

        # Add the first element to the brother, the second and third to the little sister, and the little sister to the sister element 
        brother_element.append(element1)
        little_sister_element.append(element2)
        little_sister_element.append(element3)
        sister_element.append(little_sister_element)

        # Create a new XML element tree with the parent element as the root
        root = ET.Element('opex:OPEXMetadata', attrib={'xmlns:opex': namespace})
        root.append(brother_element)
        root.append(sister_element)

        # Create a new XML file with a name based on the first value
        filename = box + '.opex'
        tree = ET.ElementTree(root)
        tree.write(filename, xml_declaration=True, encoding='utf-8')
