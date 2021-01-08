# match
- match duration (duration.seconds)

# match.Team (match.blue_team / match.red_team)
- team_win (win -> int(false/true))
- team side (side.name)
- team_barons (baron_kills)
- team dragons (dragon_kills)
- team heralds (rift_herald_kills)
- team turrents (tower_kills)
- team inhibitor (inhibitor_kills)

# for match.participantsStats (participant.stats for loop of match.Team.participants)
- team kills (kills)
- team assists (assists)
- team deaths (deaths)
- team damage_dealt_to_objectives (damage_dealt_to_objectives)
- team damage_dealt_to_turrets (damage_dealt_to_turrets)
- team damage_self_mitigated (damage_self_mitigated)
- team physical_damage_dealt_to_champions
- team magic_damage_dealt_to_champions
- total gold earned (gold_earned)
- team vision score (vision_score)
- total_time_crowd_control_dealt
- 

# for match.ParticipantTimeline (participant.timeline) ou cumulative_timeline
- team_creeps_per_min_deltas_0_10
- team_creeps_per_min_deltas_10_20
- team_xp_per_min_deltas_0_10
- team_xp_per_min_deltas_10_20