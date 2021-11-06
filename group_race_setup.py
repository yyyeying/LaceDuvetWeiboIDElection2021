from race_utils.group import GroupRace


if __name__ == '__main__':
    group_race = GroupRace()
    group_race.setup_race()
    print(group_race.dump())
    group_race.save_to_archive()
