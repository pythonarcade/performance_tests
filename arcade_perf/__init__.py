import os
from pathlib import Path
import arcade

# Root of the repository
PACKAGE_ROOT= Path(__file__).parent.resolve()
# Package directory
PROJECT_ROOT = PACKAGE_ROOT.parent
# Resources directory
RESOURCES_ROOT = PACKAGE_ROOT / "resources"
# Output directory
OUT_DIR = PROJECT_ROOT / "output"

arcade.resources.add_resource_handle("textures", RESOURCES_ROOT)

# We don't want pygame support message in logs
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
