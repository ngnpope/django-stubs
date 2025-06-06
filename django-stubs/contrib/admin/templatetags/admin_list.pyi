from collections.abc import Iterator
from typing import Any

from django.contrib.admin.filters import FieldListFilter
from django.contrib.admin.views.main import ChangeList
from django.db.models.base import Model
from django.forms.boundfield import BoundField
from django.forms.models import ModelForm
from django.template.base import Parser, Token
from django.template.context import RequestContext
from django.utils.safestring import SafeString

from .base import InclusionAdminNode

register: Any

def paginator_number(cl: ChangeList, i: int) -> SafeString: ...
def pagination(cl: ChangeList) -> dict[str, Any]: ...
def pagination_tag(parser: Parser, token: Token) -> InclusionAdminNode: ...
def result_headers(cl: ChangeList) -> Iterator[dict[str, int | str | None]]: ...
def items_for_result(cl: ChangeList, result: Model, form: ModelForm | None) -> Iterator[SafeString]: ...

class ResultList(list):
    form: ModelForm | None
    def __init__(self, form: ModelForm | None, *items: Any) -> None: ...

def results(cl: ChangeList) -> Iterator[ResultList]: ...
def result_hidden_fields(cl: ChangeList) -> Iterator[BoundField]: ...
def result_list(
    cl: ChangeList,
) -> dict[str, list[dict[str, int | str | None]] | list[ResultList] | list[BoundField] | ChangeList | int]: ...
def result_list_tag(parser: Parser, token: Token) -> InclusionAdminNode: ...
def date_hierarchy(cl: ChangeList) -> dict[str, Any] | None: ...
def date_hierarchy_tag(parser: Parser, token: Token) -> InclusionAdminNode: ...
def search_form(cl: ChangeList) -> dict[str, bool | ChangeList | str]: ...
def search_form_tag(parser: Parser, token: Token) -> InclusionAdminNode: ...
def admin_list_filter(cl: ChangeList, spec: FieldListFilter) -> SafeString: ...
def admin_actions(context: RequestContext) -> RequestContext: ...
def admin_actions_tag(parser: Parser, token: Token) -> InclusionAdminNode: ...
def change_list_object_tools_tag(parser: Parser, token: Token) -> InclusionAdminNode: ...
