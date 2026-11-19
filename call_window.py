"""Compute the daily 'call window': hours when you (in the U.S.) are awake and
not at work AND your parents (abroad) are awake.

Assumptions (edit to match your own life):
- Everyone is awake 07:00-23:00 local time.
- You work 09:00-17:00 on weekdays, so those hours are not free.
- Offsets are hours ahead of U.S. Eastern Time.
"""

AWAKE = (7.0, 23.0)
WORK = (9.0, 17.0)

# Hours ahead of U.S. Eastern. November = Eastern Standard Time (UTC-5);
# summer = Eastern Daylight Time (UTC-4). India and China do not use daylight saving.
OFFSETS = {
    "India": {"nov": 10.5, "summer": 9.5},
    "China": {"nov": 13.0, "summer": 12.0},
}


def free_minutes_us(weekday=True):
    """Minutes of the U.S. day (0-1440) when you are awake and free."""
    mins = set(range(int(AWAKE[0] * 60), int(AWAKE[1] * 60)))
    if weekday:
        mins -= set(range(int(WORK[0] * 60), int(WORK[1] * 60)))
    return mins


def parent_awake(us_minute, offset_hours):
    local = (us_minute + offset_hours * 60) % 1440
    return AWAKE[0] * 60 <= local < AWAKE[1] * 60


def call_window_hours(offset_hours, weekday=True):
    mins = [m for m in free_minutes_us(weekday) if parent_awake(m, offset_hours)]
    return len(mins) / 60


if __name__ == "__main__":
    print("country,season,weekday_call_window_hrs,weekend_call_window_hrs")
    for country, seasons in OFFSETS.items():
        for season, off in seasons.items():
            print(f"{country},{season},{call_window_hours(off, True):.1f},{call_window_hours(off, False):.1f}")
