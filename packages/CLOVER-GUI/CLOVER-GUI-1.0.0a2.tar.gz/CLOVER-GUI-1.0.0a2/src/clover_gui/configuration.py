#!/usr/bin/python3.10
########################################################################################
# configuration.py - The configuration module for CLOVER-GUI application.              #
#                                                                                      #
# Author: Ben Winchester, Hamish Beath                                                 #
# Copyright: Ben Winchester, 2022                                                      #
# Date created: 23/06/2023                                                             #
# License: MIT, Open-source                                                            #
# For more information, contact: benedict.winchester@gmail.com                         #
########################################################################################

import datetime
import tkinter as tk

import ttkbootstrap as ttk

from typing import Callable

from clover import OperatingMode, Simulation
from clover.__utils__ import ITERATION_LENGTH, MAX, MIN, NUMBER_OF_ITERATIONS, STEP
from clover.fileparser import OPTIMISATIONS
from clover.optimisation import Optimisation, OptimisationParameters, ThresholdMode
from clover.optimisation.__utils__ import (
    Criterion,
    OPTIMISATION_CRITERIA,
    OptimisationComponent,
    THRESHOLD_CRITERIA,
    THRESHOLD_CRITERION_TO_MODE,
)
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import *

from .__utils__ import BaseScreen, clover_thread
from .scenario import ConfigurationFrame


__all__ = ("ConfigurationScreen",)


class SimulationFrame(BaseScreen, show_navigation=False):

    """
    Represents the simulation frame.

    The simulation frame contains the necessary parameters needed to launch a simulation
    in CLOVER as well as a launch button for initiating the run.

    TODO: Update attributes.

    """

    def __init__(
        self,
        parent,
        launch_clover_run: Callable,
    ) -> None:
        super().__init__(parent)

        """
        Instantiate a :class:`ConfigureFrame` instance.

        :param: launch_clover_run
            A callable function to launch a simulation.

        """

        self.pack(fill="both", expand=True)

        # Set the physical distance weights of the rows and columns
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.start_year = ttk.DoubleVar()
        self.end_year = ttk.DoubleVar()

        # self.end_year_slider = ttk.Scale(self, bootstyle="danger")
        # self.end_year_slider.grid(row=3, column=1, padx=20)
        self.generate_plots = ttk.BooleanVar()

        # PV size
        self.pv_size_label = ttk.Label(self, text="PV System Size")
        self.pv_size_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.pv_size: ttk.DoubleVar = ttk.DoubleVar(self, value=0)
        self.pv_size_entry = ttk.Entry(self, bootstyle=INFO, textvariable=self.pv_size)
        self.pv_size_entry.grid(
            row=0, column=1, columnspan=2, padx=10, pady=5, sticky="ew", ipadx=80
        )

        self.pv_size_info = ttk.Label(self, text="kWp")
        self.pv_size_info.grid(row=0, column=3, sticky="w")

        # Storage size
        self.storage_size_label = ttk.Label(self, text="Storage Size")
        self.storage_size_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.storage_size: ttk.DoubleVar = ttk.DoubleVar(self, value=0)
        self.storage_size_entry = ttk.Entry(
            self, bootstyle=INFO, textvariable=self.storage_size
        )
        self.storage_size_entry.grid(
            row=1, column=1, columnspan=2, padx=10, pady=5, sticky="ew", ipadx=80
        )
        self.storage_size_info = ttk.Label(self, text="kWh")
        self.storage_size_info.grid(row=1, column=3, sticky="w")

        # Simulation period
        self.simulation_period_label = ttk.Label(self, text="Simulation period")
        self.simulation_period_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.simulation_period = ttk.IntVar(self, 20, "simulation_period")

        # self.simulation_period_info = ttk.Label(self, text="Years")
        # self.simulation_period_info.grid(row=3, column=3)

        self.scalerber = ttk.Label(
            self, text=f"{int(self.simulation_period.get())} years"
        )
        self.scalerber.grid(row=2, column=3, sticky="w")

        def scaler(e):
            self.scalerber.config(
                text=f"{' ' * (int(self.years_slider.get()) < 10)}{int(self.years_slider.get())} years"
            )

        self.years_slider = ttk.Scale(
            self,
            from_=1,
            to=30,
            orient=tk.HORIZONTAL,
            length=320,
            command=scaler,
            bootstyle=INFO,
            variable=self.simulation_period,
        )
        self.years_slider.grid(
            row=2, column=1, columnspan=2, padx=10, pady=5, sticky="ew"
        )

        # Generate plots
        self.generate_plots_label = ttk.Label(self, text="Generate plots")
        self.generate_plots_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.generate_plots: ttk.BooleanVar = ttk.BooleanVar(
            self, True, "generate_plots"
        )
        self.not_generate_plots: ttk.BooleanVar = ttk.BooleanVar(
            self, not self.generate_plots.get(), "not_generate_plots"
        )

        self.generate_plots_true_button = ttk.Checkbutton(
            self,
            variable=self.generate_plots,
            command=self._generate_plots_callback,
            bootstyle=TOOLBUTTON,
            text="ON",
        )
        self.generate_plots_true_button.grid(
            row=3, column=1, padx=10, pady=5, sticky="ew"
        )

        self.generate_plots_false_button = ttk.Checkbutton(
            self,
            variable=self.not_generate_plots,
            command=self._not_generate_plots_callback,
            bootstyle=TOOLBUTTON,
            text="OFF",
        )
        self.generate_plots_false_button.grid(
            row=3, column=2, padx=10, pady=5, sticky="ew"
        )

        # Output name
        self.output_name_label = ttk.Label(self, text="Output name")
        self.output_name_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.output_name: ttk.StringVar = ttk.StringVar(self, "results")
        self.output_name_entry = ttk.Entry(
            self, bootstyle=INFO, textvariable=self.output_name
        )
        self.output_name_entry.grid(
            row=4, column=1, columnspan=2, padx=10, pady=5, sticky="ew", ipadx=80
        )

        # Combines the functions to open the run screen and launch the simulation.
        self.run_simulation_frame = ttk.Frame(self)
        self.run_simulation_frame.grid(row=5, column=0, columnspan=4)

        self.run_simulation_frame.columnconfigure(0, weight=4, minsize=800)
        self.run_simulation_frame.columnconfigure(1, weight=1)
        self.run_simulation_frame.rowconfigure(0, weight=1)

        self.run_simulation_button = ttk.Button(
            self.run_simulation_frame,
            text="Run Simulation",
            bootstyle=f"{INFO}-outline",
            command=lambda operating_mode=OperatingMode.SIMULATION: launch_clover_run(
                operating_mode
            ),
        )
        self.run_simulation_button.grid(
            row=0,
            column=1,
            columnspan=2,
            padx=5,
            pady=5,
            ipadx=80,
            ipady=20,
            sticky="es",
        )

        # TODO: Add configuration frame widgets and layout

    def _generate_plots_callback(self) -> None:
        """Called when the not-generate-plots button is pressed."""

        self.generate_plots.set(True)
        self.not_generate_plots.set(False)

    def _not_generate_plots_callback(self) -> None:
        """Called when the not-generate-plots button is pressed."""

        self.generate_plots.set(False)
        self.not_generate_plots.set(True)

    def set_simulation(self, simulation: Simulation) -> None:
        """
        Set the information from the simulation loaded.

        :param: simulation
            The simulation to set.

        """

        # Update the simulation period from the simulations file.
        self.start_year.set(simulation.start_year)
        self.end_year.set(simulation.end_year)
        self.simulation_period.set(self.end_year.get() - self.start_year.get())

        self.years_slider.set(self.simulation_period.get())


