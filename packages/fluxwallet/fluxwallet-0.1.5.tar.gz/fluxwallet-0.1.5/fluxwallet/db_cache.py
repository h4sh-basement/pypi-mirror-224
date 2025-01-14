# -*- coding: utf-8 -*-
#
#    fluxwallet - Python Cryptocurrency Library
#    Cache DataBase - SqlAlchemy database definitions for caching
#    © 2020 February - 1200 Web Development <http://1200wd.com/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# try:
#     import mysql.connector
#     from parameterized import parameterized_class
#     import psycopg2
#     from psycopg2 import sql
#     from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# except ImportError as e:
#     print("Could not import all modules. Error: %s" % e)
#     # from psycopg2cffi import compat  # Use for PyPy support
#     # compat.register()
#     pass  # Only necessary when mysql or postgres is used
from __future__ import annotations

from urllib.parse import urlparse

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    LargeBinary,
    String,
    text,
)
from sqlalchemy.event import listen
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.ext.asyncio.engine import AsyncEngine

# from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    WriteOnlyMapped,
    mapped_column,
    relationship,
)

from fluxwallet.main import *

# _logger = logging.getLogger(__name__)


class WitnessTypeTransactions(enum.Enum):
    legacy = "legacy"
    segwit = "segwit"


class Base(AsyncAttrs, DeclarativeBase):
    pass


