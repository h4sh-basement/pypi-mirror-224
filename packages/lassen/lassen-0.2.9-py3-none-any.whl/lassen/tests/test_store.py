from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Query, Session

from lassen.enums import FilterTypeEnum
from lassen.store import StoreBase, StoreFilterMixin
from lassen.tests.model_fixtures import (
    SampleModel,
    SampleSchemaCreate,
    SampleSchemaFilter,
    SampleSchemaUpdate,
)


@pytest.fixture
def use_fixture_models(db_session: Session):
    if not db_session.bind:
        raise ValueError("No database connection")

    from lassen.db.base_class import Base

    Base.metadata.create_all(bind=db_session.bind)


def create_batch(db_session: Session, quantity: int = 1):
    create_identifiers = []
    for i in range(quantity):
        test_model = SampleModel(name=f"Test Model {i}")
        db_session.add(test_model)
        db_session.flush()
        db_session.refresh(test_model)
        create_identifiers.append(test_model.id)
    return create_identifiers


def test_store_base_get(db_session: Session, use_fixture_models):
    test_model_id = create_batch(db_session, quantity=1)[0]

    store = StoreBase[SampleModel, SampleSchemaCreate, SampleSchemaUpdate](SampleModel)
    # Test with a valid ID
    retrieved = store.get(db_session, id=test_model_id)
    assert retrieved is not None
    assert retrieved.id == test_model_id
    assert retrieved.name == "Test Model 0"

    # Test with an invalid ID
    assert store.get(db_session, id=9999) is None


def test_store_base_get_multi(db_session: Session, use_fixture_models):
    create_batch(db_session, quantity=5)

    store = StoreFilterMixin[SampleModel, SampleSchemaFilter](SampleModel)
    # Test without skip and limit
    retrieved = store.get_multi(db_session, filter=SampleSchemaFilter())
    assert len(retrieved) == 5

    # Test with skip
    retrieved = store.get_multi(db_session, skip=2, filter=SampleSchemaFilter())
    assert len(retrieved) == 3

    # Test with limit
    retrieved = store.get_multi(db_session, limit=2, filter=SampleSchemaFilter())
    assert len(retrieved) == 2

    # Test with skip and limit
    retrieved = store.get_multi(
        db_session, skip=1, limit=2, filter=SampleSchemaFilter()
    )
    assert len(retrieved) == 2


def test_store_base_update(db_session: Session, use_fixture_models):
    test_model_id = create_batch(db_session, quantity=1)[0]

    store = StoreBase[SampleModel, SampleSchemaCreate, SampleSchemaUpdate](SampleModel)
    update_schema = SampleSchemaUpdate(id=test_model_id, name="Updated Name")
    db_obj = store.get(db_session, id=test_model_id)
    assert db_obj is not None

    updated = store.update(db_session, db_obj=db_obj, obj_in=update_schema)
    db_session.commit()
    assert updated.id == test_model_id
    assert updated.name == "Updated Name"


def test_store_base_remove(db_session: Session, use_fixture_models):
    test_model_id = create_batch(db_session, quantity=1)[0]

    store = StoreBase[SampleModel, SampleSchemaCreate, SampleSchemaUpdate](SampleModel)
    store.remove(db_session, id=test_model_id)
    db_session.commit()

    # Test that the model instance has been removed
    assert store.get(db_session, id=test_model_id) is None


@pytest.mark.parametrize(
    "filter_type,expected_expression",
    [
        (FilterTypeEnum.EQUAL, lambda x, y: x == y),
        (FilterTypeEnum.NOT, lambda x, y: x != y),
        (FilterTypeEnum.IN, lambda x, y: x.in_(y)),
        (FilterTypeEnum.NOT_IN, lambda x, y: ~x.in_(y)),
        (FilterTypeEnum.LESS_THAN, lambda x, y: x < y),
        (FilterTypeEnum.LESS_THAN_OR_EQUAL, lambda x, y: x <= y),
        (FilterTypeEnum.GREATER_THAN, lambda x, y: x > y),
        (FilterTypeEnum.GREATER_THAN_OR_EQUAL, lambda x, y: x >= y),
    ],
)
def test_build_filter(filter_type, expected_expression, use_fixture_models):
    # Mock FilterSchemaType
    mock_filter = MagicMock()
    value = (
        ["mock_name"]
        if filter_type in {FilterTypeEnum.IN, FilterTypeEnum.NOT_IN}
        else "mock_name"
    )
    mock_filter.dict.return_value = {f"name__{filter_type.value}": value}

    # Mock Query
    mock_query = MagicMock(spec=Query)
    mock_query.filter.return_value = MagicMock(
        spec=Query
    )  # Return a new mock query for each filter() call

    store = StoreFilterMixin[SampleModel, SampleSchemaFilter](SampleModel)
    store.build_filter(mock_query, mock_filter, include_archived=True)

    # Check the correct function was called with the right arguments
    # Each accessor to
    expected = expected_expression(SampleModel.name, value)
    call_strings = [str(call[0][0]) for call in mock_query.filter.call_args_list]
    assert str(expected) in call_strings


def test_supports_all_filters():
    """
    All FilterSchemaType values defined in the enum are correctly parsed and supported
    in our build_filter method.

    """
    for filter_type in FilterTypeEnum:
        # Mock FilterSchemaType
        mock_filter = MagicMock()
        value = (
            ["mock_name"]
            if filter_type in {FilterTypeEnum.IN, FilterTypeEnum.NOT_IN}
            else "mock_name"
        )
        mock_filter.dict.return_value = {f"name__{filter_type.value}": value}

        # Mock Query
        mock_query = MagicMock(spec=Query)

        store = StoreFilterMixin[SampleModel, SampleSchemaFilter](SampleModel)
        assert (
            store.build_filter(mock_query, mock_filter, include_archived=True)
            is not None
        )