class ThresholdCriterion:
    """
    Represents a threshold criterion.

    .. attribute:: criterion_name
        The name of the criterion.

    .. attribute:: less_than
        Whether to use a less-than (True) or greater-than (False) condition for the
        criterion.

    .. attribute:: value
        The threshold value for the criterion.

    .. attribute:: index
        The index of the criteria as being created.

    """

    # Private attributes:
    #
    # .. attribute:: _criterion_to_name_map
    #   Map between the name of the criteria and the nice names.
    #
    # .. attribute:: _permissable_chevrons
    #   The `list` of permissable chevrons.
    #
    # .. attribute:: _permissable_threshold_criteria
    #   The `list` of permissable threshold criteria.

    criterion_to_name_map: dict[Criterion, str] = {
        Criterion.BLACKOUTS: "Blackouts fraction",
        Criterion.CLEAN_WATER_BLACKOUTS: "Clean water blackouts fraction",
        Criterion.CUMULATIVE_COST: "Cumulative cost / $",
        Criterion.CUMULATIVE_GHGS: "Cumulative ghgs / kgCO2eq",
        Criterion.CUMULATIVE_SYSTEM_COST: "Cumulative system cost / $",
        Criterion.CUMULATIVE_SYSTEM_GHGS: "Cumulative system ghgs / kgCO2eq",
        Criterion.EMISSIONS_INTENSITY: "Emissions intensity / gCO2/kWh",
        Criterion.KEROSENE_COST_MITIGATED: "Kerosene cost mitigated / $",
        Criterion.KEROSENE_GHGS_MITIGATED: "Kerosene ghgs mitigated / kgCO2eq",
        Criterion.LCUE: "LCUE / $/kWh",
        Criterion.RENEWABLES_FRACTION: "Renewables fraction",
        Criterion.TOTAL_GHGS: "Total ghgs / kgCO2eq",
        Criterion.TOTAL_SYSTEM_COST: "Total system cost / $",
        Criterion.TOTAL_SYSTEM_GHGS: "Total system ghgs / kgCO2eq",
        Criterion.TOTAL_COST: "Total_cost / $",
        Criterion.UNMET_ENERGY_FRACTION: "Unmet energy fraction",
    }

    _name_to_criterion_map: dict[str, Criterion] | None = None

    _permissable_chevrons: list[str] = sorted(["<", ">"])

    _permissable_threshold_criteria: list[str] = sorted(criterion_to_name_map.values())

    def __init__(
        self,
        parent,
        criterion_name: ttk.StringVar,
        less_than: ttk.BooleanVar,
        value: ttk.DoubleVar,
        delete_criterion: Callable,
        index: int = 0,
    ) -> None:
        """
        Instnatiate a :class:`ThresholdCriterion` instance.

        :param: parent
            The parent :class:`ttk.Frame` in which the class is being created.

        :param: criterion_name
            The name of the criterion.

        :param: less_than
            Whether to use a less-than (True) or greater-than (False) condition for the
            criterion.

        :param: value
            The threshold value for the criterion.

        :param: delete_criterion
            `Callable` to delete the criterion.

        :param: index
            The index of the criteria as being created.

        """

        # Criterion name and entry
        self.criterion_name: ttk.StringVar = criterion_name
        self.criterion_name_combobox = ttk.Combobox(
            parent, bootstyle=INFO, textvariable=self.criterion_name
        )
        self.criterion_name_combobox["values"] = self._permissable_threshold_criteria

        self.less_than: ttk.BooleanVar = less_than
        self.less_than_string: ttk.StringVar = ttk.StringVar(
            parent, "<" if self.less_than else ">"
        )
        self.less_than_combobox = ttk.Combobox(
            parent, bootstyle=INFO, textvariable=self.less_than_string
        )
        self.less_than_combobox["values"] = self._permissable_chevrons

        self.value: ttk.DoubleVar = value
        self.value_entry = ttk.Entry(parent, bootstyle=INFO, textvariable=self.value)

        self.delete_criterion_button: ttk.Button = ttk.Button(
            parent,
            bootstyle=f"{DANGER}-{OUTLINE}",
            text="Delete",
            command=lambda criterion=self: delete_criterion(criterion),
        )

        self.index: int = index

    def __hash__(self) -> int:
        """Return a `str` based on the information in the threshold criteria."""

        return self.index

    def __str__(self) -> str:
        """Return a nice-looking string."""

        return (
            f"ThresholdCriterion('{self.criterion_name.get()}' "
            + ("less than" if self.less_than.get() else "greater than")
            + f" {self.value.get()}"
        )

    def __repr__(self) -> str:
        """Return the default representation of the class."""

        return self.__str__()

    @classmethod
    def default_threshold_criterion(cls) -> str:
        """Return the default threshold criterion."""

        return cls._permissable_threshold_criteria[0]

    def display(self) -> None:
        """Display the criterion on the screen."""

        self.criterion_name_combobox.grid(
            row=(25 + self.index), column=0, padx=10, pady=5, sticky="ew"
        )
        self.less_than_combobox.grid(
            row=(25 + self.index), column=1, padx=10, pady=5, sticky="ew"
        )
        self.value_entry.grid(
            row=(25 + self.index), column=2, padx=10, pady=5, sticky="ew"
        )
        self.delete_criterion_button.grid(
            row=(25 + self.index), column=3, padx=10, pady=5, sticky="w", ipadx=20
        )

    def grid_forget(self) -> None:
        """Remove the varoius items from the screen."""

        self.criterion_name_combobox.grid_forget()
        self.less_than_combobox.grid_forget()
        self.value_entry.grid_forget()
        self.delete_criterion_button.grid_forget()

    @classmethod
    @property
    def name_to_criterion_map(self) -> dict[str, Criterion]:
        """
        Return a mapping bewteen criteria and names to be stored.

        :return:
            A mapping between criteria and names to store them in-file.

        """

        if self._name_to_criterion_map is None:
            self._name_to_criterion_map: dict[str, Criterion] = {
                value: key for key, value in self.criterion_to_name_map.items()
            }
        return self._name_to_criterion_map

    def set_index(self, index: int) -> None:
        """
        Sets the index attribute.

        :param: index
            The index to set.

        """

        self.index = index


