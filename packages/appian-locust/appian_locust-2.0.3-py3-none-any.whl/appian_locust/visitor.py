from typing import Optional

from ._actions import _Actions
from ._design import _Design
from ._interactor import _Interactor
from ._portals import _Portals
from ._records import _Records
from ._reports import _Reports
from ._sites import _Sites
from ._admin import _Admin
from ._tasks import _Tasks
from .utilities.helper import format_label
from .objects import DesignObjectType, PageType
from .uiform import ApplicationUiForm, DesignUiForm, DesignObjectUiForm, RecordInstanceUiForm, RecordListUiForm, SailUiForm


class Visitor:
    """
    Provides methods to get an interactable ``SailUiForm`` from an Appian instance. Each method will return the respected ``SailUiForm`` type for which it will allow
    interactions with the visited page.
    """

    def __init__(self, interactor: _Interactor, tasks: _Tasks, reports: _Reports, actions: _Actions, records: _Records,
                 sites: _Sites):
        self.__interactor = interactor
        self.__tasks = tasks
        self.__reports = reports
        self.__records = records
        self.__sites = sites
        self.__actions = actions
        self.__design = _Design(self.__interactor)
        self.__admin = _Admin(self.__interactor)
        self.__portals = _Portals(self.__interactor)

    def visit_task(self, task_name: str, exact_match: bool = True, locust_request_label: str = "") -> SailUiForm:
        """
        Gets the SailUiForm given a task name

        Args:
            task_name (str): Name of the task to search for
            exact_match (bool, optional): Whether or not a full match is returned. Defaults to True.
            locust_request_label (str, optional): label to be used within locust

        Returns:
            SailUiForm: SAIL form for the task
        """
        initial_task_resp: dict = self.__tasks.get_task(task_name, exact_match)
        children = initial_task_resp.get("content", {}).get("children", [])
        task_title = children[0]

        if not locust_request_label:
            breadcrumb = f"Tasks.{task_title}"
        else:
            breadcrumb = locust_request_label
        return SailUiForm(self.__interactor, self.__tasks.get_task_form_json(task_name=task_title, locust_request_label=breadcrumb, exact_match=False), breadcrumb=breadcrumb)

    def visit_report(self, report_name: str, exact_match: bool = True, locust_request_label: Optional[str] = None) -> 'SailUiForm':
        """
        Navigate to a report and return a SailUiForm for that report's UI

        Args:
            report_name (str): Name of the report to be called.
            exact_match (bool, optional): Should report name match exactly or to be partial match. Default : True
            locust_request_label (str, optional): Label locust should associate this request with

        Returns (SailUiForm): Response of report's Get UI call in SailUiForm

        """
        breadcrumb = f'Reports.SailUi.{format_label(report_name, "::", 0)}'
        locust_request_label = locust_request_label or f"Visit.Report.{report_name}"
        return SailUiForm(self.__interactor, self.__reports.fetch_report_json(report_name, exact_match, locust_request_label=locust_request_label), breadcrumb=breadcrumb)

    def visit_design(self) -> DesignUiForm:
        """
        Navigate to /design
        Returns (DesignUiForm): UiForm representing /design

        """
        return DesignUiForm(self.__interactor, self.__design.fetch_design_json(), breadcrumb="Design.ApplicationList.SailUi")

    def visit_application_by_id(self, application_id: str) -> ApplicationUiForm:
        """
        Visit an application by its opaque id

        Args:
            application_id (str): The opaque id of the application

        Returns (ApplicationUiForm): UiForm representing design application page

        """
        breadcrumb = f"Design.SelectedApplication.{application_id}.SailUi"
        return ApplicationUiForm(self.__interactor, self.__design.fetch_application_json(application_id), breadcrumb)

    def visit_application_by_name(self, application_name: str, application_prefix: Optional[str] = None) -> ApplicationUiForm:
        """
        Visit an application by name

        Args:
            application_name (str): The name of the application
            application_prefix (str, optional): The prefix of the application. Required if the application has a prefix.

        Returns (ApplicationUiForm): UiForm representing design application page

        """
        design_uiForm = self.visit_design()
        design_uiForm.search_applications(application_name)
        if application_prefix:
            application_name = f"{application_name} ({application_prefix})"
        application_uiform = design_uiForm.click_application(application_name)
        return application_uiform

    def visit_design_object_by_id(self, opaque_id: str) -> DesignObjectUiForm:
        """
        Visit a design object by its opaque id
        Args:
            opaque_id (str): opaque id of the design object

        Returns (DesignObjectUiForm): UiForm representing design object

        """
        breadcrumb = "Design.SelectedObject." + opaque_id[0:10] + ".SailUi"
        return DesignObjectUiForm(self.__interactor, self.__design.fetch_design_object_json(opaque_id), breadcrumb)

    def visit_design_object_by_name(self, object_name: str, object_type: DesignObjectType) -> DesignObjectUiForm:
        """
        Visit a design object by its name and type
        Args:
            object_name (str): The name of the design object
            object_type (DesignObjectType): The type of the design object

        Returns:

        """
        designUiForm: DesignUiForm = self.visit_design()
        designUiForm.select_nav_card_by_index(nav_group_label="leftNavbar", is_test_label=True, index=1)
        designUiForm.check_checkbox_by_test_label(test_label="object-type-checkbox", indices=[object_type.value])
        designUiForm.search_objects(object_name)
        design_object_opaque_id = self.__design.find_design_object_opaque_id_in_grid(object_name, designUiForm.get_latest_state())
        return self.visit_design_object_by_id(design_object_opaque_id)

    def visit_record_instance(self, record_type: str = "", record_name: str = "", view_url_stub: str = "",
                              exact_match: bool = False, summary_view: bool = True,
                              locust_request_label: Optional[str] = None) -> RecordInstanceUiForm:
        """
        Navigate to a specific record and return a RecordUiForm

        Args:
            record_type (str): Record Type Name. If not specified, a random record type will be selected.
            record_name (str): Name of the record to be called. If not specified, a random record will be selected.
            view_url_stub (str, optional): page/tab to be visited in the record. If not specified, "summary" dashboard will be selected.
            exact_match (bool, optional): Should record type and record name matched exactly as it is or partial match.
            summary_view (bool, optional): Should the Record UI be returned in Summary View, if false will return Header View
            locust_request_label (str, optional): Label locust should associate this request with

        Returns (RecordUiForm): The UI for the record instance

        """
        self.__records.get_records_nav(locust_request_label=locust_request_label)
        form_json = self.__records.visit_record_instance(record_type, record_name, view_url_stub=view_url_stub,
                                                         exact_match=exact_match, locust_request_label=locust_request_label)
        breadcrumb = f'Records.{record_type}.{format_label(record_name, "::", 0)}.SailUi'
        return RecordInstanceUiForm(self.__interactor, form_json, summary_view=summary_view, breadcrumb=breadcrumb)

    def visit_record_type(self, record_type: str = "",
                          locust_request_label: Optional[str] = None) -> RecordListUiForm:
        """
        This function calls the API for the specific record type and returns a SAIL form representing the list of records for that record type.

        Args:
            record_type (str): Record Type Name. If not specified, a random record type will be selected.
            locust_request_label (str, optional): Label locust should associate this request with

        Returns (SailUiForm): UI representing list of records for that record type
        """
        self.__records.get_records_nav(locust_request_label=locust_request_label)
        form_json = self.__records.visit_record_type(record_type, locust_request_label=locust_request_label)
        breadcrumb = f'Records.{record_type}.RecordListUi'
        return RecordListUiForm(self.__interactor, form_json, breadcrumb=breadcrumb)

    def visit_site(self, site_name: str, page_name: str) -> SailUiForm:
        """
        Get a SailUiForm for a Task, Report or Action

        Args:
            site_name(str): Site where the page exists
            page_name(str): Page to navigate to

        Returns: SailUiForm

        Example:
            >>> self.appian.visitor.visit_site("site_name","page_name")

        """
        form_json = self.__sites.fetch_site_tab_json(site_name, page_name)

        breadcrumb = f"Sites.{site_name}.{page_name}.SailUi"
        return SailUiForm(self.__interactor, form_json, breadcrumb=breadcrumb)

    def visit_admin(self) -> SailUiForm:
        """
        Navigates to /admin

        Returns: SailUiForm

        """
        form_json = self.__admin.fetch_admin_json()

        breadcrumb = f"Admin.MainMenu.SailUi"
        return SailUiForm(self.__interactor, form_json, breadcrumb=breadcrumb)

    def visit_site_recordlist(self, site_name: str, page_name: str) -> 'RecordListUiForm':
        """
        Get a RecordListUiForm for a record list page on a site

        Args:
            site_name(str): Site where the page exists
            page_name(str): Page to navigate to

        NOTE: The actual Type of the Site Page MUST be "Record List", this will not work for sites that are of other page types,
              such as an Interface with a record grid.

        Returns: SailUiForm

        Example:
            >>> self.appian.visitor.visit_site_recordlist("site_name","page_name")

        """
        page_type = self.__sites.get_site_page_type(site_name, page_name)
        if page_type != PageType.RECORD:
            raise Exception(f"Page {page_name} on site {site_name} is not of type record")
        form_json = self.__sites.fetch_site_tab_json(site_name, page_name)

        breadcrumb = f"Sites.{site_name}.{page_name}.SailUi"
        return RecordListUiForm(self.__interactor, form_json, breadcrumb=breadcrumb)

    def visit_site_recordlist_and_get_random_record_form(self, site_name: str, page_name: str) -> RecordInstanceUiForm:
        """
        Navigates to a site page that is a recordlist then clicks on a random record instance on the first page

        Args:
            site_name: Site Url stub
            page_name: Page Url stub

        NOTE: The actual Type of the Site Page MUST be "Record List", this will not work for sites that are of other page types,
              such as an Interface with a record grid.

        Returns: RecordInstanceUiForm
        """

        site_page_json_response = self.__sites.fetch_site_tab_record_json(site_name, page_name)
        summary_view = site_page_json_response.get("feed") is not None
        breadcrumb = f"Sites.{site_name}.{page_name}.SailUi"
        return RecordInstanceUiForm(self.__interactor, site_page_json_response, summary_view=summary_view, breadcrumb=breadcrumb)

    def visit_action(self, action_name: str, exact_match: bool = False, locust_request_label: str = "") -> SailUiForm:
        """
        Gets the action by name and returns the corresponding SailUiForm to interact with

        If the action is activity chained, this will attempt to start the process and retrieve the chained SAIL form.

        Args:
            action_name (str): Name of the action to be called. Name of the action will be in the below pattern.
                         "displayLabel::opaquqId"
            exact_match (bool, optional): Should action name match exactly or to be partial match. Default : False
            locust_request_label (str, optional): label to be used within locust. Default: '' (empty string)

        Returns: SailUiForm

        Examples:

            If the full name of the action is known, with the opaque ID,

            >>> self.appian.visitor.visit_action("action_name:igB0K7YxC0UQ2Fhx4hicRw...", exact_match=True)

            If only the display name is known, or part of the display name

            >>> self.appian.visitor.visit_action("action_name")
            >>> self.appian.visitor.visit_action("actio")
        """
        action_key = format_label(action_name, "::", 0)
        label = locust_request_label or f'Actions.GetUi.{action_key}'
        form_json = self.__actions.fetch_action_json(action_name, exact_match, label)
        return SailUiForm(self.__interactor, form_json, breadcrumb=label)

    def visit_portal_page(self, portal_unique_identifier: str, portal_page_unique_identifier: str) -> SailUiForm:
        """
        Navigate to portal's page by url and returns the corresponding SailUiForm to interact with

        Args:
            portal_unique_identifier (str): portal web address unique identifier
            portal_page_unique_identifier (str): web address unique identifier for specific page in portal

        Returns: SailUiForm

        Examples:

            If we have portal up and running with 2 pages with title "page1" and "page2", we can
            visit any portal page with help of this method.

            In order to visit "page1" with url (in browser: https://mysite.appian-internal.com/performance-testing/page/page1),
            we would use

            >>> self.appian.visitor.visit_portal_page("performance-testing", "page1")

            In order to visit "page2" with url (in browser: https://mysite.appian-internal.com/performance-testing/page/page2),
            we would use

            >>> self.appian.visitor.visit_portal_page("performance-testing", "page2")

        Note: sometimes when portal has just 1 page (for example page with title 'page1').
        appian use only "https://mysite.appian-internal.com/performance-testing" (in browser)
        instead of https://mysite.appian-internal.com/performance-testing/page/page1 . although it still works.
        """
        form_json = self.__portals.fetch_page_json(portal_unique_identifier, portal_page_unique_identifier)
        breadcrumb = f"Portals.{_Portals.get_full_url(portal_unique_identifier, portal_page_unique_identifier)}.SailUi"
        return SailUiForm(self.__interactor, form_json, breadcrumb=breadcrumb)
