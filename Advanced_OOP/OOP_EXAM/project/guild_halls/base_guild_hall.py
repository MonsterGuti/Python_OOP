from abc import ABC, abstractmethod

from project.guild_members.base_guild_member import BaseGuildMember


class BaseGuildHall(ABC):
    def __init__(self, alias: str):
        self.alias = alias
        self.members: list[BaseGuildMember] = []
    
    @property
    def alias(self):
        return self.__alias
    
    @alias.setter
    def alias(self, value):
        trimmed_value = value.strip()
        if len(trimmed_value) <= 1:
            raise ValueError("Guild hall alias is invalid!")
        if not all(ch.isalpha() or ch == ' ' for ch in trimmed_value):
            raise ValueError("Guild hall alias is invalid!")
        self.__alias = trimmed_value

    @property
    @abstractmethod
    def max_member_count(self) -> int:
        pass


    def calculate_total_gold(self):
        if not self.members:
            return 0
        total_gold = sum([m.gold for m in self.members])
        return total_gold

    def status(self):
        if self.members:
            member_tags = sorted(member.tag for member in self.members)
            members = " ".join(f"*{tag}" for tag in member_tags)
        else:
            members = "N/A"

        total_gold = sum(member.gold for member in self.members)
        return f"Guild hall: {self.alias}; Members: {members}; Total gold: {total_gold}"

    @abstractmethod
    def increase_gold(self, min_skill_level_value: int):
        pass

