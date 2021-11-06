from race_utils.half_quarter import HalfQuarterRace

if __name__ == '__main__':
    half_quarter_race = HalfQuarterRace()
    half_quarter_race.setup_race()
    print(half_quarter_race.dump())
    half_quarter_race.save_to_archive()
