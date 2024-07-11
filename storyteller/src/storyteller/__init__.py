from importlib import metadata

# Importing metadata to fetch the version of the storyteller-core package
from storyteller.config import StoryTellerConfig
# Importing StoryTellerConfig class from storyteller.config module
from storyteller.model import StoryTeller
# Importing StoryTeller class from storyteller.model module

# Defining the version of the storyteller-core package
__version__ = metadata.version("storyteller-core")
# Assigning the version to the __version__ variable

# Defining the list of all public objects in this module
__all__ = ["__version__", "StoryTellerConfig", "StoryTeller"]
# Including __version__, StoryTellerConfig, and StoryTeller in the __all__ list