from project.guild_halls.base_guild_hall import BaseGuildHall
from project.guild_halls.combat_hall import CombatHall
from project.guild_halls.magic_tower import MagicTower
from project.guild_members.base_guild_member import BaseGuildMember
from project.guild_members.mage import Mage
from project.guild_members.warrior import Warrior


class GuildMaster:
    VALID_MEMBERS = {
        "Warrior": Warrior,
        "Mage": Mage
    }

    VALID_HALLS = {
        "CombatHall": CombatHall,
        "MagicTower": MagicTower
    }

    def __init__(self):
        self.members: list[BaseGuildMember] = []
        self.guild_halls: list[BaseGuildHall] = []

    def add_member(self, member_type: str, member_tag: str, member_gold: int):
        if member_type not in self.VALID_MEMBERS:
            raise ValueError("Invalid member type!")

        member = next((m for m in self.members if m.tag == member_tag), None)
        if member:
            raise ValueError(f"{member_tag} has already been added!")

        self.members.append(self.VALID_MEMBERS[member_type](member_tag, member_gold))
        return f"{member_tag} is successfully added as {member_type}."

    def add_guild_hall(self, guild_hall_type: str, guild_hall_alias: str):
        if guild_hall_type not in self.VALID_HALLS:
            raise ValueError("Invalid guild hall type!")

        hall = next((h for h in self.guild_halls if h.alias == guild_hall_alias), None)
        if hall:
            raise ValueError(f"{guild_hall_alias} has already been added!")

        self.guild_halls.append(self.VALID_HALLS[guild_hall_type](guild_hall_alias))
        return f"{guild_hall_alias} is successfully added as a {guild_hall_type}."

    def assign_member(self, guild_hall_alias: str, member_type: str):
        guild_hall = next((h for h in self.guild_halls if h.alias == guild_hall_alias), None)
        if not guild_hall:
            raise ValueError(f"Guild hall {guild_hall_alias} does not exist!")

        member_class = self.VALID_MEMBERS[member_type]
        member = next((m for m in self.members if isinstance(m, member_class)), None)
        if not member:
            raise ValueError("No available members of the type!")

        if len(guild_hall.members) >= guild_hall.max_member_count:
            return "Maximum member count reached. Assignment is impossible."

        self.members.remove(member)
        guild_hall.members.append(member)

        return f"{member.tag} was assigned to {guild_hall_alias}."

    @staticmethod
    def practice_members(guild_hall: BaseGuildHall, sessions_number: int):
        for member in guild_hall.members:
            for _ in range(sessions_number):
                member.practice()

        total_skill_level = sum(member.skill_level for member in guild_hall.members)
        return (f"{guild_hall.alias} members have {total_skill_level}"
                f" total skill level after {sessions_number} practice session/s.")

    def unassign_member(self, guild_hall: BaseGuildHall, member_tag: str):
        member = next((m for m in guild_hall.members if m.tag == member_tag), None)
        if not member or member.skill_level == 10:
            return "The unassignment process was canceled."

        guild_hall.members.remove(member)
        self.members.append(member)
        return f"Unassigned member {member_tag}."

    def guild_update(self, min_skill_level_value: int):
        for hall in self.guild_halls:
            hall.increase_gold(min_skill_level_value)

        sorted_halls = sorted(self.guild_halls, key=lambda h: (-len(h.members), h.alias))

        result = [
            "<<<Guild Updated Status>>>",
            f"Unassigned members count: {len(self.members)}",
            f"Guild halls count: {len(self.guild_halls)}"
        ]

        for hall in sorted_halls:
            result.append(f">>>{hall.status()}")

        return "\n".join(result)

