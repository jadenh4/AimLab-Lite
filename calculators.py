import math

def edpi(dpi: float, sensitivity: float) -> float:
    return dpi * sensitivity

def cm_per_360(dpi: float, sensitivity: float, yaw: float = 0.022) -> float:
    """
    Approximation:
    - yaw is "degrees per mouse count" scale (varies by game).
    - 1 inch = 2.54 cm
    - counts per inch = dpi
    - degrees per count = sensitivity * yaw
    counts for 360 = 360 / (sensitivity * yaw)
    inches = counts / dpi
    cm = inches * 2.54
    """
    if dpi <= 0 or sensitivity <= 0 or yaw <= 0:
        return 0.0
    counts = 360.0 / (sensitivity * yaw)
    inches = counts / dpi
    return inches * 2.54

# Simple ratio table (starter version)
GAME_SCALE = {
    "Valorant": 0.07,
    "CS2": 0.022,
    "Overwatch": 0.0066,
    "Apex": 0.022,
    "Fortnite": 0.005555,
}

def convert_sens(source_game: str, target_game: str, source_sens: float) -> float:
    """
    Convert based on relative scale constants (approx).
    This is NOT perfect, but it’s a solid v1 and very expandable.
    """
    if source_sens <= 0:
        return 0.0
    s = GAME_SCALE.get(source_game)
    t = GAME_SCALE.get(target_game)
    if not s or not t:
        return 0.0
    # Keep same degrees-per-count feel:
    # source_sens * s  == target_sens * t  => target_sens = source_sens * (s / t)
    return source_sens * (s / t)