class DbCache:
    """
    Cache Database object. Initialize database and open session when creating database object.

    Create new database if is doesn't exist yet

    """

    _built = False

    @classmethod
    async def start(cls, db_uri: str | None = None) -> DbCache:
        self = DbCache()

        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        await self.test_connection()
        DbCache._built = True

        return self

    async def __aenter__(self) -> AsyncSession:
        if not DbCache._built:
            async with self.engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)

            await self.test_connection()
            DbCache._built = True

        return self._session

    async def __aexit__(self, exception_type, exception_value, exception_traceback):
        # await self._session.close()
        # return None / False will reraise
        # print("Exiting DbCache Context")
        ...

    def __init__(
        self,
        db_uri: str | None = None,
        *,
        sessionmaker: async_sessionmaker | None = None,
    ):
        if db_uri is None:
            db_uri = DEFAULT_DATABASE_CACHE

        db_uri = f"sqlite+aiosqlite:///{db_uri}"

        self.connection_possible = False
        self.engine = create_async_engine(db_uri, isolation_level="READ UNCOMMITTED")
        self.sessionmaker = async_sessionmaker(self.engine, expire_on_commit=False)

        listen(self.engine.sync_engine, "connect", self.set_sqlite_pragma)
        self.db_uri = db_uri
        self._session = self.sessionmaker()

    def get_session(self):
        return self.sessionmaker()

    def set_sqlite_pragma(self, dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.close()

        # print("Cache Engine connected")

    async def test_connection(self) -> None:
        async with self.get_session() as session:
            try:
                await session.execute(text("SELECT 1"))
                self.connection_possible = True
            except Exception:
                self.connection_possible = False

    @property
    def session(self) -> AsyncSession:
        return self._session

    # def drop_db(self):
    #     self.session.commit()
    #     # self.session.close_all()
    #     close_all_sessions()
    #     Base.metadata.drop_all(self.engine)


class DbCacheTransactionNode(Base):
    """
    Link table for cache transactions and addresses
    """

    __tablename__ = "cache_transactions_node"
    txid = Column(
        LargeBinary(32), ForeignKey("cache_transactions.txid"), primary_key=True
    )
    transaction = relationship(
        "DbCacheTransaction", back_populates="nodes", doc="Related transaction object"
    )
    index_n = Column(
        Integer, primary_key=True, doc="Order of input/output in this transaction"
    )
    value = Column(BigInteger, default=0, doc="Value of transaction input")
    address = Column(
        String(255), index=True, doc="Address string base32 or base58 encoded"
    )
    script = Column(LargeBinary, doc="Locking or unlocking script")
    witnesses = Column(
        LargeBinary, doc="Witnesses (signatures) used in Segwit transaction inputs"
    )
    sequence = Column(
        BigInteger,
        default=0xFFFFFFFF,
        doc="Transaction sequence number. Used for timelock transaction inputs",
    )
    is_input = Column(Boolean, primary_key=True, doc="True if input, False if output")
    spent = Column(Boolean, default=None, doc="Is output spent?")
    ref_txid = Column(
        LargeBinary(32),
        index=True,
        doc="Transaction hash of input which spends this output",
    )
    ref_index_n = Column(
        BigInteger, doc="Index number of transaction input which spends this output"
    )

    def prev_txid(self):
        if self.is_input:
            return self.ref_txid

    def output_n(self):
        if self.is_input:
            return self.ref_index_n

    def spending_txid(self):
        if not self.is_input:
            return self.ref_txid

    def spending_index_n(self):
        if not self.is_input:
            return self.ref_index_n


class DbCacheTransaction(Base):
    """
    Transaction Cache Table

    Database which stores transactions received from service providers as cache

    """

    __tablename__ = "cache_transactions"
    txid = Column(
        LargeBinary(32),
        primary_key=True,
        doc="Hexadecimal representation of transaction hash or transaction ID",
    )
    date = Column(
        DateTime, doc="Date when transaction was confirmed and included in a block"
    )
    version = Column(
        BigInteger,
        default=1,
        doc="Tranaction version. Default is 1 but some wallets use another version number",
    )
    locktime = Column(
        BigInteger,
        default=0,
        doc="Transaction level locktime. Locks the transaction until a specified block "
        "(value from 1 to 5 million) or until a certain time (Timestamp in seconds after 1-jan-1970)."
        " Default value is 0 for transactions without locktime",
    )
    expiry_height = Column(
        Integer,
        default=0,
        doc="Expiry height (in blocktime) for this transactions. I.e, must be confirmed before this block height."
        "Default is 0: no expiry (not version 4 transaction)",
    )
    confirmations = Column(
        Integer,
        default=0,
        doc="Number of confirmation when this transaction is included in a block. "
        "Default is 0: unconfirmed",
    )
    block_height = Column(
        Integer, index=True, doc="Height of block this transaction is included in"
    )
    network_name = Column(String(20), doc="Blockchain network name of this transaction")
    fee = Column(BigInteger, doc="Transaction fee")
    nodes = relationship(
        "DbCacheTransactionNode",
        cascade="all,delete",
        doc="List of all inputs and outputs as DbCacheTransactionNode objects",
    )
    order_n = Column(Integer, doc="Order of transaction in block")
    witness_type = Column(
        Enum(WitnessTypeTransactions),
        default=WitnessTypeTransactions.legacy,
        doc="Transaction type enum: legacy or segwit",
    )


class DbCacheAddress(Base):
    """
    Address Cache Table

    Stores transactions and unspent outputs (UTXO's) per address

    """

    __tablename__ = "cache_address"
    address = Column(
        String(255), primary_key=True, doc="Address string base32 or base58 encoded"
    )
    network_name = Column(String(20), doc="Blockchain network name of this transaction")
    balance = Column(
        BigInteger, default=0, doc="Total balance of UTXO's linked to this key"
    )
    last_block = Column(Integer, doc="Number of last updated block")
    last_txid = Column(
        LargeBinary(32), doc="Transaction ID of latest transaction in cache"
    )
    last_tx_index = Column(
        Integer, doc="Transaction index of latest transaction in cache"
    )
    n_utxos = Column(Integer, doc="Total number of UTXO's for this address")
    n_txs = Column(Integer, doc="Total number of transactions for this address")


class DbCacheBlock(Base):
    """
    Block Cache Table

    Stores block headers
    """

    __tablename__ = "cache_blocks"
    height = Column(
        Integer, primary_key=True, doc="Height or sequence number for this block"
    )
    block_hash = Column(LargeBinary(32), index=True, doc="Hash of this block")
    network_name = Column(String(20), doc="Blockchain network name")
    version = Column(
        BigInteger, doc="Block version to specify which features are used (hex)"
    )
    prev_block = Column(LargeBinary(32), doc="Block hash of previous block")
    merkle_root = Column(
        LargeBinary(32), doc="Merkle root used to validate transaction in block"
    )
    time = Column(BigInteger, doc="Timestamp to indicated when block was created")
    bits = Column(
        BigInteger,
        doc="Encoding for proof-of-work, used to determine target and difficulty",
    )
    nonce = Column(
        BigInteger,
        doc="Nonce (number used only once or n-once) is used to create different block hashes",
    )
    tx_count = Column(Integer, doc="Number of transactions included in this block")


class DbCacheVars(Base):
    """
    Table to store various blockchain related variables
    """

    __tablename__ = "cache_variables"
    varname = Column(String(50), primary_key=True, doc="Variable unique name")
    network_name = Column(
        String(20), primary_key=True, doc="Blockchain network name of this transaction"
    )
    value = Column(String(255), doc="Value of variable")
    type = Column(String(20), doc="Type of variable: int, string or float")
    expires = Column(DateTime, doc="Datetime value when variable expires")
