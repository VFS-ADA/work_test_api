from datetime import datetime


class DateTypes:
    GMT_DATE = "%a, %d %b %Y %H:%M:%S GMT"
    ISO_DATE = "%Y-%m-%d %H:%M:%S.%f"


class DateService:
    @staticmethod
    def global_init(app):
        pass

    @staticmethod
    def datetime_to_string(dt: datetime, date_type: DateTypes):
        return datetime.strftime(dt, date_type)

    @staticmethod
    def string_to_datetime(dt: str, date_type: DateTypes):
        return datetime.strptime(dt, date_type)

    @staticmethod
    def datetime_to_string_recursive(d: dict, date_type: DateTypes):
        for k, v in d.items():
            if isinstance(v, datetime):
                d[k] = DateService.datetime_to_string(v, date_type)
            elif isinstance(v, dict):
                DateService.datetime_to_string_recursive(v, date_type)
            elif isinstance(v, list):
                for i in v:
                    if isinstance(v, dict):
                        DateService.datetime_to_string_recursive(i, date_type)
