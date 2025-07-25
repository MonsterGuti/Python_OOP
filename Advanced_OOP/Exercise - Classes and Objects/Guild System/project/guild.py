from project import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        else:
            if player.guild != "Unaffiliated":
                return f"Player {player.name} is in another guild."
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        player_to_remove = next((p for p in self.players if p.name == player_name), None)
        if player_to_remove:
            self.players.remove(player_to_remove)
            player_to_remove.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_info = "\n".join(p.player_info() for p in self.players)
        return f"Guild: {self.name}\n{players_info}"
