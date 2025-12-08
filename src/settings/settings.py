from typing import Literal

LocationType = Literal['l1', 'menu']
PlayersType = Literal['1', '2']
InputType = Literal['keyboard', 'joycon']

class Settings:
    """Main game state manager."""
    
    def __init__(self):
        self.location: LocationType = 'menu' 
        self._players: PlayersType = '1'
        self._input: InputType = 'keyboard'

    def update_location(self, location: LocationType):
        """Update the location."""
        self.location = location
    
    def get_location(self) -> LocationType:
        """Get the current location."""
        return self.location

    @property
    def players(self) -> PlayersType:
        """Get the number of players."""
        return self._players
    
    @players.setter
    def players(self, value: PlayersType):
        """Set the number of players."""
        self._players = value

    @property
    def input(self) -> InputType:
        """Get the input type."""
        return self._input
    
    @input.setter
    def input(self, value: InputType):
        """Set the input type."""
        self._input = value