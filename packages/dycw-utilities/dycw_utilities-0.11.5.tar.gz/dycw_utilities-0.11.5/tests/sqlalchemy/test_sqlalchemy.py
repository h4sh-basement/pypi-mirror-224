import enum
from enum import auto
from pathlib import Path
from typing import Any, Optional, TypedDict, Union, cast

import sqlalchemy
from beartype import beartype
from hypothesis import assume, given
from hypothesis.strategies import (
    DataObject,
    booleans,
    data,
    fixed_dictionaries,
    integers,
    lists,
    none,
    permutations,
    sampled_from,
    sets,
)
from hypothesis_sqlalchemy.sample import table_records_lists
from pytest import mark, param, raises
from sqlalchemy import (
    BIGINT,
    BINARY,
    BOOLEAN,
    CHAR,
    CLOB,
    DATE,
    DATETIME,
    DECIMAL,
    DOUBLE,
    DOUBLE_PRECISION,
    FLOAT,
    INT,
    INTEGER,
    NCHAR,
    NUMERIC,
    NVARCHAR,
    REAL,
    SMALLINT,
    TEXT,
    TIME,
    TIMESTAMP,
    UUID,
    VARBINARY,
    VARCHAR,
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Double,
    Float,
    Integer,
    Interval,
    LargeBinary,
    MetaData,
    Numeric,
    Sequence,
    SmallInteger,
    String,
    Table,
    Text,
    Time,
    Unicode,
    UnicodeText,
    Uuid,
    func,
    insert,
    select,
)
from sqlalchemy import create_engine as _create_engine
from sqlalchemy.engine import Connection, Engine
from sqlalchemy.exc import DatabaseError, NoSuchTableError
from sqlalchemy.orm import declarative_base

from utilities.hypothesis import lists_fixed_length, temp_paths, text_ascii
from utilities.hypothesis.sqlalchemy import sqlite_engines
from utilities.platform import SYSTEM, System
from utilities.sqlalchemy import (
    EngineError,
    IncorrectNumberOfTablesError,
    ParseEngineError,
    TableAlreadyExistsError,
    TablenameMixin,
    UnequalBooleanColumnCreateConstraintError,
    UnequalBooleanColumnNameError,
    UnequalColumnTypesError,
    UnequalDateTimeColumnTimezoneError,
    UnequalEnumColumnCreateConstraintError,
    UnequalEnumColumnInheritSchemaError,
    UnequalEnumColumnLengthError,
    UnequalEnumColumnNativeEnumError,
    UnequalEnumColumnTypesError,
    UnequalFloatColumnAsDecimalError,
    UnequalFloatColumnDecimalReturnScaleError,
    UnequalFloatColumnPrecisionsError,
    UnequalIntervalColumnDayPrecisionError,
    UnequalIntervalColumnNativeError,
    UnequalIntervalColumnSecondPrecisionError,
    UnequalLargeBinaryColumnLengthError,
    UnequalNullableStatusError,
    UnequalNumberOfColumnsError,
    UnequalNumericScaleError,
    UnequalPrimaryKeyStatusError,
    UnequalSetOfColumnsError,
    UnequalStringCollationError,
    UnequalStringLengthError,
    UnequalTableOrColumnNamesError,
    UnequalTableOrColumnSnakeCaseNamesError,
    UnequalUUIDAsUUIDError,
    UnequalUUIDNativeUUIDError,
    _check_column_collections_equal,
    _check_column_types_equal,
    _check_columns_equal,
    _check_table_or_column_names_equal,
    _reflect_table,
    check_engine,
    check_table_against_reflection,
    check_tables_equal,
    columnwise_max,
    columnwise_min,
    create_engine,
    ensure_engine,
    ensure_table_created,
    ensure_table_dropped,
    get_column_names,
    get_columns,
    get_dialect,
    get_table,
    get_table_name,
    model_to_dict,
    next_from_sequence,
    parse_engine,
    redirect_to_no_such_table_error,
    redirect_to_table_already_exists_error,
    serialize_engine,
    yield_connection,
    yield_in_clause_rows,
)


class TestCheckColumnsEqual:
    @beartype
    def test_equal(self) -> None:
        x = Column("id", Integer)
        _check_columns_equal(x, x)

    @beartype
    def test_names(self) -> None:
        x = Column("x", Integer)
        y = Column("y", Integer)
        with raises(UnequalTableOrColumnNamesError):
            _check_columns_equal(x, y)

    @beartype
    def test_column_types(self) -> None:
        x = Column("x", Integer)
        y = Column("x", String)
        with raises(UnequalColumnTypesError):
            _check_columns_equal(x, y)

    @beartype
    def test_primary_key_status(self) -> None:
        x = Column("id", Integer, primary_key=True)
        y = Column("id", Integer)
        with raises(UnequalPrimaryKeyStatusError):
            _check_columns_equal(x, y)

    @beartype
    def test_primary_key_status_skipped(self) -> None:
        x = Column("id", Integer, primary_key=True)
        y = Column("id", Integer, nullable=False)
        _check_columns_equal(x, y, primary_key=False)

    @beartype
    def test_nullable_status(self) -> None:
        x = Column("id", Integer)
        y = Column("id", Integer, nullable=False)
        with raises(UnequalNullableStatusError):
            _check_columns_equal(x, y)


