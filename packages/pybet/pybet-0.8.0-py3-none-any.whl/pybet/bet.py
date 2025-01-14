from decimal import Decimal
from enum import Enum
from typing import Callable

from .odds import Odds


class Bet:
    """A class to represent a bet.

     Attributes:
        stake: The stake of the bet.
        odds: The odds of the bet.
        win_condition: The callback that will determine whether the bet is currently a winner or a loser.
        end_condition: The callback that will determine whether the bet can be settled.

    Example:
        >>> bradford_city = {'position': 1}
        >>> games_played = 45
        >>> bradford_win_league = lambda: bradford_city['position'] == 1
        >>> season_over = lambda: games_played == 46
        >>> bet = Bet(2.00, Odds(21), bradford_win_league, season_over)
    """

    class Status(Enum):
        """An enum to represent the status of a bet."""

        OPEN = 0
        WON = 1
        LOST = 2

        def __str__(self):
            return self.name

    def __init__(
        self,
        stake: Decimal,
        odds: Odds,
        win_condition: Callable[..., bool],
        end_condition: Callable[..., bool],
    ) -> None:
        """Initialises a bet with a win condition and an end condition.

        :param stake: The stake of the bet
        :type stake: Decimal
        :param odds: The odds of the bet
        :type odds: Odds
        :param win_condition: A callback that will determine whether the bet is currently a winner or a loser
        :type win_condition: Callable[..., bool]
        :param end_condition: A callback that will determine whether the bet can be settled
        :type end_condition: Callable[..., bool]
        :return: A bet
        :rtype: Bet

        :Example:
            >>> bet = Bet(2.00, Odds(21), bradford_win_league, season_over)
        """
        self.stake = stake
        self.odds = odds
        self.win_condition = win_condition
        self.end_condition = end_condition

    def settle(self) -> Decimal:
        """Returns the returns of the bet.

        :return: The returns of the bet to 2 decimal places
        :rtype: Decimal
        :raises ValueError: If the bet is still open

        :Example:
            >>> bet = Bet(2.00, Odds(21), bradford_win_league, season_over)
            >>> bet.settle()
            ValueError: Bet is still open
            >>> games_played = 46
            >>> bet.settle()
            42.00
            >>> bradford_city['position'] = 2
            >>> bet.settle()
            0
        """
        if not self.end_condition():
            raise ValueError("Bet is still open")

        return round(self.stake * self.odds, 2) if self.win_condition() else 0

    @property
    def status(self) -> Status:
        """Returns the status of the bet.

        :return: The status of the bet
        :rtype: Status

        :Example:
            >>> bet = Bet(2.00, Odds(21), bradford_win_league, season_over)
            >>> bet.status
            <Status.OPEN: 0>
            >>> games_played = 46
            <Status.WON: 1>
            >>> bradford_city['position'] = 2
            <Status.LOST: 2>
        """
        if self.end_condition():
            return Bet.Status.WON if self.win_condition() else Bet.Status.LOST

        return Bet.Status.OPEN
