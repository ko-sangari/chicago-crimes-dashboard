import datetime

import streamlit_mock


def test_input_widgets():
    sm = streamlit_mock.StreamlitMock()
    sm.run("main_outputs.py")

    results = sm.get_results()

    assert results.header == ["header"]
    assert results.title == ["Output examples"]
    assert results.caption == ["caption"]
    assert results.code == ["code"]
    assert results.text == ["text"]
    assert results.json == [{"key": "value"}]
    assert results.markdown == ["markdown"]

    assert len(results.dataframe) == 1
    assert len(results.table) == 1
    assert len(results.bar_chart) == 1
    assert len(results.map) == 1