class TestCheckColumnCollectionsEqual:
    @beartype
    def test_success(self) -> None:
        x = Table("x", MetaData(), Column("id", Integer, primary_key=True))
        _check_column_collections_equal(x.columns, x.columns)

    @beartype
    def test_snake(self) -> None:
        x = Table("x", MetaData(), Column("id", Integer, primary_key=True))
        y = Table("y", MetaData(), Column("Id", Integer, primary_key=True))
        _check_column_collections_equal(x.columns, y.columns, snake=True)

    @beartype
    def test_allow_permutations(self) -> None:
        x = Table(
            "x",
            MetaData(),
            Column("id1", Integer, primary_key=True),
            Column("id2", Integer, primary_key=True),
        )
        y = Table(
            "y",
            MetaData(),
            Column("id2", Integer, primary_key=True),
            Column("id1", Integer, primary_key=True),
        )
        _check_column_collections_equal(x.columns, y.columns, allow_permutations=True)

    @beartype
    def test_snake_and_allow_permutations(self) -> None:
        x = Table(
            "x",
            MetaData(),
            Column("id1", Integer, primary_key=True),
            Column("id2", Integer, primary_key=True),
        )
        y = Table(
            "y",
            MetaData(),
            Column("Id2", Integer, primary_key=True),
            Column("Id1", Integer, primary_key=True),
        )
        _check_column_collections_equal(
            x.columns, y.columns, snake=True, allow_permutations=True
        )

    @beartype
    def test_unequal_number_of_columns(self) -> None:
        x = Table("x", MetaData(), Column("id", Integer, primary_key=True))
        y = Table(
            "y",
            MetaData(),
            Column("id", Integer, primary_key=True),
            Column("value", Integer),
        )
        with raises(UnequalNumberOfColumnsError):
            _check_column_collections_equal(x.columns, y.columns)

    @beartype
    def test_unequal_set_of_columns(self) -> None:
        x = Table("x", MetaData(), Column("id1", Integer, primary_key=True))
        y = Table("y", MetaData(), Column("id2", Integer, primary_key=True))
        with raises(UnequalSetOfColumnsError):
            _check_column_collections_equal(x.columns, y.columns)

    @mark.parametrize("allow_permutation", [param(True), param(False)])
    @beartype
    def test_unequal_column_types(self, allow_permutation: bool) -> None:
        x = Table("x", MetaData(), Column("id", Integer, primary_key=True))
        y = Table("y", MetaData(), Column("id", String, primary_key=True))
        with raises(UnequalColumnTypesError):
            _check_column_collections_equal(
                x.columns, y.columns, allow_permutations=allow_permutation
            )


