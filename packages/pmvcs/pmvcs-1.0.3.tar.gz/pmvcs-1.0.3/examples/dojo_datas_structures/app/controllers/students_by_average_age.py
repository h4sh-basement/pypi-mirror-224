""" Students By Average Age Controller file for Dojo_Datastructures
Reto: Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35)."""
from app.controllers.base_controller import BaseController
from app.models.students_by_average_age import StudentsByAverageAgeModel
from app.views.students_by_average_age import StudentsByAverageAgeView


class StudentsByAverageAgeController(BaseController):
    """ Class for Students By Average Age Controller  """

    def __init__(self, **kwargs) -> None:
        """
        Init Students By Average Age Controller requirements
        """
        super().__init__(**kwargs)

        self.model = StudentsByAverageAgeModel(**kwargs)
        self.view = StudentsByAverageAgeView(**kwargs)

        self.model.data = self.data_model

    def _get_submenu_section_data(self) -> list:
        """
        Returns submenu section data
        """
        return ['18-25', '26-35', '> 35']

    def _get_submenu_section_message(self) -> str:
        """
        Returns submenu option message
        """
        return self.lang.get("LANG_SELECT_AVERAGE_AGE")

    def _get_submenu_section_path(self, section: str) -> list:
        """
        Returns submenu range_age path
        """
        return [self.lang.sprintf("LANG_PATH_AGE_RANGE", section)]

    def _get_submenu_formats_path(self, section: str, formats: str) -> list:
        """
        Returns submenu formats path
        """
        return [self.lang.sprintf("LANG_PATH_AGE_RANGE", section),
                self.lang.sprintf("LANG_PATH_FORMAT", self.lang.translate(formats))]

    def _get_submenu_output_path(self, section: str, formats: str, output: str) -> list:
        """
        Returns submenu output path
        """
        return [self.lang.sprintf("LANG_PATH_AGE_RANGE", section),
                self.lang.sprintf("LANG_PATH_FORMAT",
                                  self.lang.translate(formats)),
                self.lang.sprintf("LANG_PATH_OUTPUT", self.lang.translate(output))]

    def _get_submenu_path(self, *args) -> list:
        """
        Returns submenu path
        """
        if len(args) == 1:
            return self._get_submenu_section_path(args[0])

        if len(args) == 2:
            return self._get_submenu_formats_path(args[0], args[1])

        if len(args) == 3:
            return self._get_submenu_output_path(args[0], args[1], args[2])

        return args
