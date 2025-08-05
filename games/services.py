import csv
import dataclasses
from collections import UserDict
from datetime import datetime, date
from typing import Iterable

from django.conf import settings
from django.template.defaultfilters import slugify

from games.models import Developer, Game, Genre, Platform, Rating

CSV_GAMES = settings.BASE_DIR / "metacritic_games.csv"


class GameImportError(Exception): ...


class GameCsvFileError(GameImportError): ...


@dataclasses.dataclass
class GameRow:
    title: str
    platform: str
    developer: str
    genre: str
    rating: int
    released_at: date
    meta_score: int
    user_score: int


class DictCache(UserDict):
    def __init__(self, model_cls) -> None:
        super().__init__()
        self.model_cls = model_cls
        self.data = dict(self.model_cls.objects.values_list("pk", "name"))

    def __getitem__(self, key: str) -> int:
        try:
            return super().__getitem__(key)
        except KeyError:
            item, _ = self.model_cls.objects.get_or_create(name=key)
            self.data[key] = item.pk
            return super().__getitem__(key)


def get_date_from_string(s: str) -> date:
    return datetime.strptime(s, "%b %d, %Y").date()


class GameSaver:
    developers: DictCache
    genres: Genre
    platforms: Platform
    ratings: Rating

    def __init__(self) -> None:
        self.developers = DictCache(Developer)
        self.genres = DictCache(Genre)
        self.platforms = DictCache(Platform)
        self.ratings = DictCache(Rating)

    def save(self, row: GameRow) -> Game:
        game, _ = Game.objects.get_or_create(
            title=row.title,
            slug=slugify(row.title),
            developer_id=self.developers[row.developer],
            genre_id=self.genres[row.genre],
            platform_id=self.platforms[row.platform],
            rating_id=self.ratings[row.rating],
            released_at=row.released_at,
            meta_score=row.meta_score,
            user_score=row.user_score,
        )
        return game


class GameImportService:
    saver: GameSaver

    def __init__(self) -> None:
        self.saver = GameSaver()

    def save(self, rows: list[GameRow]) -> Iterable[Game]:
        return (self.saver.save(row) for row in rows)

    def get_data_from_csv(self) -> list[GameRow]:
        if not CSV_GAMES.is_file():
            raise GameCsvFileError(f"File `{CSV_GAMES}` is missing. Please download it first!")

        with open(CSV_GAMES) as f:
            reader = csv.DictReader(f)
            return [
                GameRow(
                    title=row["game"],
                    platform=row["platform"],
                    developer=row["developer"],
                    genre=row["genre"],
                    rating=row["rating"],
                    released_at=get_date_from_string(row["release_date"]),
                    meta_score=int(row["metascore"]),
                    user_score=int(row["user_score"]),
                )
                for row in reader
            ]