class TestCheckColumnTypesEqual:
    groups = (
        [BIGINT, INT, INTEGER, SMALLINT, BigInteger, Integer, SmallInteger],
        [BOOLEAN, Boolean],
        [DATE, Date],
        [DATETIME, TIMESTAMP, DateTime],
        [Interval],
        [BINARY, VARBINARY, LargeBinary],
        [
            DECIMAL,
            DOUBLE,
            DOUBLE_PRECISION,
            FLOAT,
            NUMERIC,
            REAL,
            Double,
            Float,
            Numeric,
        ],
        [
            CHAR,
            CLOB,
            NCHAR,
            NVARCHAR,
            TEXT,
            VARCHAR,
            String,
            Text,
            Unicode,
            UnicodeText,
            sqlalchemy.Enum,
        ],
        [TIME, Time],
        [UUID, Uuid],
    )

    @given(data=data())
    @beartype
    def test_equal(self, data: DataObject) -> None:
        group = data.draw(sampled_from(self.groups))
        cls = data.draw(sampled_from(group))
        elements = sampled_from([cls, cls()])
        x, y = data.draw(lists_fixed_length(elements, 2))
        _check_column_types_equal(x, y)

    @given(data=data())
    @beartype
    def test_unequal(self, data: DataObject) -> None:
        groups = self.groups
        i, j = data.draw(lists_fixed_length(integers(0, len(groups) - 1), 2))
        _ = assume(i != j)
        group_i, group_j = groups[i], groups[j]
        cls_x, cls_y = (data.draw(sampled_from(g)) for g in [group_i, group_j])
        x, y = (data.draw(sampled_from([c, c()])) for c in [cls_x, cls_y])
        with raises(UnequalColumnTypesError):
            _check_column_types_equal(x, y)

    @given(create_constraints=lists_fixed_length(booleans(), 2))
    @beartype
    def test_boolean_create_constraint(self, create_constraints: list[bool]) -> None:
        create_constraint_x, create_constraint_y = create_constraints
        x, y = (Boolean(create_constraint=cs) for cs in create_constraints)
        if create_constraint_x is create_constraint_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalBooleanColumnCreateConstraintError):
                _check_column_types_equal(x, y)

    @given(names=lists_fixed_length(text_ascii(min_size=1) | none(), 2))
    @beartype
    def test_boolean_name(self, names: list[Optional[str]]) -> None:
        name_x, name_y = names
        x, y = (Boolean(name=n) for n in names)
        if name_x == name_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalBooleanColumnNameError):
                _check_column_types_equal(x, y)

    @beartype
    def test_camel_versus_upper(self) -> None:
        _check_column_types_equal(Boolean, BOOLEAN)

    @given(timezones=lists_fixed_length(booleans(), 2))
    @beartype
    def test_datetime_timezone(self, timezones: list[bool]) -> None:
        timezone_x, timezone_y = timezones
        x, y = (DateTime(timezone=tz) for tz in timezones)
        if timezone_x is timezone_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalDateTimeColumnTimezoneError):
                _check_column_types_equal(x, y)

    @beartype
    def test_enum_two_enum_classes(self) -> None:
        class EnumX(enum.Enum):
            member = auto()

        class EnumY(enum.Enum):
            member = auto()

        x, y = (sqlalchemy.Enum(e) for e in [EnumX, EnumY])
        with raises(UnequalEnumColumnTypesError):
            _check_column_types_equal(x, y)

    @given(data=data())
    @beartype
    def test_enum_one_enum_class(self, data: DataObject) -> None:
        class MyEnum(enum.Enum):
            member = auto()

        x = sqlalchemy.Enum(MyEnum)
        y = data.draw(sampled_from([sqlalchemy.Enum, sqlalchemy.Enum()]))
        x, y = data.draw(permutations([x, y]))
        with raises(UnequalEnumColumnTypesError):
            _check_column_types_equal(x, y)

    @given(create_constraints=lists_fixed_length(booleans(), 2))
    @beartype
    def test_enum_create_constraint(self, create_constraints: list[bool]) -> None:
        class MyEnum(enum.Enum):
            member = auto()

        create_constraint_x, create_constraint_y = create_constraints
        x, y = (
            sqlalchemy.Enum(MyEnum, create_constraint=cs) for cs in create_constraints
        )
        if create_constraint_x is create_constraint_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalEnumColumnCreateConstraintError):
                _check_column_types_equal(x, y)

    @given(native_enums=lists_fixed_length(booleans(), 2))
    @beartype
    def test_enum_native_enum(self, native_enums: list[bool]) -> None:
        class MyEnum(enum.Enum):
            member = auto()

        native_enum_x, native_enum_y = native_enums
        x, y = (sqlalchemy.Enum(MyEnum, native_enum=ne) for ne in native_enums)
        if native_enum_x is native_enum_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalEnumColumnNativeEnumError):
                _check_column_types_equal(x, y)

    @given(lengths=lists_fixed_length(integers(6, 10), 2))
    @beartype
    def test_enum_length(self, lengths: list[int]) -> None:
        class MyEnum(enum.Enum):
            member = auto()

        length_x, length_y = lengths
        x, y = (sqlalchemy.Enum(MyEnum, length=l_) for l_ in lengths)
        if length_x == length_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalEnumColumnLengthError):
                _check_column_types_equal(x, y)

    @given(inherit_schemas=lists_fixed_length(booleans(), 2))
    @beartype
    def test_enum_inherit_schema(self, inherit_schemas: list[bool]) -> None:
        class MyEnum(enum.Enum):
            member = auto()

        inherit_schema_x, inherit_schema_y = inherit_schemas
        x, y = (sqlalchemy.Enum(MyEnum, inherit_schema=is_) for is_ in inherit_schemas)
        if inherit_schema_x is inherit_schema_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalEnumColumnInheritSchemaError):
                _check_column_types_equal(x, y)

    @given(
        cls=sampled_from([Float, Numeric]),
        precisions=lists_fixed_length(integers(0, 10) | none(), 2),
    )
    @beartype
    def test_float_precision(
        self, cls: Union[type[Float], type[Numeric]], precisions: list[Optional[int]]
    ) -> None:
        precision_x, precision_y = precisions
        x, y = (cls(precision=p) for p in precisions)
        if precision_x == precision_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalFloatColumnPrecisionsError):
                _check_column_types_equal(x, y)

    @given(
        cls=sampled_from([Float, Numeric]), asdecimals=lists_fixed_length(booleans(), 2)
    )
    @beartype
    def test_float_asdecimal(
        self, cls: Union[type[Float], type[Numeric]], asdecimals: list[bool]
    ) -> None:
        asdecimal_x, asdecimal_y = asdecimals
        x, y = (cls(asdecimal=cast(Any, a)) for a in asdecimals)
        if asdecimal_x is asdecimal_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalFloatColumnAsDecimalError):
                _check_column_types_equal(x, y)

    @given(
        cls=sampled_from([Float, Numeric]),
        dec_ret_scales=lists_fixed_length(integers(0, 10) | none(), 2),
    )
    @beartype
    def test_float_dec_ret_scale(
        self,
        cls: Union[type[Float], type[Numeric]],
        dec_ret_scales: list[Optional[int]],
    ) -> None:
        dec_ret_scale_x, dec_ret_scale_y = dec_ret_scales
        x, y = (cls(decimal_return_scale=drs) for drs in dec_ret_scales)
        if dec_ret_scale_x == dec_ret_scale_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalFloatColumnDecimalReturnScaleError):
                _check_column_types_equal(x, y)

    @given(natives=lists_fixed_length(booleans(), 2))
    @beartype
    def test_interval_native(self, natives: list[bool]) -> None:
        native_x, native_y = natives
        x, y = (Interval(native=n) for n in natives)
        if native_x is native_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalIntervalColumnNativeError):
                _check_column_types_equal(x, y)

    @given(second_precisions=lists_fixed_length(integers(0, 10) | none(), 2))
    @beartype
    def test_interval_second_precision(
        self, second_precisions: list[Optional[int]]
    ) -> None:
        second_precision_x, second_precision_y = second_precisions
        x, y = (Interval(second_precision=sp) for sp in second_precisions)
        if second_precision_x == second_precision_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalIntervalColumnSecondPrecisionError):
                _check_column_types_equal(x, y)

    @given(day_precisions=lists_fixed_length(integers(0, 10) | none(), 2))
    @beartype
    def test_interval_day_precision(self, day_precisions: list[Optional[int]]) -> None:
        day_precision_x, day_precision_y = day_precisions
        x, y = (Interval(day_precision=dp) for dp in day_precisions)
        if day_precision_x == day_precision_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalIntervalColumnDayPrecisionError):
                _check_column_types_equal(x, y)

    @given(lengths=lists_fixed_length(integers(0, 10) | none(), 2))
    @beartype
    def test_large_binary_length(self, lengths: list[Optional[int]]) -> None:
        length_x, length_y = lengths
        x, y = (LargeBinary(length=l_) for l_ in lengths)
        if length_x == length_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalLargeBinaryColumnLengthError):
                _check_column_types_equal(x, y)

    @given(scales=lists_fixed_length(integers(0, 10) | none(), 2))
    @beartype
    def test_numeric_scale(self, scales: list[Optional[int]]) -> None:
        scale_x, scale_y = scales
        x, y = (Numeric(scale=s) for s in scales)
        if scale_x == scale_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalNumericScaleError):
                _check_column_types_equal(x, y)

    @given(
        cls=sampled_from([String, Unicode, UnicodeText]),
        lengths=lists_fixed_length(integers(0, 10) | none(), 2),
    )
    @beartype
    def test_string_length(
        self,
        cls: Union[type[String], type[Unicode], type[UnicodeText]],
        lengths: list[Optional[int]],
    ) -> None:
        length_x, length_y = lengths
        x, y = (cls(length=l_) for l_ in lengths)
        if length_x == length_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalStringLengthError):
                _check_column_types_equal(x, y)

    @given(collations=lists_fixed_length(text_ascii(min_size=1) | none(), 2))
    @beartype
    def test_string_collation(self, collations: list[Optional[str]]) -> None:
        collation_x, collation_y = collations
        x, y = (String(collation=c) for c in collations)
        if collation_x == collation_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalStringCollationError):
                _check_column_types_equal(x, y)

    @given(as_uuids=lists_fixed_length(booleans(), 2))
    @beartype
    def test_uuid_as_uuid(self, as_uuids: list[bool]) -> None:
        as_uuid_x, as_uuid_y = as_uuids
        x, y = (Uuid(as_uuid=cast(Any, au)) for au in as_uuids)
        if as_uuid_x is as_uuid_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalUUIDAsUUIDError):
                _check_column_types_equal(x, y)

    @given(native_uuids=lists_fixed_length(booleans(), 2))
    @beartype
    def test_uuid_native_uuid(self, native_uuids: list[bool]) -> None:
        native_uuid_x, native_uuid_y = native_uuids
        x, y = (Uuid(native_uuid=nu) for nu in native_uuids)
        if native_uuid_x is native_uuid_y:
            _check_column_types_equal(x, y)
        else:
            with raises(UnequalUUIDNativeUUIDError):
                _check_column_types_equal(x, y)


