import re
import emoji
from src import ModuleManager, utils

@utils.export("channelset", utils.BoolSetting("demojize",
    "Translate emojis in to their text descriptions"))
class Module(ModuleManager.BaseModule):
    @utils.hook("command.regex")
    @utils.kwarg("pattern", re.compile(".+"))
    @utils.kwarg("expect_output", False)
    @utils.kwarg("ignore_action", False)
    @utils.kwarg("command", "demojize")
    def demojize(self, event):
        if event["target"].get_setting("demojize", False):
            demojised = emoji.demojize(event["message"])
            if not demojised == event["message"]:
                if event["action"]:
                    format = "* %s %s"
                else:
                    format = "<%s> %s"
                event["stdout"].write(format % (event["user"].nickname,
                    demojised))

