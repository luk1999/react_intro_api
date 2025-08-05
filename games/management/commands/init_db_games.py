from django.core.management.base import BaseCommand, CommandError
from tqdm import tqdm

from games.models import Game
from games.services import GameImportError, GameImportService


class Command(BaseCommand):
    help = "Initializes database with games-related data"

    def add_arguments(self, parser):
        parser.add_argument("--force", action="store_true", default=False)

    def handle(self, *_args, **options):
        if not options["force"] and Game.objects.exists():
            raise CommandError("Games list was already initialized. Use `--force` to initialize it again.")

        self.stdout.write("Running import process. Please wait...")

        try:
            service = GameImportService()
            rows = service.get_data_from_csv()
            generator = service.save(rows)
            for _game in tqdm(generator, total=len(rows)):
                ...
        except GameImportError as e:
            raise CommandError(e)

        self.stdout.write(self.style.SUCCESS("Import done."))
