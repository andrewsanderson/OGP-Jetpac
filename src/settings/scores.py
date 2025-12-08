import json
import os
from typing import Literal

PlayerTypes = Literal['p1', 'p2']

class Scores:
    """Manages player scores and high score persistence."""
    HIGH_SCORE_FILE = "high_score.json"
    
    def __init__(self):
        self.scores: dict[PlayerTypes, int] = {
            'p1': 0,
            'p2': 0
        }   
        self.high_score = self._load_high_score()
    
    def _load_high_score(self):
        """Load high score from file, or return 0 if file doesn't exist."""
        if os.path.exists(self.HIGH_SCORE_FILE):
            try:
                with open(self.HIGH_SCORE_FILE, 'r') as f:
                    data = json.load(f)
                    return data.get('high_score', 0)
            except (json.JSONDecodeError, IOError):
                return 0
        return 0
    
    def _save_high_score(self):
        """Save high score to file."""
        try:
            with open(self.HIGH_SCORE_FILE, 'w') as f:
                json.dump({'high_score': self.high_score}, f)
        except IOError:
            pass
    
    def update_score(self, player: PlayerTypes, score: int):
        """Update player 1 score and check for new high score."""
        self.scores[player] = score
        if score > self.high_score:
            self.high_score = score
            self._save_high_score()
