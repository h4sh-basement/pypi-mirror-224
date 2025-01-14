# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class VendorCreditsRetrieveRequestExpand(str, enum.Enum):
    COMPANY = "company"
    LINES = "lines"
    LINES_COMPANY = "lines,company"
    LINES_TRACKING_CATEGORIES = "lines,tracking_categories"
    LINES_TRACKING_CATEGORIES_COMPANY = "lines,tracking_categories,company"
    LINES_TRACKING_CATEGORIES_VENDOR = "lines,tracking_categories,vendor"
    LINES_TRACKING_CATEGORIES_VENDOR_COMPANY = "lines,tracking_categories,vendor,company"
    LINES_VENDOR = "lines,vendor"
    LINES_VENDOR_COMPANY = "lines,vendor,company"
    TRACKING_CATEGORIES = "tracking_categories"
    TRACKING_CATEGORIES_COMPANY = "tracking_categories,company"
    TRACKING_CATEGORIES_VENDOR = "tracking_categories,vendor"
    TRACKING_CATEGORIES_VENDOR_COMPANY = "tracking_categories,vendor,company"
    VENDOR = "vendor"
    VENDOR_COMPANY = "vendor,company"

    def visit(
        self,
        company: typing.Callable[[], T_Result],
        lines: typing.Callable[[], T_Result],
        lines_company: typing.Callable[[], T_Result],
        lines_tracking_categories: typing.Callable[[], T_Result],
        lines_tracking_categories_company: typing.Callable[[], T_Result],
        lines_tracking_categories_vendor: typing.Callable[[], T_Result],
        lines_tracking_categories_vendor_company: typing.Callable[[], T_Result],
        lines_vendor: typing.Callable[[], T_Result],
        lines_vendor_company: typing.Callable[[], T_Result],
        tracking_categories: typing.Callable[[], T_Result],
        tracking_categories_company: typing.Callable[[], T_Result],
        tracking_categories_vendor: typing.Callable[[], T_Result],
        tracking_categories_vendor_company: typing.Callable[[], T_Result],
        vendor: typing.Callable[[], T_Result],
        vendor_company: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VendorCreditsRetrieveRequestExpand.COMPANY:
            return company()
        if self is VendorCreditsRetrieveRequestExpand.LINES:
            return lines()
        if self is VendorCreditsRetrieveRequestExpand.LINES_COMPANY:
            return lines_company()
        if self is VendorCreditsRetrieveRequestExpand.LINES_TRACKING_CATEGORIES:
            return lines_tracking_categories()
        if self is VendorCreditsRetrieveRequestExpand.LINES_TRACKING_CATEGORIES_COMPANY:
            return lines_tracking_categories_company()
        if self is VendorCreditsRetrieveRequestExpand.LINES_TRACKING_CATEGORIES_VENDOR:
            return lines_tracking_categories_vendor()
        if self is VendorCreditsRetrieveRequestExpand.LINES_TRACKING_CATEGORIES_VENDOR_COMPANY:
            return lines_tracking_categories_vendor_company()
        if self is VendorCreditsRetrieveRequestExpand.LINES_VENDOR:
            return lines_vendor()
        if self is VendorCreditsRetrieveRequestExpand.LINES_VENDOR_COMPANY:
            return lines_vendor_company()
        if self is VendorCreditsRetrieveRequestExpand.TRACKING_CATEGORIES:
            return tracking_categories()
        if self is VendorCreditsRetrieveRequestExpand.TRACKING_CATEGORIES_COMPANY:
            return tracking_categories_company()
        if self is VendorCreditsRetrieveRequestExpand.TRACKING_CATEGORIES_VENDOR:
            return tracking_categories_vendor()
        if self is VendorCreditsRetrieveRequestExpand.TRACKING_CATEGORIES_VENDOR_COMPANY:
            return tracking_categories_vendor_company()
        if self is VendorCreditsRetrieveRequestExpand.VENDOR:
            return vendor()
        if self is VendorCreditsRetrieveRequestExpand.VENDOR_COMPANY:
            return vendor_company()
