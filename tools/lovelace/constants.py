# Shared styling constants for Lovelace maintenance scripts.
# Keeping these in one place stops drift between utilities.

DEFAULT_CARD_MOD = """card_mod:
  style: |
    ha-card {
      background: linear-gradient(145deg, #1E3A5F 0%, #0D1B2A 100%);
      color: white;
      border-radius: 12px;
      box-shadow: 0 8px 16px rgba(30, 58, 95, 0.4);
      border: none;
      transition: all 0.3s ease;
    }
    ha-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 24px rgba(30, 58, 95, 0.5);
    }
    ha-tile-icon {
      filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
    }"""

# Map of YAML anchor references used in style files.
ANCHOR_TO_VALUE = {
    # Gradients
    "*gradient_navy": "linear-gradient(145deg, #1E3A5F 0%, #0D1B2A 100%)",
    "*gradient_slate": "linear-gradient(145deg, #334155 0%, #1E293B 100%)",
    "*gradient_teal": "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
    "*gradient_indigo": "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
    "*gradient_amber": "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
    "*gradient_rose": "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
    "*gradient_purple": "linear-gradient(145deg, #9C27B0 0%, #7B1FA2 100%)",
    # Shadows (RGB values)
    "*shadow_navy": "30, 58, 95",
    "*shadow_slate": "51, 65, 85",
    "*shadow_teal": "15, 118, 110",
    "*shadow_indigo": "79, 70, 229",
    "*shadow_amber": "217, 119, 6",
    "*shadow_rose": "225, 29, 72",
    "*shadow_purple": "156, 39, 176",
    "*shadow_dark": "0, 0, 0",
    "*shadow_light": "255, 255, 255",
}

