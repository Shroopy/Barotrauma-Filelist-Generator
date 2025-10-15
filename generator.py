from pathlib import Path
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element

targetDir = input("Target directory to scan: ")
targetDir = Path(targetDir).as_posix()

name = targetDir.split("/")[-1]

filelist = ElementTree(Element("contentpackage", {"name":name}))

for rootdir, dirs, files in Path(targetDir).walk():
	dirs[:] = [d for d in dirs if not d.startswith('.')]
	for file in files:
		if file.endswith(".xml"):
			tree = ET.parse(str(rootdir) + "/" + file)
			root = tree.getroot()

			tagtypes = {
				"Item" : "Item",
				"Character" : "Character",
				"Afflictions" : "Afflictions",
				"backgroundcreatures" : "BackgroundCreaturePrefabs",
				"BallastFloraBehavior" : "BallastFlora",
				"CaveGenerationParameters" : "CaveGenerationParameters", 
				"Corpses" : "Corpses", 
				#"prefabs" : "Decals", 
				"EventManagerSettings" : "EventManagerSettings", 
				"Factions" : "Factions",
				"ItemAssembly" : "ItemAssembly", 
				"Jobs" : "Jobs", 
				"LevelGenerationParameters" : "LevelGenerationParameters", 
				"levelobjects" : "LevelObjectPrefabs",
				"locationtypes" : "LocationTypes",
				"MapGenerationParameters" : "MapGenerationParameters",
				"Missions" : "Missions", 
				"Conversations" : "NPCConversations", 
				"PersonalityTraits" : "NPCPersonalityTraits",
				"npcsets" : "NPCSets", 
				"Orders" : "Orders", 
				"OutpostConfig" : "OutpostConfig", 
				"prefabs" : "Particles", 
				"Randomevents" : "RandomEvents", 
				"RuinGenerationParameters" : "RuinConfig", 
				#"ServerExecutable", 
				"SkillSettings" : "SkillSettings", 
				"sounds" : "Sounds", 
				"StartItems" : "StartItems", 
				#"prefabs" : "Structure", 
				"Talents" : "Talents", 
				"TalentTrees" : "TalentTrees", 
				"infotexts" : "Text", 
				"TraitorMissions" : "TraitorMissions", 
				"Tutorials" : "Tutorials", 
				"style" : "UIStyle", 
				"UpgradeModules" : "UpgradeModules", 
				"WreckAIConfig" : "WreckAIConfig",
				#"Other"
			}
			if root.tag not in tagtypes:
				continue
			newtag = tagtypes[root.tag]
			
			line: str
			filepath = (str(rootdir.as_posix()) + "/" + file).replace(targetDir, "%ModDir%")
			fileElement = Element(newtag, {"file":filepath})

			fileElement.tag = fileElement.tag.replace("infotexts", "Text")
			fileElement.tag = fileElement.tag.replace("style", "UIStyle")

			filelist.getroot().append(fileElement) # type: ignore

ET.indent(filelist, '\t')
filelist.write("filelist.xml", xml_declaration=True)