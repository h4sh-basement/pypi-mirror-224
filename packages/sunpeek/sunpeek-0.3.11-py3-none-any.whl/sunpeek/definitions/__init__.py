"""
This package contains definitions for the pre-defined components such as fluids or collectors.
These are used to pre-populate the application database.
"""
import enum
from pathlib import Path

# from sunpeek.definitions import collector_types
# from sunpeek.definitions import fluid_definitions


class FluidProps(str, enum.Enum):
    density = 'density'
    heat_capacity = 'heat capacity'


fluid_data_dir = Path(__file__).with_name('fluid_data')
