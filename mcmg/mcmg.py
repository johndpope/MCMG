'''
	Markov Chain Music Generator
	
'''

import sys
music_xml_filename = 'D:\Projects\MCMG\MusicXML\The_dance_of_victory-Eluveitie\lg-155582393382959147.xml'

import xml.etree.ElementTree as ET
tree = ET.parse(music_xml_filename)
root = tree.getroot()


part = root.find('part')
part_id = part.get('id')
part_name = root.find("./part-list/score-part[@id='%s']" % part_id).find('part-name').text

PRINT_NOTES = 15
print 'First %d notes of part "%s":' % (PRINT_NOTES, part_name)
for note in part.iter('note'):
	step = note.find('pitch').find('step').text
	octave = note.find('pitch').find('octave').text
	type = note.find('type').text
	
	alter = note.find('pitch').find('alter')
	accidental = None
	if (alter == None or int(alter.text) == 0): 
		accidental = ''
	elif (int(alter.text) == 1):
		accidental = '#'
	elif (int(alter.text) == -1):
		accidental = 'b'
	else:
		accidental = '(alter value >1 or <-1)'

	print step + accidental + octave + ' ' + type
	
	PRINT_NOTES -= 1
	if (PRINT_NOTES == 0): 
		break