class TestCheckEngine:
    @given(engine=sqlite_engines())
    @beartype
    def test_success(self, engine: Engine) -> None:
        check_engine(engine)

    @given(root=temp_paths())
    @beartype
    def test_engine_error(self, root: Path) -> None:
        engine = create_engine("sqlite", database=root.as_posix())
        with raises(EngineError):
            check_engine(engine)

    @given(engine=sqlite_engines())
    @beartype
    def test_num_tables(self, engine: Engine) -> None:
        table = Table("example", MetaData(), Column("id", Integer, primary_key=True))
        ensure_table_created(table, engine)
        check_engine(engine, num_tables=1)

    @given(engine=sqlite_engines())
    @beartype
    def test_num_tables_error(self, engine: Engine) -> None:
        with raises(IncorrectNumberOfTablesError):
            check_engine(engine, num_tables=1)

    @given(engine=sqlite_engines())
    @beartype
    def test_num_tables_rel_tol_correct(self, engine: Engine) -> None:
        table = Table("example", MetaData(), Column("id", Integer, primary_key=True))
        ensure_table_created(table, engine)
        check_engine(engine, num_tables=2, rel_tol=0.5)

    @given(engine=sqlite_engines())
    @beartype
    def test_num_tables_rel_tol_error(self, engine: Engine) -> None:
        with raises(IncorrectNumberOfTablesError):
            check_engine(engine, num_tables=1, rel_tol=0.5)

    @given(engine=sqlite_engines())
    @beartype
    def test_num_tables_abs_tol_correct(self, engine: Engine) -> None:
        check_engine(engine, num_tables=1, abs_tol=1)

    @given(engine=sqlite_engines())
    @beartype
    def test_num_tables_abs_tol_error(self, engine: Engine) -> None:
        with raises(IncorrectNumberOfTablesError):
            check_engine(engine, num_tables=2, abs_tol=1)


