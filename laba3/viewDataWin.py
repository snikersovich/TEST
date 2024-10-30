import pytest
from viewDataWin import ViewDataWindow


def test_data_display(db_connection):
    db = DatabaseClass(db_connection)
    db.add_record("Тест записи")
    view_window = ViewDataWindow(db_connection)

    assert view_window.displayed_data() == ["Тест записи"]


def test_data_update_after_addition(db_connection):
    db = DatabaseClass(db_connection)
    db.add_record("Запись 1")
    view_window = ViewDataWindow(db_connection)

    db.add_record("Запись 2")
    assert view_window.displayed_data() == ["Запись 1", "Запись 2"]