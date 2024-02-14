import pandas as pd
import json

dict = {
	"Gear Train 1": {"Gear Ratio": 0, "Gear Type": ""},
	"Gear Train 2": {"Gear Ratio": 0, "Gear Type": ""},
	"Gear Train 3": {"Gear Ratio": 0, "Gear Type": ""},
			 }

def Challenge():
	t1Done = False
	t2Done = False
	t3Done = False
	
	try:
		file = open("gear_specs.csv")
	except:
		print("Files Missing")
		return

	gears = pd.read_csv(file)
	
	for line in gears["Gear Train"]:
		if line == 1:
			if not t1Done:
				index = gears.index[gears["Gear Train"] == 1].tolist()
				position = gears["Position"][index]
				t1DriverTeeth = gears["Number of Teeth"][index[0]]
				t1DrivenTeeth = gears["Number of Teeth"][index[-1]]
				
				dict["Gear Train 1"]["Gear Ratio"] = t1DrivenTeeth/t1DriverTeeth
				
				if dict["Gear Train 1"]["Gear Ratio"] < 1.0:
					dict["Gear Train 1"]["Gear Type"] = "Speed"
					
				elif dict["Gear Train 1"]["Gear Ratio"] == 1.0:
					dict["Gear Train 1"]["Gear Type"] = "Balanced"
					
				elif dict["Gear Train 1"]["Gear Ratio"] > 1.0:
					dict["Gear Train 1"]["Gear Type"] = "Torue"
					
				t1Done = True
				continue
		elif line == 2:
			if not t2Done:
				index = gears.index[gears["Gear Train"] == 2].tolist()
				position = gears["Position"][index]
				t2DriverTeeth = gears["Number of Teeth"][index[0]]
				t2DrivenTeeth = gears["Number of Teeth"][index[-1]]

				dict["Gear Train 2"]["Gear Ratio"] = t2DrivenTeeth/t2DriverTeeth

				if dict["Gear Train 2"]["Gear Ratio"] < 1.0:
					dict["Gear Train 2"]["Gear Type"] = "Speed"

				elif dict["Gear Train 2"]["Gear Ratio"] == 1.0:
					dict["Gear Train 2"]["Gear Type"] = "Balanced"

				elif dict["Gear Train 2"]["Gear Ratio"] > 1.0:
					dict["Gear Train 2"]["Gear Type"] = "Torue"

				t2Done = True
				continue
				
		elif line == 3:
			if not t3Done:
				index = gears.index[gears["Gear Train"] == 3].tolist()
				position = gears["Position"][index]
				t3DriverTeeth = gears["Number of Teeth"][index[0]]
				t3DrivenTeeth = gears["Number of Teeth"][index[-1]]

				dict["Gear Train 3"]["Gear Ratio"] = t3DrivenTeeth/t3DriverTeeth

				if dict["Gear Train 3"]["Gear Ratio"] < 1.0:
					dict["Gear Train 3"]["Gear Type"] = "Speed"

				elif dict["Gear Train 3"]["Gear Ratio"] == 1.0:
					dict["Gear Train 3"]["Gear Type"] = "Balanced"

				elif dict["Gear Train 3"]["Gear Ratio"] > 1.0:
					dict["Gear Train 3"]["Gear Type"] = "Torque"

				t3Done = True
				continue

	with open("gear_system_information.json", "w") as f:
		json.dump(dict, f, indent = 6)
	
Challenge()