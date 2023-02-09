from .services.sheet_service import SheetService


class GoogleSheet(SheetService):

    def __init__(self, *args, **kwargs, ) -> None:
        super().__init__(*args, **kwargs)