class TestCheckTableAgainstReflection:
    @given(engine=sqlite_engines())
    @beartype
    def test_reflected(self, engine: Engine) -> None:
        table = Table("example", MetaData(), Column("Id", Integer, primary_key=True))
        ensure_table_created(table, engine)
        check_table_against_reflection(table, engine)

    @given(engine=sqlite_engines())
    @beartype
    def test_no_such_table(self, engine: Engine) -> None:
        table = Table("example", MetaData(), Column("Id", Integer, primary_key=True))
        with raises(NoSuchTableError):
            _ = check_table_against_reflection(table, engine)


class TestCheckTablesEqual:
    @beartype
    def test_equal(self) -> None:
        table = Table("example", MetaData(), Column("id", Integer, primary_key=True))
        check_tables_equal(table, table)

    @beartype
    def test_column_collections(self) -> None:
        x = Table("example", MetaData(), Column("id", Integer, primary_key=True))
        y = Table(
            "example",
            MetaData(),
            Column("id", Integer, primary_key=True),
            Column("value", Integer),
        )
        with raises(UnequalNumberOfColumnsError):
            check_tables_equal(x, y)

    @beartype
    def test_snake_table(self) -> None:
        x = Table("example", MetaData(), Column("id", Integer, primary_key=True))
        y = Table("Example", MetaData(), Column("id", Integer, primary_key=True))
        check_tables_equal(x, y, snake_table=True)

    @beartype
    def test_snake_columns(self) -> None:
        x = Table("example", MetaData(), Column("id", Integer, primary_key=True))
        y = Table("example", MetaData(), Column("Id", Integer, primary_key=True))
        check_tables_equal(x, y, snake_columns=True)

    @beartype
    def test_orm(self) -> None:
        class Example(declarative_base()):
            __tablename__ = "example"

            Id = Column(Integer, primary_key=True)

        check_tables_equal(Example, Example)


