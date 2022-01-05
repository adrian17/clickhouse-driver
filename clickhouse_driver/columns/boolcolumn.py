from .base import FormatColumn

class BoolColumn(FormatColumn):
    ch_type = 'Bool'
    py_types = (bool, )
    format = 'B'

    def before_write_items(self, items, nulls_map=None):
        null_value = self.null_value

        for i, item in enumerate(items):
            if nulls_map and nulls_map[i]:
                items[i] = null_value
                continue

            items[i] = bool(item)

    def after_read_items(self, items, nulls_map=None):
        if nulls_map is None:
            return tuple(bool(item) for item in items)
        else:
            return tuple(
                (None if is_null else bool(items[i]))
                for i, is_null in enumerate(nulls_map)
            )
