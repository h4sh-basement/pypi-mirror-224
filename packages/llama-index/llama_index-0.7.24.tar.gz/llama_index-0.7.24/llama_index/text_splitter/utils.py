from typing import Callable, List

from llama_index.text_splitter.types import TextSplitter


def truncate_text(text: str, text_splitter: TextSplitter) -> str:
    """Truncate text to fit within the chunk size."""
    chunks = text_splitter.split_text(text)
    return chunks[0]


def split_text_keep_separator(text: str, separator: str) -> List[str]:
    """Split text with separator and keep the separator at the end of each split."""
    parts = text.split(separator)
    result = [separator + s if i > 0 else s for i, s in enumerate(parts)]
    result = [s for s in result if s]
    return result


def split_by_sep(sep: str, keep_sep: bool = True) -> Callable[[str], List[str]]:
    """Split text by separator."""
    if keep_sep:
        return lambda text: split_text_keep_separator(text, sep)
    else:
        return lambda text: text.split(sep)


def split_by_char() -> Callable[[str], List[str]]:
    """Split text by character."""
    return lambda text: list(text)


def split_by_sentence_tokenizer() -> Callable[[str], List[str]]:
    import nltk

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        import os

        nltk_data_dir = os.environ.get("NLTK_DATA", None)
        nltk.download("punkt", download_dir=nltk_data_dir)

    return nltk.sent_tokenize


def split_by_regex(regex: str) -> Callable[[str], List[str]]:
    """Split text by regex."""
    import re

    return lambda text: re.findall(regex, text)


def split_by_phrase_regex() -> Callable[[str], List[str]]:
    """Split text by phrase regex.

    This regular expression will split the sentences into phrases,
    where each phrase is a sequence of one or more non-comma,
    non-period, and non-semicolon characters, followed by an optional comma,
    period, or semicolon. The regular expression will also capture the
    delimiters themselves as separate items in the list of phrases.
    """
    regex = "[^,.;。]+[,.;。]?"
    return split_by_regex(regex)