class OptimisationFrame(ttk.Frame):
    """
    Represents the optimisation frame.

    The optimisation frame contains the launch parameters needed for launching an
    optimisation in CLOVER as well as a launch button for initiating the run.

    TODO: Update attributes.

    """

    def __init__(
        self, parent, launch_clover_run: Callable, system_lifetime: ttk.IntVar
    ):
        super().__init__(parent)

        self.system_lifetime = system_lifetime

        # TODO: Add configuration frame widgets and layout
        self.pack(fill="both", expand=True)

        self.rowconfigure(0, weight=20)  # scrolled frame
        self.rowconfigure(1, weight=1)  # run optimisation button

        self.columnconfigure(0, weight=1)

        # Create the scrollable frame and rows
        self.scrollable_optimisation_frame = ScrolledFrame(
            self,
        )
        self.scrollable_optimisation_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
            ipady=0,
            ipadx=0,
            sticky="news",
        )

        # rows
        self.scrollable_optimisation_frame.rowconfigure(0, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(1, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(2, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(3, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(4, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(5, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(6, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(7, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(8, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(9, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(10, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(11, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(12, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(13, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(14, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(15, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(16, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(17, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(18, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(19, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(20, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(21, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(22, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(23, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(24, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(25, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(26, weight=1)
        self.scrollable_optimisation_frame.rowconfigure(27, weight=1)

        # columns
        self.scrollable_optimisation_frame.columnconfigure(0, weight=1)
        self.scrollable_optimisation_frame.columnconfigure(1, weight=1)
        self.scrollable_optimisation_frame.columnconfigure(2, weight=1)
        self.scrollable_optimisation_frame.columnconfigure(3, weight=1)
        self.scrollable_optimisation_frame.columnconfigure(4, weight=1)
        # self.scrollable_optimisation_frame.columnconfigure(5, weight=1)
        # self.scrollable_optimisation_frame.columnconfigure(6, weight=1)

        # Iterations frame
        # self.iterations_frame = ttk.Labelframe(
        #     self, style="info.TLabelframe", text="Iterations"
        # )
        # self.iterations_frame.grid(
        #     row=0,
        #     column=0,
        #     columnspan=2,
        #     padx=5,
        #     pady=10,
        #     ipady=80,
        #     ipadx=40,
        #     sticky="news",
        # )

        # self.iterations_frame.rowconfigure(0, weight=4)
        # self.iterations_frame.rowconfigure(1, weight=4)
        # self.iterations_frame.rowconfigure(2, weight=1)

        # self.iterations_frame.columnconfigure(0, weight=10)  # First row has the header
        # self.iterations_frame.columnconfigure(1, weight=10)  # These rows have entries
        # self.iterations_frame.columnconfigure(2, weight=1)  # These rows have entries
        # self.iterations_frame.columnconfigure(3, weight=1)  # These rows have entries

        # Warning about number of iterations
        self.iteration_length = ttk.IntVar(self, "5")
        self.number_of_iterations = ttk.IntVar(self, "2")

        self.warning_text = ttk.Label(
            self.scrollable_optimisation_frame, text="", bootstyle=SECONDARY
        )
        self.warning_text_displayed = ttk.BooleanVar(
            self, False, "warning_text_displayed"
        )
        self.warning_text.grid(
            row=3, column=0, columnspan=3, padx=10, pady=5, sticky="ew"
        )

        def update_optimisation_time_warning() -> None:
            """
            If the simulation time is longer than the system lifetime, warn the user.

            The simulation time, i.e., the total length of time for which optimisations
            will be run, can either equal zero, or can exceed the lifetime of the
            system. In either case, the user needs to be warned.

            """

            # Period exceeds system lifetime
            if (
                optimisation_length := self.iteration_length.get()
                * self.number_of_iterations.get()
            ) > self.system_lifetime.get():
                self.warning_text.configure(
                    text="The length and number of iterations specified amounts to "
                    f"{optimisation_length} years which is greater than the system "
                    f"lifetime of {self.system_lifetime.get()} years.",
                )
                self.warning_text.configure(
                    bootstyle=DANGER,
                )
                self.warning_text_displayed.set(True)
                return

            # Optimisation length is zero years.
            if optimisation_length == 0:
                self.warning_text.configure(
                    text="The length and number of iterations specified amounts to "
                    f"{optimisation_length} years and, hence, no optimisations will be "
                    "carried out.",
                )
                self.warning_text.configure(
                    bootstyle=DANGER,
                )
                self.warning_text_displayed.set(True)
                return

            # Text should be disabled.
            if self.warning_text_displayed.get():
                self.warning_text.configure(
                    text="The length and number of iterations specified amounts to "
                    f"{optimisation_length} years which is "
                    + (
                        "less than "
                        if optimisation_length < self.system_lifetime.get()
                        else "equal to "
                    )
                    + f"the system lifetime of {self.system_lifetime.get()} years.",
                    bootstyle=SECONDARY,
                )

        # Iteration header
        bold_head = ttk.Style()
        bold_head.configure("Bold.TLabel", font=("TkDefaultFont", 13, "bold"))

        self.iteration_header = ttk.Label(
            self.scrollable_optimisation_frame, text="Iterations", style="Bold.TLabel"
        )
        self.iteration_header.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Iteration length
        self.iteration_length_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Iteration Length"
        )
        self.iteration_length_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        def scalar_iteration_length(_):
            self.iteration_length.set(self.iteration_length.get())
            self.iteration_length_entry.update()
            update_optimisation_time_warning()

        self.iteration_length_slider = ttk.Scale(
            self.scrollable_optimisation_frame,
            from_=1,
            to=30,
            orient=tk.HORIZONTAL,
            # length=320,
            command=scalar_iteration_length,
            bootstyle=INFO,
            variable=self.iteration_length,
            # state=DISABLED
        )
        self.iteration_length_slider.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        def enter_iteration_length(_):
            self.iteration_length.set(self.iteration_length_entry.get())
            self.iteration_length_slider.set(int(self.iteration_length.get()))
            update_optimisation_time_warning()

        self.iteration_length_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=INFO,
            textvariable=self.iteration_length,
        )
        self.iteration_length_entry.grid(row=1, column=2, padx=10, pady=5, sticky="ew")
        self.iteration_length_entry.bind("<Return>", enter_iteration_length)

        self.iteration_length_unit = ttk.Label(
            self.scrollable_optimisation_frame, text=f"years"
        )
        self.iteration_length_unit.grid(row=1, column=3, padx=10, pady=5, sticky="ew")

        # Number of iterations
        self.number_of_iterations_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Number of iterations"
        )
        self.number_of_iterations_label.grid(
            row=2, column=0, padx=10, pady=5, sticky="w"
        )

        def scalarber_of_iterations(_):
            self.number_of_iterations.set(self.number_of_iterations.get())
            self.number_of_iterations_entry.update()
            update_optimisation_time_warning()

        self.number_of_iterations_slider = ttk.Scale(
            self.scrollable_optimisation_frame,
            from_=1,
            to=self.system_lifetime.get(),
            orient=tk.HORIZONTAL,
            # length=320,
            command=scalarber_of_iterations,
            bootstyle=INFO,
            variable=self.number_of_iterations,
            # state=DISABLED
        )
        self.number_of_iterations_slider.grid(
            row=2, column=1, padx=10, pady=5, sticky="ew"
        )

        def enterber_of_iterations(_):
            self.number_of_iterations.set(self.number_of_iterations_entry.get())
            self.number_of_iterations_slider.set(int(self.number_of_iterations.get()))
            update_optimisation_time_warning()

        self.number_of_iterations_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=INFO,
            textvariable=self.number_of_iterations,
        )
        self.number_of_iterations_entry.grid(
            row=2, column=2, padx=10, pady=5, sticky="ew"
        )
        self.number_of_iterations_entry.bind("<Return>", enterber_of_iterations)

        self.number_of_iterations_unit = ttk.Label(
            self.scrollable_optimisation_frame, text=f"iterations"
        )
        self.number_of_iterations_unit.grid(
            row=2, column=3, padx=10, pady=5, sticky="ew"
        )

        # Horizontal divider
        self.horizontal_divider = ttk.Separator(
            self.scrollable_optimisation_frame, orient=tk.HORIZONTAL
        )
        self.horizontal_divider.grid(
            row=4, column=0, columnspan=7, padx=10, pady=5, sticky="ew"
        )

        # Steps frame
        # self.steps_frame = ttk.Labelframe(
        #     self, style="info.TLabelframe", text="Optimisation configuration parameters"
        # )
        # self.steps_frame.grid(
        #     row=1,
        #     column=0,
        #     columnspan=2,
        #     padx=5,
        #     pady=10,
        #     ipady=0,
        #     ipadx=0,
        #     sticky="news",
        # )

        # self.steps_frame.rowconfigure(0, weight=1)

        # self.steps_frame.columnconfigure(0, weight=1)

        # self.scrollable_steps_frame = ScrolledFrame(self.steps_frame)
        # self.scrollable_steps_frame.grid(
        #     row=0,
        #     column=0,
        #     padx=10,
        #     pady=5,
        #     ipady=0,
        #     ipadx=0,
        #     sticky="news",
        # )

        # self.scrollable_steps_frame.rowconfigure(0, weight=1)
        # self.scrollable_steps_frame.rowconfigure(1, weight=1)
        # self.scrollable_steps_frame.rowconfigure(2, weight=1)
        # self.scrollable_steps_frame.rowconfigure(3, weight=1)
        # self.scrollable_steps_frame.rowconfigure(4, weight=1)

        # self.scrollable_steps_frame.columnconfigure(
        #     0, weight=2
        # )  # First row has the header
        # self.scrollable_steps_frame.columnconfigure(
        #     1, weight=1
        # )  # These rows have entries
        # self.scrollable_steps_frame.columnconfigure(
        #     2, weight=2
        # )  # These rows have entries
        # self.scrollable_steps_frame.columnconfigure(
        #     3, weight=1
        # )  # These rows have entries
        # self.scrollable_steps_frame.columnconfigure(
        #     4, weight=2
        # )  # First row has the header
        # self.scrollable_steps_frame.columnconfigure(
        #     5, weight=1
        # )  # These rows have entries
        # self.scrollable_steps_frame.columnconfigure(
        #     6, weight=1
        # )  # These rows have entries

        # Optimisation parameters header
        self.optimisation_parameters_header = ttk.Label(
            self.scrollable_optimisation_frame,
            text="Optimisation parameters",
            style="Bold.TLabel",
        )
        self.optimisation_parameters_header.grid(
            row=5, column=0, padx=10, pady=5, sticky="w"
        )

        # PV step size
        self.pv_label = ttk.Label(self.scrollable_optimisation_frame, text="PV min")
        self.pv_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        self.pv_min = ttk.IntVar(self, 5)
        self.pv_min_entry = ttk.Entry(
            self.scrollable_optimisation_frame, bootstyle=INFO, textvariable=self.pv_min
        )
        self.pv_min_entry.grid(row=6, column=1, padx=10, pady=5, sticky="ew")

        self.pv_min_unit = ttk.Label(self.scrollable_optimisation_frame, text="panels")
        self.pv_min_unit.grid(row=6, column=2, padx=10, pady=5, sticky="w")

        self.pv_max_label = ttk.Label(self.scrollable_optimisation_frame, text="PV max")
        self.pv_max_label.grid(row=6, column=2, padx=10, pady=5, sticky="e")

        self.pv_max = ttk.IntVar(self, 20)
        self.pv_max_entry = ttk.Entry(
            self.scrollable_optimisation_frame, bootstyle=INFO, textvariable=self.pv_max
        )
        self.pv_max_entry.grid(row=6, column=3, padx=10, pady=5, sticky="ew")

        self.pv_max_unit = ttk.Label(self.scrollable_optimisation_frame, text="panels")
        self.pv_max_unit.grid(row=6, column=4, padx=10, pady=5, sticky="w")

        self.pv_step_label = ttk.Label(
            self.scrollable_optimisation_frame, text="PV step size"
        )
        self.pv_step_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.pv_step = ttk.IntVar(self, 5)

        self.pv_step_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=INFO,
            textvariable=self.pv_step,
        )
        self.pv_step_entry.grid(row=7, column=1, padx=10, pady=5, sticky="ew")

        self.pv_step_unit = ttk.Label(self.scrollable_optimisation_frame, text="panels")
        self.pv_step_unit.grid(row=7, column=2, padx=10, pady=5, sticky="w")

        # Storage step size
        self.storage_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Storage min"
        )
        self.storage_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        # self.storage_min_label = ttk.Label(self.scrollable_optimisation_frame, text="min")
        # self.storage_min_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")

        self.storage_min = ttk.IntVar(self, 5)
        self.storage_min_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=INFO,
            textvariable=self.storage_min,
        )
        self.storage_min_entry.grid(row=8, column=1, padx=10, pady=5, sticky="ew")

        self.storage_min_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="batteries"
        )
        self.storage_min_unit.grid(row=8, column=2, padx=10, pady=5, sticky="w")

        self.storage_max_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Storage max"
        )
        self.storage_max_label.grid(row=8, column=2, padx=10, pady=5, sticky="e")

        self.storage_max = ttk.IntVar(self, 30)
        self.storage_max_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=INFO,
            textvariable=self.storage_max,
        )
        self.storage_max_entry.grid(row=8, column=3, padx=10, pady=5, sticky="ew")

        self.storage_max_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="batteries"
        )
        self.storage_max_unit.grid(row=8, column=4, padx=10, pady=5, sticky="w")

        self.storage_step_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Storage step size"
        )
        self.storage_step_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.storage_step = ttk.IntVar(self, 5)

        self.storage_step_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=INFO,
            textvariable=self.storage_step,
        )
        self.storage_step_entry.grid(row=9, column=1, padx=10, pady=5, sticky="ew")

        self.storage_step_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="batteries"
        )
        self.storage_step_unit.grid(row=9, column=2, padx=10, pady=5, sticky="w")

        # Hot-water PV-T step size
        self.hw_pv_t_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Hot-water PV-T min"
        )
        # self.hw_pv_t_label.grid(row=10, column=0, padx=10, pady=5, sticky="w")

        self.hw_pv_t_min_label = ttk.Label(
            self.scrollable_optimisation_frame, text="min"
        )
        # self.hw_pv_t_min_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.hw_pv_t_min = ttk.IntVar(self, 0)
        self.hw_pv_t_min_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.hw_pv_t_min,
            state=DISABLED,
        )
        # self.hw_pv_t_min_entry.grid(row=10, column=1, padx=10, pady=5, sticky="ew")

        self.hw_pv_t_min_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="panels"
        )
        # self.hw_pv_t_min_unit.grid(row=10, column=2, padx=10, pady=5, sticky="w")

        self.hw_pv_t_max_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Hot-water PV-T max"
        )
        # self.hw_pv_t_max_label.grid(row=10, column=2, padx=10, pady=5, sticky="e")

        self.hw_pv_t_max = ttk.IntVar(self, 0)
        self.hw_pv_t_max_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.hw_pv_t_max,
            state=DISABLED,
        )
        # self.hw_pv_t_max_entry.grid(row=10, column=3, padx=10, pady=5, sticky="ew")

        self.hw_pv_t_max_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="panels"
        )
        # self.hw_pv_t_max_unit.grid(row=10, column=4, padx=10, pady=5, sticky="w")

        self.hw_pv_t_step_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Hot-water PV-T step size"
        )
        # self.hw_pv_t_step_label.grid(row=11, column=0, padx=10, pady=5, sticky="w")
        self.hw_pv_t_step = ttk.IntVar(self, 0)

        self.hw_pv_t_step_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.hw_pv_t_step,
            state=DISABLED,
        )
        # self.hw_pv_t_step_entry.grid(row=11, column=1, padx=10, pady=5, sticky="ew")

        self.hw_pv_t_step_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="panels"
        )
        # self.hw_pv_t_step_unit.grid(row=11, column=2, padx=10, pady=5, sticky="w")

        # Clean-water PV-T step size
        self.cw_pv_t_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Clean-water PV-T min"
        )
        # self.cw_pv_t_label.grid(row=12, column=0, padx=10, pady=5, sticky="w")

        self.cw_pv_t_min = ttk.IntVar(self, 0)
        self.cw_pv_t_min_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.cw_pv_t_min,
            state=DISABLED,
        )
        # self.cw_pv_t_min_entry.grid(row=12, column=1, padx=10, pady=5, sticky="ew")

        self.cw_pv_t_min_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="panels"
        )
        # self.cw_pv_t_min_unit.grid(row=12, column=2, padx=10, pady=5, sticky="w")

        self.cw_pv_t_max_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Clean-water PV-T max"
        )
        # self.cw_pv_t_max_label.grid(row=12, column=2, padx=10, pady=5, sticky="e")

        self.cw_pv_t_max = ttk.IntVar(self, 0)
        self.cw_pv_t_max_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.cw_pv_t_max,
            state=DISABLED,
        )
        # self.cw_pv_t_max_entry.grid(row=12, column=3, padx=10, pady=5, sticky="ew")

        self.cw_pv_t_max_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="panels"
        )
        # self.cw_pv_t_max_unit.grid(row=12, column=4, padx=10, pady=5, sticky="w")

        self.cw_pv_t_step_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Clean-water PV-T step size"
        )
        # self.cw_pv_t_step_label.grid(row=13, column=0, padx=10, pady=5, sticky="w")
        self.cw_pv_t_step = ttk.IntVar(self, 0)

        self.cw_pv_t_step_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.cw_pv_t_step,
            state=DISABLED,
        )
        # self.cw_pv_t_step_entry.grid(row=13, column=1, padx=10, pady=5, sticky="ew")

        self.cw_pv_t_step_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="panels"
        )
        # self.cw_pv_t_step_unit.grid(row=13, column=2, padx=10, pady=5, sticky="w")

        # Solar Thermal step size
        self.solar_thermal_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Solar-thermal min"
        )
        # self.solar_thermal_label.grid(row=14, column=0, padx=10, pady=5, sticky="w")

        self.solar_thermal_min = ttk.IntVar(self, 0)
        self.solar_thermal_min_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.solar_thermal_min,
            state=DISABLED,
        )
        # self.solar_thermal_min_entry.grid(
        #     row=14, column=1, padx=10, pady=5, sticky="ew"
        # )

        self.solar_thermal_min_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="panels"
        )
        # self.solar_thermal_min_unit.grid(row=14, column=2, padx=10, pady=5, sticky="w")

        self.solar_thermal_max_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Solar-thermal max"
        )
        # self.solar_thermal_max_label.grid(row=14, column=2, padx=10, pady=5, sticky="e")

        self.solar_thermal_max = ttk.IntVar(self, 0)
        self.solar_thermal_max_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.solar_thermal_max,
            state=DISABLED,
        )
        # self.solar_thermal_max_entry.grid(
        #     row=14, column=3, padx=10, pady=5, sticky="ew"
        # )

        self.solar_thermal_max_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="panels"
        )
        # self.solar_thermal_max_unit.grid(row=14, column=4, padx=10, pady=5, sticky="w")

        self.solar_thermal_step_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Solar-thermal step size"
        )
        # self.solar_thermal_step_label.grid(
        #     row=15, column=0, padx=10, pady=5, sticky="w"
        # )
        self.solar_thermal_step = ttk.IntVar(self, 0)

        self.solar_thermal_step_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.solar_thermal_step,
            state=DISABLED,
        )
        # self.solar_thermal_step_entry.grid(
        #     row=15, column=1, padx=10, pady=5, sticky="ew"
        # )

        self.solar_thermal_step_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="panels"
        )
        # self.solar_thermal_step_unit.grid(row=15, column=2, padx=10, pady=5, sticky="w")

        # Line break
        self.line_break_label = ttk.Label(self.scrollable_optimisation_frame, text="")
        self.line_break_label.grid(row=16, column=0, padx=10, pady=5, sticky="w")

        # Hot Water Tanks step size
        self.hot_water_tanks_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Hot-water tanks"
        )
        # self.hot_water_tanks_label.grid(row=14, column=0, padx=10, pady=5, sticky="w")

        self.hot_water_tanks_min_label = ttk.Label(
            self.scrollable_optimisation_frame, text="min"
        )
        # self.hot_water_tanks_min_label.grid(
        #     row=15, column=0, padx=10, pady=5, sticky="w"
        # )

        self.hot_water_tanks_min = ttk.IntVar(self, 0)
        self.hot_water_tanks_min_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.hot_water_tanks_min,
            state=DISABLED,
        )
        # self.hot_water_tanks_min_entry.grid(
        # #     row=15, column=1, padx=10, pady=5, sticky="ew"
        # # )

        self.hot_water_tanks_min_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="tanks"
        )
        # self.hot_water_tanks_min_unit.grid(row=15, column=2, padx=10, pady=5, sticky="w")

        self.hot_water_tanks_max_label = ttk.Label(
            self.scrollable_optimisation_frame, text="max"
        )
        # self.hot_water_tanks_max_label.grid(
        #     row=15, column=2, padx=10, pady=5, sticky="e"
        # )

        self.hot_water_tanks_max = ttk.IntVar(self, 0)
        self.hot_water_tanks_max_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.hot_water_tanks_max,
            state=DISABLED,
        )
        # self.hot_water_tanks_max_entry.grid(
        #     row=15, column=3, padx=10, pady=5, sticky="ew"
        # )

        self.hot_water_tanks_max_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="tanks"
        )
        # self.hot_water_tanks_max_unit.grid(row=15, column=4, padx=10, pady=5, sticky="w")

        self.hot_water_tanks_step_label = ttk.Label(
            self.scrollable_optimisation_frame, text="step"
        )
        # self.hot_water_tanks_step_label.grid(
        #     row=15, column=4, padx=10, pady=5, sticky="e"
        # )
        self.hot_water_tanks_step = ttk.IntVar(self, 0)

        self.hot_water_tanks_step_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.solar_thermal_step,
            state=DISABLED,
        )
        # self.hot_water_tanks_step_entry.grid(
        #     row=15, column=5, padx=10, pady=5, sticky="ew"
        # )

        self.hot_water_tanks_step_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="tanks"
        )
        # self.hot_water_tanks_step_unit.grid(
        #     row=15, column=6, padx=10, pady=5, sticky="w"
        # )

        # Clean-water Tanks step size
        self.clean_water_tanks_label = ttk.Label(
            self.scrollable_optimisation_frame, text="Clean-water tanks"
        )
        # self.clean_water_tanks_label.grid(row=16, column=0, padx=10, pady=5, sticky="w")

        self.clean_water_tanks_min_label = ttk.Label(
            self.scrollable_optimisation_frame, text="min"
        )
        # self.clean_water_tanks_min_label.grid(
        #     row=17, column=0, padx=10, pady=5, sticky="w"
        # )

        self.clean_water_tanks_min = ttk.IntVar(self, 0)
        self.clean_water_tanks_min_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.clean_water_tanks_min,
            state=DISABLED,
        )
        # self.clean_water_tanks_min_entry.grid(
        #     row=17, column=1, padx=10, pady=5, sticky="ew"
        # )

        self.clean_water_tanks_min_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="tanks"
        )
        # self.clean_water_tanks_min_unit.grid(
        #     row=17, column=2, padx=10, pady=5, sticky="w"
        # )

        self.clean_water_tanks_max_label = ttk.Label(
            self.scrollable_optimisation_frame, text="max"
        )
        # self.clean_water_tanks_max_label.grid(
        #     row=17, column=2, padx=10, pady=5, sticky="e"
        # )

        self.clean_water_tanks_max = ttk.IntVar(self, 0)
        self.clean_water_tanks_max_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.clean_water_tanks_max,
            state=DISABLED,
        )
        # self.clean_water_tanks_max_entry.grid(
        #     row=17, column=3, padx=10, pady=5, sticky="ew"
        # )

        self.clean_water_tanks_max_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="tanks"
        )
        # self.clean_water_tanks_max_unit.grid(
        #     row=17, column=4, padx=10, pady=5, sticky="w"
        # )

        self.clean_water_tanks_step_label = ttk.Label(
            self.scrollable_optimisation_frame, text="step"
        )
        # self.clean_water_tanks_step_label.grid(
        #     row=17, column=4, padx=10, pady=5, sticky="e"
        # )
        self.clean_water_tanks_step = ttk.IntVar(self, 0)

        self.clean_water_tanks_step_entry = ttk.Entry(
            self.scrollable_optimisation_frame,
            bootstyle=SECONDARY,
            textvariable=self.clean_water_tanks_step,
            state=DISABLED,
        )
        # self.clean_water_tanks_step_entry.grid(
        #     row=17, column=5, padx=10, pady=5, sticky="ew"
        # )

        self.clean_water_tanks_step_unit = ttk.Label(
            self.scrollable_optimisation_frame, text="tanks"
        )
        # self.clean_water_tanks_step_unit.grid(
        #     row=17, column=6, padx=10, pady=5, sticky="w"
        # )

        # Horizontal separator
        self.separator = ttk.Separator(self.scrollable_optimisation_frame)
        self.separator.grid(row=18, column=0, columnspan=5, sticky="ew")

        # Optimisation criterion header
        self.optimisation_criterion_label = ttk.Label(
            self.scrollable_optimisation_frame,
            text="Optimisation criterion",
            style="Bold.TLabel",
        )
        self.optimisation_criterion_label.grid(
            row=19, column=0, padx=10, pady=5, sticky="w"
        )

        # Optimisation criterion frame
        # self.scrollable_optimisation_frame = ttk.Labelframe(
        #     self, style="info.TLabelframe", text="Optimisation criterion"
        # )
        # self.scrollable_optimisation_frame.grid(
        #     row=2,
        #     column=0,
        #     columnspan=2,
        #     padx=5,
        #     pady=10,
        #     ipady=40,
        #     ipadx=20,
        #     sticky="news",
        # )

        # self.scrollable_optimisation_frame.rowconfigure(0, weight=1)

        # self.scrollable_optimisation_frame.columnconfigure(0, weight=3)
        # self.scrollable_optimisation_frame.columnconfigure(1, weight=1)
        # self.scrollable_optimisation_frame.columnconfigure(2, weight=3)

        # Optimisation Min/Max set
        self.optimisation_minmax = ttk.StringVar(self, "Minimise", "Minimum/Maximum")
        self.optimisation_minmax_entry = ttk.Combobox(
            self.scrollable_optimisation_frame,
            bootstyle=INFO,
            textvariable=self.optimisation_minmax,
            width=15,
        )
        self.optimisation_minmax_entry.grid(
            row=20, column=0, padx=10, pady=5, sticky="ew", ipadx=10
        )
        self.populate_minmax()

        # the
        self.optimisation_minmax_label = ttk.Label(
            self.scrollable_optimisation_frame, text="the"
        )
        self.optimisation_minmax_label.grid(
            row=20, column=1, padx=10, pady=5, sticky="ew"
        )

        # Optimisation criterion set
        self.optimisation_criterion = ttk.StringVar(
            self, "LCUE", "Optimisation Criterion"
        )
        self.optimisation_criterion_entry = ttk.Combobox(
            self.scrollable_optimisation_frame,
            bootstyle=INFO,
            textvariable=self.optimisation_criterion,
        )
        self.optimisation_criterion_entry.grid(
            row=20, column=2, padx=10, pady=5, sticky="ew", ipadx=10
        )
        self.populate_available_optimisation_criterion()

        # Line break
        self.line_break = ttk.Label(self.scrollable_optimisation_frame, text="")
        self.line_break.grid(row=21, column=1, padx=10, pady=5, sticky="w")

        # Horizontal separator
        self.separator = ttk.Separator(self.scrollable_optimisation_frame)
        self.separator.grid(row=22, column=0, columnspan=7, sticky="ew")

        # Threshold criteria header
        self.threshold_criteria_label = ttk.Label(
            self.scrollable_optimisation_frame,
            text="Threshold criteria",
            style="Bold.TLabel",
        )
        self.threshold_criteria_label.grid(
            row=23, column=0, padx=10, pady=5, sticky="w"
        )

        # Threshold criteria frame
        # self.threshold_criteria_frame = ttk.Labelframe(
        #     self, style="info.TLabelframe", text="Threshold criteria"
        # )
        # self.threshold_criteria_frame.grid(
        #     row=3,
        #     column=0,
        #     columnspan=2,
        #     padx=5,
        #     pady=10,
        #     ipady=60,
        #     ipadx=20,
        #     sticky="news",
        # )

        # self.threshold_criteria_frame.rowconfigure(0, weight=1, pad=40)
        # self.threshold_criteria_frame.rowconfigure(1, weight=4)

        # self.threshold_criteria_frame.columnconfigure(0, weight=1)
        # self.threshold_criteria_frame.columnconfigure(1, weight=1)
        # self.threshold_criteria_frame.columnconfigure(2, weight=1)
        # self.threshold_criteria_frame.columnconfigure(3, weight=1)

        # # Create the scrollable frame for threshold criteria
        # self.scrollable_threshold_frame = ScrolledFrame(self.scrollable_optimisation_frame)
        # self.scrollable_threshold_frame.grid(
        #     row=1,
        #     column=0,
        #     columnspan=4,
        #     padx=10,
        #     pady=5,
        #     sticky="ew",
        #     ipadx=10,
        #     ipady=30,
        # )

        # self.scrollable_threshold_frame.columnconfigure(0, weight=1)
        # self.scrollable_threshold_frame.columnconfigure(1, weight=1)
        # self.scrollable_threshold_frame.columnconfigure(2, weight=1)
        # self.scrollable_threshold_frame.columnconfigure(3, weight=1)

        self.threshold_criteria: list[ThresholdCriterion] = []

        def add_threshold_criterion() -> None:
            """Add a new threshold criterion to the list."""
            self.threshold_criteria.append(
                ThresholdCriterion(
                    self.scrollable_optimisation_frame,
                    ttk.StringVar(
                        self, ThresholdCriterion.default_threshold_criterion()
                    ),
                    ttk.BooleanVar(self, True),
                    ttk.DoubleVar(self, 0),
                    self.delete_criterion,
                    len(self.threshold_criteria) + 1,
                )
            )
            self.update_threshold_criteria()

        self.add_threshold_criterion_button = ttk.Button(
            self.scrollable_optimisation_frame,
            bootstyle=f"{INFO}-{OUTLINE}",
            command=add_threshold_criterion,
            text="Add threshold criterion",
        )
        self.add_threshold_criterion_button.grid(
            row=24, column=0, padx=10, pady=5, sticky="w", ipadx=40
        )

        self.update_threshold_criteria()

        # Combines the functions to open the run screen and launch the simulation.
        self.run_optimisation_frame = ttk.Frame(self)
        self.run_optimisation_frame.grid(row=5, column=0, columnspan=4)

        self.run_optimisation_frame.columnconfigure(0, weight=1, minsize=800)
        self.run_optimisation_frame.columnconfigure(2, weight=1)
        self.run_optimisation_frame.rowconfigure(0, weight=1)

        self.run_optimisation_button = ttk.Button(
            self.run_optimisation_frame,
            text="Run Optimisation",
            bootstyle=f"{INFO}-outline",
            command=lambda operating_mode=OperatingMode.OPTIMISATION: launch_clover_run(
                operating_mode
            ),
        )
        self.run_optimisation_button.grid(
            row=0, column=1, padx=5, pady=5, sticky="es", ipadx=80, ipady=20
        )

        # TODO: Add configuration frame widgets and layout

    @property
    def as_dict(
        self,
    ) -> dict[
        str,
        dict[str, float] | float | list[dict[str, list[dict[str, float | str]] | str]],
    ]:
        """
        Return the optimisation screen information as a `dict`.

        In order to update the optimisation inputs file ready to run a CLOVER
        optimisation, the optimisation inputs information needs to be saved.

        :returns:
            The optimisation information ready to be saved.

        """

        return {
            ITERATION_LENGTH: self.iteration_length.get(),
            NUMBER_OF_ITERATIONS: self.number_of_iterations.get(),
            OptimisationComponent.PV_SIZE.value: {
                MAX: self.pv_max.get(),
                MIN: self.pv_min.get(),
                STEP: self.pv_step.get(),
            },
            OptimisationComponent.STORAGE_SIZE.value: {
                MAX: self.storage_max.get(),
                MIN: self.storage_min.get(),
                STEP: self.storage_step.get(),
            },
            OPTIMISATIONS: [
                {
                    OPTIMISATION_CRITERIA: [
                        {
                            ThresholdCriterion.name_to_criterion_map[
                                self.optimisation_criterion.get()
                            ]
                            .value: self.optimisation_minmax.get()
                            .lower()
                        }
                    ],
                    THRESHOLD_CRITERIA: [
                        {
                            ThresholdCriterion.name_to_criterion_map[
                                criterion.criterion_name.get()
                            ].value: criterion.value.get()
                            for criterion in self.threshold_criteria
                        }
                    ],
                }
            ],
        }

    def delete_criterion(self, criterion_to_delete: ThresholdCriterion) -> None:
        """
        Remove a threshold criterion from the `list` and the screen.

        :param: criterion
            The :class:`ThresholdCriterion` to delete.

        """

        for criterion in self.threshold_criteria:
            criterion.grid_forget()

        self.threshold_criteria = [
            entry
            for entry in self.threshold_criteria
            if entry is not criterion_to_delete
        ]
        del criterion
        self.update_threshold_criteria()

    def populate_available_optimisation_criterion(self) -> None:
        """Populate the combo box with the set of avialable batteries."""

        self.optimisation_criterion_entry["values"] = [
            "LCUE ($/kWh)",
            "Emissions intensity (gCO2/kWh)",
            "Unmet energy fraction",
            "Blackouts",
            "Clean water blackouts",
            "Cumulative cost ($)",
            "Cumulative ghgs (kgCO2eq)",
            "Cumulative system cost ($)",
            "Cumulative system ghgs (kgCO2eq)",
            "Total_cost ($)",
            "Total system cost ($)",
            "Total ghgs (kgCO2eq)",
            "Total system ghgs (kgCO2eq)",
            "Kerosene cost mitigated ($)",
            "Kerosene ghgsm mitigated (kgCO2eq)",
            "Renewables fraction",
        ]

    def populate_minmax(self) -> None:
        """Populate the combo box with minmax."""

        self.optimisation_minmax_entry["values"] = [
            "Minimise",
            "Maximise",
        ]

    def set_optimisation(
        self, optimisation: Optimisation, optimisation_inputs: OptimisationParameters
    ) -> None:
        """
        Set the optimisation information based on the inputs.

        :param: optimisation
            The optimisation to use.

        :param: optimisation_inputs
            The optimisation inputs to use.

        """

        # Iteration parameters
        self.iteration_length.set(optimisation_inputs.iteration_length)
        self.iteration_length_entry.update()
        self.iteration_length_slider.set(self.iteration_length.get())

        self.number_of_iterations.set(optimisation_inputs.number_of_iterations)
        self.number_of_iterations_entry.update()
        self.number_of_iterations_slider.set(self.number_of_iterations.get())

        # Steps
        # PV steps
        self.pv_min.set(optimisation_inputs.pv_size.min)
        self.pv_min_entry.update()
        self.pv_max.set(optimisation_inputs.pv_size.max)
        self.pv_max_entry.update()
        self.pv_step.set(optimisation_inputs.pv_size.step)
        self.pv_step_entry.update()

        # Storage steps
        self.storage_min.set(optimisation_inputs.storage_size.min)
        self.storage_min_entry.update()
        self.storage_max.set(optimisation_inputs.storage_size.max)
        self.storage_max_entry.update()
        self.storage_step.set(optimisation_inputs.storage_size.step)
        self.storage_step_entry.update()

        # PV-T steps
        self.hw_pv_t_min.set(optimisation_inputs.hw_pvt_size.min)
        self.hw_pv_t_min_entry.update()
        self.hw_pv_t_max.set(optimisation_inputs.hw_pvt_size.max)
        self.hw_pv_t_max_entry.update()
        self.hw_pv_t_step.set(optimisation_inputs.hw_pvt_size.step)
        self.hw_pv_t_step_entry.update()

        self.cw_pv_t_min.set(optimisation_inputs.cw_pvt_size.min)
        self.cw_pv_t_min_entry.update()
        self.cw_pv_t_max.set(optimisation_inputs.cw_pvt_size.max)
        self.cw_pv_t_max_entry.update()
        self.cw_pv_t_step.set(optimisation_inputs.cw_pvt_size.step)
        self.cw_pv_t_step_entry.update()

        # Solar-thermal steps
        # self.solar_thermal_min.set(optimisation_inputs.hw_st_size.min)
        # self.solar_thermal_min_entry.update()
        # self.solar_thermal_max.set(optimisation_inputs.hw_st_size.max)
        # self.solar_thermal_max_entry.update()
        # self.solar_thermal_step.set(optimisation_inputs.hw_st_size.step)
        # self.solar_thermal_step_entry.update()

        # Clean water tanks steps
        self.clean_water_tanks_min.set(optimisation_inputs.clean_water_tanks.min)
        self.clean_water_tanks_min_entry.update()
        self.clean_water_tanks_max.set(optimisation_inputs.clean_water_tanks.max)
        self.clean_water_tanks_max_entry.update()
        self.clean_water_tanks_step.set(optimisation_inputs.clean_water_tanks.step)
        self.clean_water_tanks_step_entry.update()

        # Hot-water tanks steps
        self.hot_water_tanks_min.set(optimisation_inputs.hot_water_tanks.min)
        self.hot_water_tanks_min_entry.update()
        self.hot_water_tanks_max.set(optimisation_inputs.hot_water_tanks.max)
        self.hot_water_tanks_max_entry.update()
        self.hot_water_tanks_step.set(optimisation_inputs.hot_water_tanks.step)
        self.hot_water_tanks_step_entry.update()

        # Update optimisation criteria
        for criterion, criterion_mode in optimisation.optimisation_criteria.items():
            self.optimisation_criterion.set(
                ThresholdCriterion.criterion_to_name_map[criterion]
            )
            self.optimisation_criterion_entry.update()

            self.optimisation_minmax.set(criterion_mode.value.capitalize())
            self.optimisation_minmax_entry.update()

        # Update threshold criteria
        self.threshold_criteria = []
        for index, criterion in enumerate(optimisation.threshold_criteria):
            self.threshold_criteria.append(
                ThresholdCriterion(
                    self.scrollable_optimisation_frame,
                    ttk.StringVar(
                        self, ThresholdCriterion.criterion_to_name_map[criterion]
                    ),
                    ttk.BooleanVar(
                        self,
                        THRESHOLD_CRITERION_TO_MODE[criterion] == ThresholdMode.MAXIMUM,
                    ),
                    ttk.DoubleVar(self, optimisation.threshold_criteria[criterion]),
                    self.delete_criterion,
                    index + 1,
                )
            )

        self.update_threshold_criteria()

    def update_threshold_criteria(self) -> None:
        """Updates the threshold criteria being displayed."""

        for index, criterion in enumerate(self.threshold_criteria):
            criterion.set_index(index + 1)
            criterion.display()


