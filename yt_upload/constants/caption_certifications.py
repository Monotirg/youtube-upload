from ..typing import YT_CAPTION_CERTIFICATION
from .indexes import YT_CAPTION_CERTIFICATION_TO_INDEX


CONTENT_HAS_NEVER_AIRED: YT_CAPTION_CERTIFICATION = \
    "This content has never aired on television in the U.S."
CONTENT_HAS_ONLY_AIRED: YT_CAPTION_CERTIFICATION = \
    "This content has only aired on television in the U.S. without captions"
CONTENT_HAS_NOT_AIRED: YT_CAPTION_CERTIFICATION = \
    "This content has not aired on U.S. television with captions since September 30, 2012."
CONTENT_DOES_NOT_FALL: YT_CAPTION_CERTIFICATION = \
    "This content does not fall within a category of online programming that requires captions under FCC regulations (47 C.F.R. § 79)."
CONGRESS_HAS_GRANTED: YT_CAPTION_CERTIFICATION =\
    "The FCC and/or U.S. Congress has granted an exemption from captioning requirements for this content."

YT_CAPTION_CERTIFICATIONS = list(YT_CAPTION_CERTIFICATION_TO_INDEX.keys())
