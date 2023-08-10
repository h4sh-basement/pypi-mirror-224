from dataclasses import dataclass

from rich.text import Text

from codelimit.common.Measurement import Measurement


@dataclass
class ReportUnit:
    file: str
    measurement: Measurement


def format_report_unit(unit: ReportUnit) -> Text:
    name = unit.measurement.unit_name
    length = unit.measurement.value
    if length > 60:
        style = "red"
    elif length > 30:
        style = "dark_orange"
    elif length > 15:
        style = "yellow"
    else:
        style = "green"
    length_text = f"{length:3}" if length < 61 else "60+"
    styled_text = Text(length_text, style=style)
    return Text.assemble("[", styled_text, "] ", name)
