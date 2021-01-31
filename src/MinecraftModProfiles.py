import json
from src.exceptions.Exceptions import ProfileNotFoundError
import os
import shutil


class MinecraftModProfiles:
    def __init__(self):
        try:
            with open("settings.json", "r") as settings:
                self.settings = json.loads(settings.read())
        except FileNotFoundError:
            open("settings.json", "w")\
                .write(json.dumps(
                    {
                        "profiles": {},
                        "minecraft": f"{os.environ['appdata']}\\.minecraft"
                    }
                )
            )

    def setting(self, **kwargs):
        for key, value in kwargs.items():
            if key == "minecraft":
                self.settings["minecraft"] = value
        open("settings.json", "w").write(json.dumps(self.settings))

    def changeProfile(self, name):
        try:
            path = self.settings["profiles"][name]

            for i in os.listdir(self.settings["minecraft"]):
                os.remove(self.settings["minecraft"] + "\\" + i)

            for i in os.listdir(path):
                shutil.copyfile(path+i, self.settings["minecraft"]+"\\mods")
        except KeyError:
            raise ProfileNotFoundError(f"Setting Profile {name}", f"Profile {name} not found")


if __name__ == "__main__":
    import GUI
    g = GUI.GUI()