class ConfigurationScreen(BaseScreen, show_navigation=True):
    """
    Represents the configuration screen.

    The configure screen contains tabbed information for configuring the screen.

    TODO: Update attributes.

    """

    def __init__(
        self,
        data_directory: str,
        location_name: ttk.StringVar,
        open_details_window: Callable,
        save_configuration: Callable,
        system_lifetime: ttk.IntVar,
        open_run_screen: Callable,
    ) -> None:
        """
        Instantiate a :class:`ConfigureFrame` instance.

        :param: data_directory
            The path to the data directory.

        :param: location_name
            The name of the location being considered.

        :param: open_details_window
            A callable function to open the details screen.

        :param: save_configuration
            A callable function to save the configuration.

        :param: system_lifetime
            The lifetime of the system, in years.

        """

        super().__init__()

        self.open_run_screen: Callable = open_run_screen
        self.save_configuration: Callable = save_configuration
        self.system_lifetime: ttk.IntVar = system_lifetime

        self.pack(fill="both", expand=True)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=10)
        self.columnconfigure(4, weight=1)

        self.rowconfigure(0, weight=1, minsize=80)
        self.rowconfigure(1, weight=1, minsize=600)
        self.rowconfigure(2, weight=1, minsize=80)

        self.location_label = ttk.Label(
            self, bootstyle=INFO, text=location_name.get().capitalize(), font="80"
        )
        self.location_label.grid(
            row=0, column=0, columnspan=4, sticky="ew", padx=60, pady=20
        )

        self.location_name: ttk.Stringvar = location_name

        self.configuration_notebook = ttk.Notebook(self, bootstyle=f"{INFO}")
        self.configuration_notebook.grid(
            row=1, column=0, columnspan=5, sticky="news", padx=60, pady=20
        )  # Use grid

        style = ttk.Style()
        style.configure("TNotebook.Tab", width=int(self.winfo_screenwidth() / 4))

        self.configuration_frame = ConfigurationFrame(
            self.configuration_notebook, data_directory, open_details_window
        )
        self.configuration_notebook.add(
            self.configuration_frame, text="Configure", sticky="news"
        )

        self.simulation_frame = SimulationFrame(
            self.configuration_notebook,
            lambda operating_mode=OperatingMode.SIMULATION: self.launch_clover_run(
                operating_mode
            ),
        )
        self.configuration_notebook.add(self.simulation_frame, text="Simulate")

        self.optimisation_frame = OptimisationFrame(
            self.configuration_notebook,
            lambda operating_mode=OperatingMode.OPTIMISATION: self.launch_clover_run(
                operating_mode
            ),
            self.system_lifetime,
        )
        self.configuration_notebook.add(self.optimisation_frame, text="Optimise")

        self.bottom_bar_frame = ttk.Frame(self)
        self.bottom_bar_frame.grid(row=2, column=0, columnspan=5, sticky="news")

        self.bottom_bar_frame.columnconfigure(0, weight=1)
        self.bottom_bar_frame.columnconfigure(1, weight=1)
        self.bottom_bar_frame.columnconfigure(2, weight=1)
        self.bottom_bar_frame.columnconfigure(3, weight=10)
        self.bottom_bar_frame.columnconfigure(4, weight=1)

        self.back_button = ttk.Button(
            self.bottom_bar_frame,
            text="Back",
            bootstyle=f"{PRIMARY}-{OUTLINE}",
            command=lambda self=self: BaseScreen.go_back(self),
        )
        self.back_button.grid(row=0, column=0, padx=10, pady=5)

        self.home_button = ttk.Button(
            self.bottom_bar_frame,
            text="Home",
            bootstyle=f"{PRIMARY}-{OUTLINE}",
            command=lambda self=self: BaseScreen.go_home(self),
        )
        self.home_button.grid(row=0, column=1, padx=10, pady=5)

        self.forward_button = ttk.Button(
            self.bottom_bar_frame,
            text="Forward",
            bootstyle=f"{PRIMARY}-{OUTLINE}",
            command=lambda self=self: BaseScreen.go_forward(self),
        )
        self.forward_button.grid(row=0, column=2, padx=10, pady=5)

        self.advanced_settings_button = ttk.Button(
            self.bottom_bar_frame,
            bootstyle=INFO,
            text="Advanced settings",
            command=open_details_window,
        )
        self.advanced_settings_button.grid(
            row=0, column=4, sticky="w", pady=5, ipadx=80, ipady=20
        )

    def launch_clover_run(self, operating_mode: OperatingMode) -> None:
        """Launch a CLOVER simulation."""

        # Save all input files before running.
        self.save_configuration()

        # Assemble arguments and call to CLOVER.
        clover_args: list[str] = [
            "-l",
            str(self.location_name.get()),
        ]

        # Append simulation arguments:
        if operating_mode == OperatingMode.SIMULATION:
            clover_args.extend(["-sim", "-a"])

            # Append the PV size if PV is selected
            if self.configuration_frame.solar_pv_selected.get():
                clover_args.extend(
                    [
                        "-pv",
                        str(self.simulation_frame.pv_size.get()),
                    ]
                )

            # Append the battery size if batteries are selected
            if self.configuration_frame.battery_selected.get():
                clover_args.extend(
                    [
                        "-b",
                        str(self.simulation_frame.storage_size.get()),
                    ]
                )

            if not self.simulation_frame.generate_plots.get():
                clover_args.append("-sp")

            # Append the datetime to the output name then append to the arguments
            clover_args.extend(
                [
                    "-o",
                    str(self.simulation_frame.output_name.get())
                    + datetime.datetime.now().strftime("_%Y_%m_%d_%H_%M_%S_%f"),
                ]
            )

        if operating_mode == OperatingMode.OPTIMISATION:
            clover_args.extend(["-opt"])

            # Append the datetime to the output name then append to the arguments
            # self.simulation_frame.output_name.get() + datetime.datetime.now().strftime("_%Y_%m_%d_%H_%M_%S_%f")

        self.clover_thread = clover_thread(clover_args)
        self.open_run_screen(self.clover_thread)

    def set_location(self, location_name: str) -> None:
        """
        Set the location name on the screen.

        :param: location_name
            The name of the location to set.

        """

        self.location_name.set(location_name)
        self.location_label.configure(text=self.location_name.get())
