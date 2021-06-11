#!python3
import re
import os

def format(values):
    while True:
        # replace space with comma for creation of xml file
        values = values.replace(' ',',') 
        #check to see if user entered correct number of values
        if int(values.count(',')) != 2:
            print('Please ensure your values look like: "x,x,x" or "x x x"')
            values = input()
        else:
            break
    return values

print('An XML file for your HUD will be generated automatically')
print('Your matrix values consist of three numbers, "0 0 5" is an example')

print('Enter matrix red: ')
red = format(input())
print('Enter matrix green: ')
green = format(input())
print('Enter matrix blue: ')
blue = format(input())

# change xml_location to the location of your xml file
# this can be found here on Windows: 'C:\Users\*you*\AppData\Local\Frontier Developments\Elite Dangerous\Options\Graphics'
xml_location = r''

f = open(xml_location + r'\GraphicsConfigurationOverride.xml',"w") # w = overwrite
print('Location entered: ' + xml_location + r'\GraphicsConfigurationOverride.xml')
f.write('''<?xml version="1.0" encoding="UTF-8" ?>
<GraphicsConfig>
    <GUIColour>
        <Default>
            <LocalisationName>Standard</LocalisationName>
            <MatrixRed>%s</MatrixRed>
            <MatrixGreen>%s</MatrixGreen>
            <MatrixBlue>%s</MatrixBlue>
        </Default>
    </GUIColour>
</GraphicsConfig>'''%(red,green,blue))
f.close()
print("File (should be) created.")
os.system("pause") # press any key to continue in cmd