def truncate(text, limit, suffix='...'):
    if text is None:
        return None
    return (text[:limit] + suffix) if len(text) > limit else text