class TestCheckTableOrColumnNamesEqual:
    @mark.parametrize(
        ("x", "y", "snake", "expected"),
        [
            param("x", "x", False, None),
            param("x", "x", True, None),
            param("x", "X", False, UnequalTableOrColumnNamesError),
            param("x", "X", True, None),
            param("x", "y", False, UnequalTableOrColumnNamesError),
            param("x", "y", True, UnequalTableOrColumnSnakeCaseNamesError),
        ],
    )
    @beartype
    def test_main(
        self, x: str, y: str, snake: bool, expected: Optional[type[Exception]]
    ) -> None:
        if expected is None:
            _check_table_or_column_names_equal(x, y, snake=snake)
        else:
            with raises(expected):
                _check_table_or_column_names_equal(x, y, snake=snake)

    @mark.parametrize(("name", "expected"), [param(None, "Id"), param("x", "x")])
    @beartype
    def test_orm(self, name: Optional[str], expected: str) -> None:
        class Kwargs(TypedDict, total=False):
            name: str

        class Example(declarative_base()):
            __tablename__ = "example"

            Id = Column(
                Integer,
                primary_key=True,
                **(cast(Kwargs, {} if name is None else {"name": name})),
            )

        _check_table_or_column_names_equal(Example.Id.name, expected)


class TestColumnwiseMinMax:
    @given(
        values=lists(
            fixed_dictionaries(
                {"x": integers(0, 100) | none(), "y": integers(0, 100) | none()}
            ),
            min_size=1,
            max_size=10,
        ),
        engine=sqlite_engines(),
    )
    @beartype
    def test_main(self, values: list[dict[str, Optional[int]]], engine: Engine) -> None:
        table = Table(
            "example",
            MetaData(),
            Column("id_", Integer, primary_key=True, autoincrement=True),
            Column("x", Integer),
            Column("y", Integer),
        )
        ensure_table_created(table, engine)
        with engine.begin() as conn:
            _ = conn.execute(table.insert(), values)
            res = conn.execute(table.select()).all()

        sel = select(
            table.c.x,
            table.c.y,
            columnwise_min(table.c.x, table.c.y).label("min_xy"),
            columnwise_max(table.c.x, table.c.y).label("max_xy"),
        )
        with engine.begin() as conn:
            res = conn.execute(sel).all()

        assert len(res) == len(values)
        for x, y, min_xy, max_xy in res:
            if (x is None) and (y is None):
                assert min_xy is None
                assert max_xy is None
            elif (x is not None) and (y is None):
                assert min_xy == x
                assert max_xy == x
            elif (x is None) and (y is not None):
                assert min_xy == y
                assert max_xy == y
            else:
                assert min_xy == min(x, y)
                assert max_xy == max(x, y)

    @given(engine=sqlite_engines())
    @beartype
    def test_label(self, engine: Engine) -> None:
        table = Table(
            "example",
            MetaData(),
            Column("id_", Integer, primary_key=True, autoincrement=True),
            Column("x", Integer),
        )
        ensure_table_created(table, engine)

        sel = select(columnwise_min(table.c.x, table.c.x))
        with engine.begin() as conn:
            _ = conn.execute(sel).all()


class TestCreateEngine:
    @given(temp_path=temp_paths())
    @beartype
    def test_main(self, temp_path: Path) -> None:
        engine = create_engine("sqlite", database=temp_path.name)
        assert isinstance(engine, Engine)


class TestEnsureEngine:
    @given(data=data(), engine=sqlite_engines())
    @beartype
    def test_main(self, data: DataObject, engine: Engine) -> None:
        maybe_engine = data.draw(
            sampled_from([engine, engine.url.render_as_string(hide_password=False)])
        )
        result = ensure_engine(maybe_engine)
        assert result.url == engine.url


class TestEnsureTableCreated:
    @given(engine=sqlite_engines())
    @mark.parametrize("runs", [param(1), param(2)])
    @beartype
    def test_core(self, engine: Engine, runs: int) -> None:
        table = Table("example", MetaData(), Column("id_", Integer, primary_key=True))
        self._run_test(table, engine, runs)

    @given(engine=sqlite_engines())
    @mark.parametrize("runs", [param(1), param(2)])
    @beartype
    def test_orm(self, engine: Engine, runs: int) -> None:
        class Example(declarative_base()):
            __tablename__ = "example"

            id_ = Column(Integer, primary_key=True)

        self._run_test(Example, engine, runs)

    def _run_test(self, table_or_model: Any, engine: Engine, runs: int, /) -> None:
        sel = get_table(table_or_model).select()
        with raises(NoSuchTableError), engine.begin() as conn:
            try:
                _ = conn.execute(sel).all()
            except DatabaseError as error:
                redirect_to_no_such_table_error(engine, error)
        for _ in range(runs):
            ensure_table_created(table_or_model, engine)
        with engine.begin() as conn:
            _ = conn.execute(sel).all()


