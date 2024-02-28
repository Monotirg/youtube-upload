import asyncio
import logging

from typing import Any

from ..loggers import logadapter
from ..pages._YTPage import YTPage 
from ..models.video import YTModel
from ..exceptions import YTStateGroupError, YTWarning


logger = logging.getLogger("yt_logger")


class YTModelField:
    def __init__(
        self, 
        value: Any = None, 
        always: bool = False, 
        repeat: int = 1,
        log_message: str = None
    ) -> None:
        self.value = value
        self.always = always
        self.repeat = repeat
        self.log_message = log_message


class YTPageStateGroup:
    def __new__(cls):
        instance = super().__new__(cls)

        if not hasattr(cls, "__yt_page__"):
            msg = f"'{cls.__name__}' has no attribute '__yt_page__'"
            raise YTStateGroupError(msg)
        
        if not hasattr(cls, "__yt_model__"):
            print(cls.__dict__)
            msg = f"'{cls.__name__}' has no attribute '__yt_model__'"
            raise YTStateGroupError(msg)

        yt_page = getattr(cls, "__yt_page__")
        yt_model = getattr(cls, "__yt_model__")

        if not issubclass(yt_page, YTPage):
            msg = f"'{yt_page.__name__}' is not a child class of 'YTPage'"
            raise YTStateGroupError(msg)
        
        if not issubclass(yt_model, YTModel):
            msg = f"'{yt_model.__name__}' is not a child class of 'YTModel'"
            raise YTStateGroupError(msg)

        setattr(instance, "__yt_page__", yt_page)
        setattr(instance, "__yt_model__", yt_model)

        yt_page_events = list(
            filter(
                lambda item: not item.startswith("_"), 
                yt_page.__dict__.keys()
            )
        )
        yt_model_fields = list(yt_model.model_fields.keys())
        
        for attr, model_field in cls.__dict__.items():
            if attr.startswith("__"):
                continue
            
            if attr not in yt_page_events:
                msg = f"'{yt_page.__name__}' has no attribute '{attr}'"
                raise YTStateGroupError(msg)
            
            if not isinstance(model_field,  YTModelField):
                msg = f"Attribute '{attr}' must be an instance of a class 'YTModelField'"
                raise YTStateGroupError(msg)

            if model_field.value not in yt_model_fields and model_field.value is not None:
                msg = f"{yt_model.__name__} has no attribute '{model_field.value}'"
                raise ValueError(msg)
            
            setattr(instance, attr, model_field)
        
        return instance
    
    @classmethod
    async def trigger(cls, state, yt_page, video_data, log_data):
        event = getattr(yt_page, state)
        field = getattr(cls, state)
        repeat = getattr(field, "repeat")
        params = getattr(video_data, str(field.value), None)
    
        if field.always:
            logger.info(field.log_message, extra=logadapter(
                log_data,
                params=params,
            ))

            for _ in range(repeat):
                await event()

            return None
    
        if params is not None:
            logger.info(field.log_message, extra=logadapter(
                log_data,
                params=params,
            ))
            
            for _ in range(repeat):
                await event(params)
        
        return None

    @classmethod
    async def start(cls, yt_page, video_data, log_data):
        states = [
            attr for attr in cls.__dict__
            if not attr.startswith("__")
        ]
        
        for state in states:
            try:
                await cls.trigger(state, yt_page, video_data, log_data)
            except YTWarning as warn:
                warn_type = warn.__class__.__name__
                warn_message = warn.args[0]
                logger.warning("%s %s" % (warn_type, warn_message), extra=logadapter(
                    log_data,
                    warn_type=warn_type,
                    warn_message=warn_message
                ))
                continue
            except:
                raise
