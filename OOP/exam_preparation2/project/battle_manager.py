from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    mapper_zone = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}
    mapper_ship = {"RoyalBattleship": RoyalBattleship, "PirateBattleship": PirateBattleship}

    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in self.mapper_zone:
            raise Exception("Invalid zone type!")

        zone = [z for z in self.zones if z.code == zone_code]

        if zone:
            raise Exception("Zone already exists!")

        zone = self.mapper_zone[zone_type](zone_code)
        self.zones.append(zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.mapper_ship:
            raise Exception(f"{ship_type} is an invalid type of ship!")
        ship = self.mapper_ship[ship_type](name, health, hit_strength)
        self.ships.append(ship)
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if ((isinstance(ship, PirateBattleship) and isinstance(zone, RoyalZone)) or
                 (isinstance(ship, RoyalBattleship) and isinstance(zone, PirateZone))):
            ship.is_attacking = False
        else:
            ship.is_attacking = True

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        try:
            ship = [s for s in self.ships if s.name == ship_name][0]
        except IndexError:
            return "No ship with this name!"
        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        sorted_attackers = sorted([s for s in zone.ships if s.is_attacking and (zone.type == s.type)],
                                  key=lambda s: -s.hit_strength)
        sorted_targets = sorted([s for s in zone.ships if not s.is_attacking and (zone.type != s.type)],
                                key=lambda s: -s.health)

        if not sorted_attackers or not sorted_targets:
            return "Not enough participants. The battle is canceled."

        attacker = sorted_attackers[0]
        target = sorted_targets[0]

        attacker.attack()
        target.take_damage(attacker)

        if target.health <= 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f"{target.name} lost the battle and was sunk."

        if attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."



    def get_statistics(self):
        available_ships_name = [s.name for s in self.ships if s.is_available]
        result = f"Available Battleships: {len(available_ships_name)}\n"
        result += f"#{', '.join(available_ships_name)}#\n" if available_ships_name else ""
        order_zone = sorted(self.zones,key=lambda z: z.code)

        result += "***Zones Statistics:***\n"
        result += f"Total Zones: {len(self.zones)}\n"
        for zone in order_zone:
            result += zone.zone_info() + "\n"
        # return result[:-1]
        return result.strip()