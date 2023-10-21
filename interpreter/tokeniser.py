import re


def tokenise(stream: str):
    stream = re.sub(r"[^<>+\-.,\[\]]", "", string=stream)
    stream = list(stream)
    return stream