# Modern Blue-Based Color Palette (from card_styles.yaml)
# Using actual values instead of YAML anchors since anchors don't work across files.
THEME_COLORS = {
    # Gradients - keeping the originals as-is since they're already the theme colors
    "linear-gradient(145deg, #1E3A5F 0%, #0D1B2A 100%)": (
        "linear-gradient(145deg, #1E3A5F 0%, #0D1B2A 100%)",
        "Navy gradient",
    ),
    "linear-gradient(145deg, #334155 0%, #1E293B 100%)": (
        "linear-gradient(145deg, #334155 0%, #1E293B 100%)",
        "Slate gradient",
    ),
    "linear-gradient(145deg, #0F766E 0%, #115E59 100%)": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Teal gradient",
    ),
    "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Indigo gradient",
    ),
    "linear-gradient(145deg, #D97706 0%, #B45309 100%)": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Amber gradient",
    ),
    "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Rose gradient",
    ),
    "linear-gradient(145deg, #9C27B0 0%, #7B1FA2 100%)": (
        "linear-gradient(145deg, #9C27B0 0%, #7B1FA2 100%)",
        "Purple gradient",
    ),
    # Shadow RGB values - keeping as-is
    "30, 58, 95": ("30, 58, 95", "Navy shadow"),
    "51, 65, 85": ("51, 65, 85", "Slate shadow"),
    "15, 118, 110": ("15, 118, 110", "Teal shadow"),
    "79, 70, 229": ("79, 70, 229", "Indigo shadow"),
    "217, 119, 6": ("217, 119, 6", "Amber shadow"),
    "225, 29, 72": ("225, 29, 72", "Rose shadow"),
    "156, 39, 176": ("156, 39, 176", "Purple shadow"),
    "0, 0, 0": ("0, 0, 0", "Dark shadow"),
    "255, 255, 255": ("255, 255, 255", "Light shadow"),
    # Hex color mappings to gradients
    "#1E3A5F": (
        "linear-gradient(145deg, #1E3A5F 0%, #0D1B2A 100%)",
        "Navy",
    ),
    "#0D1B2A": (
        "linear-gradient(145deg, #1E3A5F 0%, #0D1B2A 100%)",
        "Navy dark",
    ),
    "#334155": (
        "linear-gradient(145deg, #334155 0%, #1E293B 100%)",
        "Slate",
    ),
    "#1E293B": (
        "linear-gradient(145deg, #334155 0%, #1E293B 100%)",
        "Slate dark",
    ),
    "#0F766E": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Teal",
    ),
    "#115E59": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Teal dark",
    ),
    "#4F46E5": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Indigo",
    ),
    "#3730A3": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Indigo dark",
    ),
    "#D97706": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Amber",
    ),
    "#B45309": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Amber dark",
    ),
    "#FFB74D": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Amber light",
    ),
    "#FFA726": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Amber medium",
    ),
    "#E11D48": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Rose",
    ),
    "#BE123C": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Rose dark",
    ),
    "#9C27B0": (
        "linear-gradient(145deg, #9C27B0 0%, #7B1FA2 100%)",
        "Purple",
    ),
    "#7B1FA2": (
        "linear-gradient(145deg, #9C27B0 0%, #7B1FA2 100%)",
        "Purple dark",
    ),
    # Google Material Design colors mapped to theme
    "#4285F4": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Blue - Google Material",
    ),
    "#357ABD": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Blue Dark - Google Material",
    ),
    "#DB4437": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Red - Google Material",
    ),
    "#B23121": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Red Dark - Google Material",
    ),
    "#F4B400": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Yellow - Google Material",
    ),
    "#C79100": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Yellow Dark - Google Material",
    ),
    "#0F9D58": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Green - Google Material",
    ),
    "#0A7E3E": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Green Dark - Google Material",
    ),
    "#009688": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Teal - Material",
    ),
    "#1DB954": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Spotify Green",
    ),
    "#1AA34A": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Spotify Green Dark",
    ),
    "#42A5F5": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Blue Light - Material",
    ),
    "#64B5F6": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Blue Lighter - Material",
    ),
    "#66BB6A": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Green Light - Material",
    ),
    "#81C784": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Green Lighter - Material",
    ),
    "#E53935": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Red - Material",
    ),
    "#EF5350": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Red Medium - Material",
    ),
    "#FF7043": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Orange - Material",
    ),
    "#8E24AA": (
        "linear-gradient(145deg, #9C27B0 0%, #7B1FA2 100%)",
        "Purple - Material",
    ),
    "#AB47BC": (
        "linear-gradient(145deg, #9C27B0 0%, #7B1FA2 100%)",
        "Purple Medium - Material",
    ),
    "#26C6DA": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Cyan - Material",
    ),
    "#EC407A": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Pink - Material",
    ),
    "#5C6BC0": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Indigo - Material",
    ),
    "#B0BEC5": (
        "linear-gradient(145deg, #334155 0%, #1E293B 100%)",
        "Blue Gray - Material",
    ),
    "#90A4AE": (
        "linear-gradient(145deg, #334155 0%, #1E293B 100%)",
        "Blue Gray Medium - Material",
    ),
    "#78909C": (
        "linear-gradient(145deg, #334155 0%, #1E293B 100%)",
        "Blue Gray Dark - Material",
    ),
    "#607D8B": (
        "linear-gradient(145deg, #334155 0%, #1E293B 100%)",
        "Blue Gray Darker - Material",
    ),
    "#00C853": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Green Accent",
    ),
    "#64DD17": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Light Green Accent",
    ),
    "#AEEA00": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Lime Accent",
    ),
    "#FFD600": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Yellow Accent",
    ),
    "#FFAB00": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Amber Accent",
    ),
    "#FF6D00": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Orange Accent",
    ),
    "#DD2C00": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Deep Orange Accent",
    ),
    "#2962FF": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Blue Accent",
    ),
    "#304FFE": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Blue Accent Dark",
    ),
    "#6200EA": (
        "linear-gradient(145deg, #9C27B0 0%, #7B1FA2 100%)",
        "Deep Purple Accent",
    ),
    "#AA00FF": (
        "linear-gradient(145deg, #9C27B0 0%, #7B1FA2 100%)",
        "Purple Accent",
    ),
    "#C51162": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Pink Accent",
    ),
    "#D50000": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Red Accent",
    ),
    "#F06292": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Pink Medium - Material",
    ),
    "#9575CD": (
        "linear-gradient(145deg, #9C27B0 0%, #7B1FA2 100%)",
        "Deep Purple Medium - Material",
    ),
    "#7986CB": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Indigo Medium - Material",
    ),
    "#4DD0E1": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Cyan Medium - Material",
    ),
    "#4DB6AC": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Teal Medium - Material",
    ),
    "#81D4FA": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Blue Medium - Material",
    ),
    "#90CAF9": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Blue Light Medium - Material",
    ),
    "#A5D6A7": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Green Medium - Material",
    ),
    "#C5E1A5": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Light Green Medium - Material",
    ),
    "#E6EE9C": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Lime Medium - Material",
    ),
    "#FFF59D": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Yellow Medium - Material",
    ),
    "#FFE082": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Amber Medium Light - Material",
    ),
    "#FFAB91": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Deep Orange Medium - Material",
    ),
    "#CE93D8": (
        "linear-gradient(145deg, #9C27B0 0%, #7B1FA2 100%)",
        "Purple Light - Material",
    ),
    "#FFCDD2": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Red Light - Material",
    ),
    "#F8BBD0": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Pink Light - Material",
    ),
    "#E1BEE7": (
        "linear-gradient(145deg, #9C27B0 0%, #7B1FA2 100%)",
        "Purple Light Medium - Material",
    ),
    "#D1C4E9": (
        "linear-gradient(145deg, #9C27B0 0%, #7B1FA2 100%)",
        "Deep Purple Light - Material",
    ),
    "#C5CAE9": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Indigo Light - Material",
    ),
    "#BBDEFB": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Blue Light - Material",
    ),
    "#B3E5FC": (
        "linear-gradient(145deg, #4F46E5 0%, #3730A3 100%)",
        "Light Blue Light - Material",
    ),
    "#B2EBF2": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Cyan Light - Material",
    ),
    "#B2DFDB": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Teal Light - Material",
    ),
    "#C8E6C9": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Green Light - Material",
    ),
    "#DCEDC8": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Light Green Extra Light - Material",
    ),
    "#F0F4C3": (
        "linear-gradient(145deg, #0F766E 0%, #115E59 100%)",
        "Lime Extra Light - Material",
    ),
    "#FFF9C4": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Yellow Extra Light - Material",
    ),
    "#FFECB3": (
        "linear-gradient(145deg, #D97706 0%, #B45309 100%)",
        "Amber Extra Light - Material",
    ),
    "#FFE0B2": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Orange Extra Light - Material",
    ),
    "#FFCCBC": (
        "linear-gradient(145deg, #E11D48 0%, #BE123C 100%)",
        "Deep Orange Extra Light - Material",
    ),
    "#D7CCC8": (
        "linear-gradient(145deg, #334155 0%, #1E293B 100%)",
        "Brown Light - Material",
    ),
    "#CFD8DC": (
        "linear-gradient(145deg, #334155 0%, #1E293B 100%)",
        "Blue Gray Extra Light - Material",
    ),
}