class TestEnsureTableDropped:
    @given(engine=sqlite_engines())
    @mark.parametrize("runs", [param(1), param(2)])
    @beartype
    def test_core(self, engine: Engine, runs: int) -> None:
        table = Table("example", MetaData(), Column("id_", Integer, primary_key=True))
        self._run_test(table, engine, runs)

    @given(engine=sqlite_engines())
    @mark.parametrize("runs", [param(1), param(2)])
    @beartype
    def test_orm(self, engine: Engine, runs: int) -> None:
        class Example(declarative_base()):
            __tablename__ = "example"

            id_ = Column(Integer, primary_key=True)

        self._run_test(Example, engine, runs)

    def _run_test(self, table_or_model: Any, engine: Engine, runs: int, /) -> None:
        table = get_table(table_or_model)
        sel = table.select()
        with engine.begin() as conn:
            table.create(conn)
            _ = conn.execute(sel).all()
        for _ in range(runs):
            ensure_table_dropped(table_or_model, engine)
        with raises(NoSuchTableError), engine.begin() as conn:
            try:
                _ = conn.execute(sel).all()
            except DatabaseError as error:
                redirect_to_no_such_table_error(engine, error)


class TestGetColumnNames:
    @beartype
    def test_core(self) -> None:
        table = Table("example", MetaData(), Column("id_", Integer, primary_key=True))
        self._run_test(table)

    @beartype
    def test_orm(self) -> None:
        class Example(declarative_base()):
            __tablename__ = "example"

            id_ = Column(Integer, primary_key=True)

        self._run_test(Example)

    @beartype
    def _run_test(self, table_or_model: Any, /) -> None:
        assert get_column_names(table_or_model) == ["id_"]


class TestGetColumns:
    @beartype
    def test_core(self) -> None:
        table = Table("example", MetaData(), Column("id", Integer, primary_key=True))
        self._run_test(table)

    @beartype
    def test_orm(self) -> None:
        class Example(declarative_base()):
            __tablename__ = "example"

            id_ = Column(Integer, primary_key=True)

        self._run_test(Example)

    @beartype
    def _run_test(self, table_or_model: Any, /) -> None:
        columns = get_columns(table_or_model)
        assert isinstance(columns, list)
        assert len(columns) == 1
        assert isinstance(columns[0], Column)


class TestGetDialect:
    @given(engine=sqlite_engines())
    @beartype
    def test_sqlite(self, engine: Engine) -> None:
        assert get_dialect(engine) == "sqlite"

    @mark.parametrize(
        ("url", "expected"),
        [
            param(
                "mssql+pyodbc://scott:tiger@mydsn",
                "mssql",
                marks=mark.skipif(SYSTEM is not System.linux, reason="Linux only"),
            ),
            param(
                "mysql://scott:tiger@localhost/foo",
                "mysql",
                marks=mark.skipif(SYSTEM is not System.linux, reason="Linux only"),
            ),
            param("oracle://scott:tiger@127.0.0.1:1521/sidname", "oracle"),
            param(
                "postgresql://scott:tiger@localhost/mydatabase",
                "postgresql",
                marks=mark.skipif(SYSTEM is not System.linux, reason="Linux only"),
            ),
        ],
    )
    @beartype
    def test_non_sqlite(self, url: str, expected: str) -> None:
        assert get_dialect(_create_engine(url)) == expected


class TestGetTable:
    @beartype
    def test_core(self) -> None:
        table = Table("example", MetaData(), Column("id_", Integer, primary_key=True))
        result = get_table(table)
        assert result is table

    @beartype
    def test_orm(self) -> None:
        class Example(declarative_base()):
            __tablename__ = "example"

            id_ = Column(Integer, primary_key=True)

        table = get_table(Example)
        result = get_table(table)
        assert result is Example.__table__


class TestGetTableName:
    @beartype
    def test_core(self) -> None:
        table = Table("example", MetaData(), Column("id_", Integer, primary_key=True))
        result = get_table_name(table)
        expected = "example"
        assert result == expected

    @beartype
    def test_orm(self) -> None:
        class Example(declarative_base()):
            __tablename__ = "example"

            id_ = Column(Integer, primary_key=True)

        result = get_table_name(Example)
        expected = "example"
        assert result == expected


class TestModelToDict:
    @given(id_=integers())
    @beartype
    def test_main(self, id_: int) -> None:
        class Example(declarative_base()):
            __tablename__ = "example"
            id_ = Column(Integer, primary_key=True)

        example = Example(id_=id_)
        assert model_to_dict(example) == {"id_": id_}

    @given(id_=integers())
    @beartype
    def test_explicitly_named_column(self, id_: int) -> None:
        class Example(declarative_base()):
            __tablename__ = "example"
            ID = Column(Integer, primary_key=True, name="id")

        example = Example(ID=id_)
        assert model_to_dict(example) == {"id": id_}


