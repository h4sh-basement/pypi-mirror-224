import asyncio
from typing import Dict, Iterator, List, Tuple, Union

import duckdb
from textual import work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.css.query import NoMatches
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import (
    ContentSwitcher,
    DataTable,
    LoadingIndicator,
    TabbedContent,
    TabPane,
)
from textual.worker import Worker, WorkerState

from harlequin.tui.utils import short_type


class ResultsTable(DataTable):
    DEFAULT_CSS = """
        ResultsTable {
            height: 100%;
            width: 100%;
        }
    """


class ResultsViewer(ContentSwitcher, can_focus=True):
    TABBED_ID = "tabs"
    LOADING_ID = "loading"
    data: reactive[Dict[str, List[Tuple]]] = reactive(dict)
    BINDINGS = [
        Binding("j", "switch_tab(-1)", "Previous Tab", show=False),
        Binding("k", "switch_tab(1)", "Next Tab", show=False),
    ]

    class Ready(Message):
        pass

    def __init__(
        self,
        *children: Widget,
        name: Union[str, None] = None,
        id: Union[str, None] = None,  # noqa A002
        classes: Union[str, None] = None,
        disabled: bool = False,
        initial: Union[str, None] = None,
        max_results: int = 10_000,
    ) -> None:
        super().__init__(
            *children,
            name=name,
            id=id,
            classes=classes,
            disabled=disabled,
            initial=initial,
        )
        self.MAX_RESULTS = max_results

    def compose(self) -> ComposeResult:
        yield TabbedContent(id=self.TABBED_ID)
        yield LoadingIndicator(id=self.LOADING_ID)

    def on_mount(self) -> None:
        self.border_title = "Query Results"
        self.current = self.TABBED_ID
        self.tab_switcher = self.query_one(TabbedContent)

    def on_focus(self) -> None:
        self._focus_on_visible_table()

    def _focus_on_visible_table(self) -> None:
        maybe_table = self.get_visible_table()
        if maybe_table is not None:
            maybe_table.focus()

    def on_tabbed_content_tab_activated(
        self, message: TabbedContent.TabActivated
    ) -> None:
        message.stop()
        # Don't update the border if we're still loading the table.
        if self.border_title and str(self.border_title).startswith("Loading"):
            return
        maybe_table = self.get_visible_table()
        if maybe_table is not None and self.data:
            id_ = maybe_table.id
            assert id_ is not None
            self.border_title = f"Query Results {self._human_row_count(self.data[id_])}"

    def action_switch_tab(self, offset: int) -> None:
        if not self.tab_switcher.active:
            return
        tab_number = int(self.tab_switcher.active.split("-")[1])
        unsafe_tab_number = tab_number + offset
        if unsafe_tab_number < 1:
            new_tab_number = self.tab_switcher.tab_count
        elif unsafe_tab_number > self.tab_switcher.tab_count:
            new_tab_number = 1
        else:
            new_tab_number = unsafe_tab_number
        self.tab_switcher.active = f"tab-{new_tab_number}"
        self._focus_on_visible_table()

    def get_visible_table(self) -> Union[ResultsTable, None]:
        content = self.tab_switcher.query_one(ContentSwitcher)
        active_tab_id = self.tab_switcher.active
        if active_tab_id:
            try:
                tab_pane = content.query_one(f"#{active_tab_id}", TabPane)
                return tab_pane.query_one(ResultsTable)
            except NoMatches:
                return None
        else:
            tables = content.query(ResultsTable)
            try:
                return tables.first(ResultsTable)
            except NoMatches:
                return None

    async def watch_data(self, data: Dict[str, List[Tuple]]) -> None:
        if data:
            await self.set_not_responsive(data=data)
            self.load_data(data=data)

    @work(exclusive=True, group="data_loaders", description="Loading data.")
    async def load_data(self, data: Dict[str, List[Tuple]]) -> Dict[str, List[Tuple]]:
        for table_id, result in data.items():
            table = self.tab_switcher.query_one(f"#{table_id}", ResultsTable)
            for i, chunk in self.chunk(result[: self.MAX_RESULTS]):
                table.add_rows(chunk)
                self.increment_progress_bar()
                await asyncio.sleep(0)
                if i == 0:
                    self.show_table()
        return data

    def on_worker_state_changed(self, event: Worker.StateChanged) -> None:
        if (
            event.worker.name == "load_data"
            and event.worker.state == WorkerState.SUCCESS
        ):
            self.set_responsive(data=event.worker.result)
            self.post_message(self.Ready())
            self.focus()

    @staticmethod
    def chunk(
        data: List[Tuple], chunksize: int = 1000
    ) -> Iterator[Tuple[int, List[Tuple]]]:
        for i in range(len(data) // chunksize + 1):
            yield i, data[i * chunksize : (i + 1) * chunksize]

    async def set_not_responsive(self, data: Dict[str, List[Tuple]]) -> None:
        if len(data) > 1:
            self.border_title = f"Loading Data from {len(data):,} Queries."
        elif data:
            self.border_title = (
                f"Loading Data {self._human_row_count(next(iter(data.values())))}."
            )
        self.add_class("non-responsive")

    def increment_progress_bar(self) -> None:
        self.border_title = f"{self.border_title}."

    def set_responsive(
        self,
        data: Union[Dict[str, List[Tuple]], None] = None,
        did_run: bool = True,
    ) -> None:
        if not did_run:
            self.border_title = "Query Results"
        elif data is None:
            self.border_title = "Query Returned No Records"
        else:
            table = self.get_visible_table()
            if table is not None:
                id_ = table.id
                assert id_ is not None
                self.border_title = f"Query Results {self._human_row_count(data[id_])}"
            else:
                self.border_title = (
                    f"Query Results {self._human_row_count(next(iter(data.values())))}"
                )
        self.remove_class("non-responsive")

    def _human_row_count(self, data: List[Tuple]) -> str:
        if (total_rows := len(data)) > self.MAX_RESULTS:
            return f"(Showing {self.MAX_RESULTS:,} of {total_rows:,} Records)"
        else:
            return f"({total_rows:,} Records)"

    def show_table(self) -> None:
        self.current = self.TABBED_ID

    def push_table(self, table_id: str, relation: duckdb.DuckDBPyRelation) -> None:
        table = ResultsTable(id=table_id)
        short_types = [short_type(t) for t in relation.dtypes]
        table.add_columns(
            *[
                f"{name} [#888888]{data_type}[/]"
                for name, data_type in zip(relation.columns, short_types)
            ]
        )
        n = self.tab_switcher.tab_count + 1
        if n > 1:
            self.remove_class("hide-tabs")
        pane = TabPane(f"Result {n}", table)
        self.tab_switcher.add_pane(pane)

    def clear_all_tables(self) -> None:
        self.tab_switcher.clear_panes()
        self.add_class("hide-tabs")

    def show_loading(self) -> None:
        self.current = self.LOADING_ID
        self.border_title = "Running Query"
        self.add_class("non-responsive")

    def get_loading(self) -> LoadingIndicator:
        loading = self.get_child_by_id(self.LOADING_ID, expect_type=LoadingIndicator)
        return loading
