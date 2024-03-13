import re
import os
import json
import pprint
import logging
import datetime as dt

from ..utils import datetime_to_yt_date
from ..constants.categories import EDUCATION, GAMING


LOG_RECORD_BUILTIN_ATTR = {
    "video",
    "params",
    "playwright_settings",
    "youtube_video_settigns",
    "error_type",
    "error_message",
    "warn_type",
    "warn_message"
}


class LogFormatter:
    @staticmethod
    def playwright_settings(settings: dict):
        proxy = settings.get("proxy", None)

        if proxy is not None:
            settings.update(
                proxy={
                    "server": proxy['server']
                }
            )

        return LogFormatter._prepare_log(settings).replace(2*os.sep, os.sep)
    
    @staticmethod
    def video_settings(video: dict):
        category = video.get("category")
        education_problems = video.get("education_problems", None)

        if category != GAMING:
            video.pop("game_title")
        
        if category != EDUCATION:
            video.pop("education_type")
            video.pop("education_academic_system")
            video.pop("education_problems")
            video.pop("education_level")
            video.pop("education_exam")
            education_problems = None            
            
        if education_problems is not None:
            for i, item in enumerate(education_problems):
                time, text = item
                m, s = divmod(time.seconds, 60)
                education_problems[i] = [f"{m:02}:{s:02}", text]
            
            video.update(
                education_problems=education_problems
            )
        
        return LogFormatter._prepare_log(video)

            
    @staticmethod
    def _prepare_log(params, indent: bool =False):
        if isinstance(params, list | tuple):
            if indent:
                return "[" + ", ".join([LogFormatter._prepare_log(item, True)
                                        for item in params]) + "]"

            msg = "[ "
            msg += "".join(["%s," % LogFormatter._prepare_log(item, True)
                            for item in params])
            return msg[:-1] + "]"
        
        elif isinstance(params, dict):
            for key, value in params.items():
                if isinstance(params[key], dt.datetime | dt.date | dt.timedelta):
                    params[key] = LogFormatter._prepare_log(value)
            msg = pprint.pformat(params, indent=4, sort_dicts=False)
            msg = "{\n " + msg[1:-1] + "\n}"
            return msg.replace(2*os.sep, os.sep)
        elif isinstance(params, dt.datetime):
            return "%s %s" % datetime_to_yt_date(params)
        elif isinstance(params, dt.date):
            return "%s" % datetime_to_yt_date(params)
        elif isinstance(params, dt.timedelta):
            m, s = divmod(params.seconds, 60)
            return f"{m:02}:{s:02}"

        return pprint.pformat(params).replace(2*os.sep, os.sep)


class JSONFormatter(logging.Formatter):
    def __init__(
        self,
        *,
        fmt_keys: dict[str, str] | None = None,
    ):
        super().__init__()
        self.fmt_keys = fmt_keys if fmt_keys is not None else {}

    def format(self, record: logging.LogRecord) -> str:
        message = self._prepare_log_dict(record)
        return json.dumps(message, default=str, ensure_ascii=False)

    def _prepare_log_dict(self, record: logging.LogRecord):
        always_fields = {
             "timestamp": dt.datetime.fromtimestamp(
                record.created, tz=dt.timezone.utc
            ).isoformat(),
            "youtube_channel": getattr(record, "youtube_channel", None),
            "level": record.levelname,
        }

        video = getattr(record, "video", None)

        if video is not None:
            always_fields.update(
                video=video, 
            )
        
        always_fields.update(
            message=record.getMessage()
        )
        message = {
            field: value
            for field in LOG_RECORD_BUILTIN_ATTR
            if (value := getattr(record, field, None)) is not None
        }
        always_fields.update(message)
        
        return always_fields

class ConsoleFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord):
        date = dt.datetime.fromtimestamp(record.created)
        date = date.strftime("%Y-%m-%d %H:%M:%S")
        youtube_channel = getattr(record, "youtube_channel")
        level = record.levelname

        start_message = "%s [YouTube Channel: %s]" % (date, youtube_channel)
        
        if hasattr(record, "video"):
            video = getattr(record, "video")
            start_message += (
                " [Video: %s, Title: %s] %s" 
                % (video['path'], video['title'], level)
            )
        else:
            start_message += " %s" % level

        message = "%s %s" % (start_message, record.getMessage())

        if hasattr(record, "playwright_settings"):
            pw_settings = getattr(record, "playwright_settings")
            message += " %s" % LogFormatter.playwright_settings(pw_settings)
        elif hasattr(record, "youtube_video_settigns"):
            additional_message = pprint.pformat(getattr(record, "youtube_video_settigns"),
                                                sort_dicts=False, indent=4)
            additional_message = additional_message.replace(2*os.sep, os.sep)
            additional_message = "{\n" + additional_message[1:-1] + "\n}"
            message += " %s" % additional_message
        
        if hasattr(record, "params"):
            if getattr(record, "params") is not None:
                message += ": %s" % LogFormatter._prepare_log(getattr(record, "params"))
        
        return message