class TestNextFromSequence:
    @given(engine=sqlite_engines())
    @beartype
    def test_main(self, engine: Engine) -> None:
        with raises(NotImplementedError):
            _ = next_from_sequence("test", engine)

    @given(engine=sqlite_engines())
    @beartype
    def test_limit_within(self, engine: Engine) -> None:
        with raises(NotImplementedError):
            _ = next_from_sequence("test", engine, timeout=1.0)

    @given(engine=sqlite_engines())
    @beartype
    def test_limit_breached(self, engine: Engine) -> None:
        result = next_from_sequence("test", engine, timeout=1e-9)
        assert result is None


class TestParseEngine:
    @given(engine=sqlite_engines())
    @beartype
    def test_str(self, engine: Engine) -> None:
        url = engine.url
        result = parse_engine(url.render_as_string(hide_password=False))
        assert result.url == url

    @beartype
    def test_error(self) -> None:
        with raises(ParseEngineError):
            _ = parse_engine("error")


class TestRedirectToNoSuchSequenceError:
    @given(engine=sqlite_engines())
    @beartype
    def test_main(self, engine: Engine) -> None:
        seq = Sequence("example")
        with raises(NotImplementedError), engine.begin() as conn:
            _ = conn.scalar(seq)


class TestRedirectToNoSuchTableError:
    @given(engine=sqlite_engines())
    @beartype
    def test_main(self, engine: Engine) -> None:
        table = Table("example", MetaData(), Column("id", Integer, primary_key=True))
        with raises(NoSuchTableError), engine.begin() as conn:
            try:
                _ = conn.execute(select(table))
            except DatabaseError as error:
                redirect_to_no_such_table_error(engine, error)


class TestRedirectTableAlreadyExistsError:
    @given(engine=sqlite_engines())
    @beartype
    def test_main(self, engine: Engine) -> None:
        table = Table("example", MetaData(), Column("id", Integer, primary_key=True))
        with engine.begin() as conn:
            _ = table.create(conn)
        with raises(TableAlreadyExistsError), engine.begin() as conn:
            try:
                _ = table.create(conn)
            except DatabaseError as error:
                redirect_to_table_already_exists_error(engine, error)


class TestReflectTable:
    @given(
        engine=sqlite_engines(),
        col_type=sampled_from(
            [
                INTEGER,
                INTEGER(),
                NVARCHAR,
                NVARCHAR(),
                NVARCHAR(1),
                Integer,
                Integer(),
                String,
                String(),
                String(1),
            ]
        ),
    )
    @beartype
    def test_reflected(self, engine: Engine, col_type: Any) -> None:
        table = Table("example", MetaData(), Column("Id", col_type, primary_key=True))
        ensure_table_created(table, engine)
        reflected = _reflect_table(table, engine)
        check_tables_equal(reflected, table)

    @given(engine=sqlite_engines())
    @beartype
    def test_no_such_table(self, engine: Engine) -> None:
        table = Table("example", MetaData(), Column("Id", Integer, primary_key=True))
        with raises(NoSuchTableError):
            _ = _reflect_table(table, engine)


class TestSerializeEngine:
    @given(data=data())
    @beartype
    def test_main(self, data: DataObject) -> None:
        engine = data.draw(sqlite_engines())
        result = parse_engine(serialize_engine(engine))
        assert result.url == engine.url


class TestTablenameMixin:
    @beartype
    def test_main(self) -> None:
        class Example(declarative_base(cls=TablenameMixin)):
            Id = Column(Integer, primary_key=True)

        assert get_table_name(Example) == "example"


class TestYieldConnection:
    @given(engine=sqlite_engines())
    @beartype
    def test_engine(self, engine: Engine) -> None:
        with yield_connection(engine) as conn:
            assert isinstance(conn, Connection)

    @given(engine=sqlite_engines())
    @beartype
    def test_connection(self, engine: Engine) -> None:
        with engine.begin() as conn1, yield_connection(conn1) as conn2:
            assert isinstance(conn2, Connection)


class TestYieldInClauseRows:
    @given(data=data(), engine=sqlite_engines(), chunk_size=integers(1, 10) | none())
    @beartype
    def test_main(
        self, data: DataObject, engine: Engine, chunk_size: Optional[int]
    ) -> None:
        table = Table("example", MetaData(), Column("id", Integer, primary_key=True))
        rows = data.draw(table_records_lists(table, min_size=1))
        num_rows = len(rows)
        with engine.begin() as conn:
            table.create(conn)
            _ = conn.execute(insert(table).values(rows))
            assert (
                conn.execute(select(func.count()).select_from(table)).scalar()
                == num_rows
            )
        row_vals = [row[0] for row in rows]
        values = data.draw(sets(sampled_from(row_vals)))
        result = list(
            yield_in_clause_rows(
                select(table.c.id), table.c.id, values, engine, chunk_size=chunk_size
            )
        )
        assert len(result) == len(values)
