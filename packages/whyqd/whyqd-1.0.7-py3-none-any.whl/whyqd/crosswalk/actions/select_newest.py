from __future__ import annotations
import modin.pandas as pd
import numpy as np

from whyqd.crosswalk.base import BaseSchemaAction
from whyqd.models import ModifierModel, FieldModel


class Action(BaseSchemaAction):
    """
    Create a new field by iterating over a list of fields and selecting the newest value in the list.

    !!! tip "Script template"
        ```python
        "SELECT_NEWEST > 'destination_field' < ['source_field' + 'source_field_date', 'source_field' + 'source_field_date', etc.]"
        ```

        Where `+` links two columns together, explicitly declaring that the date in `source_field_date` is used to
        assign the order to the values in `source_field`. Unlike the `SELECT` action, `SELECT_NEWEST` takes its ordering from
        this date assignment.

    !!! example
        ```python
        "SELECT_NEWEST > 'occupation_state_date' < ['Current Relief Award Start Date' + 'Current Relief Award Start Date', 'Account Start date' + 'Account Start date']"
        ```
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = "SELECT_NEWEST"
        self.title = "select by newest"
        self.description = "Use sparse data from a list of fields to populate a new field selecting by most recent value. Field-pairs required, with the first containing the values, and the second the dates for comparison, linked by a '+' modifier (e.g. A+dA, B+dB, C+dC, values with the most recent associated date will have precedence over other values)."
        self.structure = [FieldModel, ModifierModel, FieldModel]

    @property
    def modifiers(self) -> list[ModifierModel]:
        return [ModifierModel(**{"name": "+", "title": "Links"})]

    def transform(
        self,
        *,
        df: pd.DataFrame,
        destination: FieldModel,
        source: list[FieldModel | ModifierModel],
    ) -> pd.DataFrame:
        base_date = None
        # Requires sets of 3 terms: field, +, date_field
        term_set = len(self.structure)
        for data, modifier, date in self.core.chunks(lst=source, n=term_set):
            if modifier.name != "+":
                raise ValueError(f"Field `{source}` has invalid SELECT_BY_NEW script. Please review.")
            if not base_date:
                # Start the comparison on the next round
                df.rename(index=str, columns={data.name: destination.name}, inplace=True)
                base_date = date.name
                if data.name == date.name:
                    # Just comparing date columns
                    base_date = destination.name
                df[base_date] = df[base_date].apply(self.reader.parse_dates_coerced)
                continue
            # np.where date is <> base_date and don't replace value with null
            # logic: if test_date not null & base_date <> test_date
            # False if (test_date == nan) | (base_date == nan) | base_date >< test_date
            # Therefore we need to test again for the alternatives
            df[date.name] = df[date.name].apply(self.reader.parse_dates_coerced)
            df[destination.name] = np.where(
                df[date.name].isnull() | (df[base_date] > df[date.name]),
                np.where(df[destination.name].notnull(), df[destination.name], df[data.name]),
                np.where(df[data.name].notnull(), df[data.name], df[destination.name]),
            )
            if base_date != destination.name:
                df[base_date] = np.where(
                    df[date.name].isnull() | (df[base_date] > df[date.name]),
                    np.where(df[base_date].notnull(), df[base_date], df[date.name]),
                    np.where(df[date.name].notnull(), df[date.name], df[base_date]),
                )
        return df
