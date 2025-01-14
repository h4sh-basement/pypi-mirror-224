from __future__ import annotations

from tcsoa.gen.Reports._2007_01.CrfReports import ReportProperties, GetReportDefinitionsResponse, GenerateReportResponse, ReportsCriteria, GenerateReportCriteria, CreateReportDefinitionResponse, GenerateReportDefintionIdsResponse
from typing import List
from tcsoa.base import TcService


class CrfReportsService(TcService):

    @classmethod
    def getReportDefinitions(cls, inputCriteria: List[ReportsCriteria]) -> GetReportDefinitionsResponse:
        """
        Retrieves a set of report definitions that meet the specified criteria.
        
        Use cases:
        Document set of user level use cases, should describe how user interacts with this operation to accomplish the
        goal.
        """
        return cls.execute_soa_method(
            method_name='getReportDefinitions',
            library='Reports',
            service_date='2007_01',
            service_name='CrfReports',
            params={'inputCriteria': inputCriteria},
            response_cls=GetReportDefinitionsResponse,
        )

    @classmethod
    def createReportDefinition(cls, reportProperties: ReportProperties) -> CreateReportDefinitionResponse:
        """
        Creates a report definition with the specified properties.
        """
        return cls.execute_soa_method(
            method_name='createReportDefinition',
            library='Reports',
            service_date='2007_01',
            service_name='CrfReports',
            params={'reportProperties': reportProperties},
            response_cls=CreateReportDefinitionResponse,
        )

    @classmethod
    def generateReport(cls, inputCriteria: GenerateReportCriteria, applicationId: str) -> GenerateReportResponse:
        """
        Generates report (Summary Report/Custom Report/Item Report) using the specified criteria and the selected
        report style sheet. The report can be displayed with the selected report style. The report style is used to
        define how to display the report result in UI to end user. The report can optionally be saved as a Dataset in
        the Teamcenter database. The generated report is saved in the FMS transient volume and an FMS ticket is
        returned.
        
        Use cases:
        User can generate one report (Summary Report/Custom Report/Item Report) by selecting one report definition and
        then inputs criteria for the report query, selects one report style sheet, and inputs the dataset name for the
        report if user would like to save the report as a dataset in Teamcenter.
        """
        return cls.execute_soa_method(
            method_name='generateReport',
            library='Reports',
            service_date='2007_01',
            service_name='CrfReports',
            params={'inputCriteria': inputCriteria, 'applicationId': applicationId},
            response_cls=GenerateReportResponse,
        )

    @classmethod
    def generateReportDefintionIds(cls, inputCriteria: List[ReportsCriteria]) -> GenerateReportDefintionIdsResponse:
        """
        Generates new report definition id(s) based upon the specified report criteria. This operation is used when
        user creates new report definition; the report definition id is generated by this operation. Multiple report
        definition id generation is not supported currently.
        
        Use cases:
        User creates a new report definition from the New Report wizard. User presses the button to generate the report
        definition id for the new report definition. This operation will be triggered to generate the report definition
        id and assign to the new report definition.
        """
        return cls.execute_soa_method(
            method_name='generateReportDefintionIds',
            library='Reports',
            service_date='2007_01',
            service_name='CrfReports',
            params={'inputCriteria': inputCriteria},
            response_cls=GenerateReportDefintionIdsResponse,
        )
