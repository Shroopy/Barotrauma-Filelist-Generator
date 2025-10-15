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

			if root.tag not in ("Item", "Character", "Afflictions", "BackgroundCreaturePrefabs", "BallastFlora", "CaveGenerationParameters", "Corpses", "Decals", "EventManagerSettings", "Factions", "ItemAssembly", "Jobs", "LevelGenerationParameters", "LevelObjectPrefabs","LocationTypes","MapGenerationParameters", "Missions", "NPCConversations","NPCPersonalityTraits", "NPCSets", "Orders", "OutpostConfig", "Particles", "RandomEvents", "RuinConfig", "ServerExecutable", "SkillSettings", "Sounds", "StartItems", "Structure", "Talents", "TalentTrees", "Text", "TraitorMissions", "Tutorials", "UIStyle", "UpgradeModules", "WreckAIConfig", "Other"):
				continue
			
			line: str
			filepath = (str(rootdir.as_posix()) + "/" + file).replace(targetDir, "%ModDir%")
			fileElement = Element(root.tag, {"file":filepath})

			filelist.getroot().append(fileElement) # type: ignore

ET.indent(filelist, '\t')
filelist.write("filelist.xml", xml_declaration=True)