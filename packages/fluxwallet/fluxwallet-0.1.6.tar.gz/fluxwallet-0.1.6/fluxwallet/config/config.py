# -*- coding: utf-8 -*-
#
#    fluxwallet - Python Cryptocurrency Library
#    CONFIG - Configuration settings
#    © 2022 October - 1200 Web Development <http://1200wd.com/>
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

import configparser
import enum
import locale
import os
import platform
from datetime import datetime
from pathlib import Path

# General defaults
TYPE_TEXT = str
TYPE_INT = int
LOGLEVEL = "DEBUG"


# File locations
FW_CONFIG_FILE = ""
FW_INSTALL_DIR = Path(__file__).parents[1]
FW_DATA_DIR = ""
FW_DATABASE_DIR = ""
DEFAULT_DATABASE = None
DEFAULT_DATABASE_CACHE = None
FW_LOG_FILE = ""

# Main
ENABLE_fluxwallet_LOGGING = True
ALLOW_DATABASE_THREADS = None

# Services
TIMEOUT_REQUESTS = 5
# MAX_TRANSACTIONS = 20
MAX_TRANSACTIONS = 20000
BLOCK_COUNT_CACHE_TIME = 3
SERVICE_MAX_ERRORS = 3  # Fail service request when more then max errors occur for <SERVICE_MAX_ERRORS> providers

# Transactions
SCRIPT_TYPES_LOCKING = {
    # Locking scripts / scriptPubKey (Output)
    "p2pkh": ["OP_DUP", "OP_HASH160", "hash-20", "OP_EQUALVERIFY", "OP_CHECKSIG"],
    "p2sh": ["OP_HASH160", "hash-20", "OP_EQUAL"],
    "p2wpkh": ["OP_0", "hash-20"],
    "p2wsh": ["OP_0", "hash-32"],
    "p2tr": ["op_n", "hash-32"],
    "multisig": ["op_m", "multisig", "op_n", "OP_CHECKMULTISIG"],
    "p2pk": ["public_key", "OP_CHECKSIG"],
    "nulldata": ["OP_RETURN", "return_data"],
}

SCRIPT_TYPES_UNLOCKING = {
    # Unlocking scripts / scriptSig (Input)
    "sig_pubkey": ["signature", "SIGHASH_ALL", "public_key"],
    "p2sh_multisig": ["OP_0", "multisig", "redeemscript"],
    "p2sh_p2wpkh": ["OP_0", "OP_HASH160", "redeemscript", "OP_EQUAL"],
    "p2sh_p2wsh": ["OP_0", "push_size", "redeemscript"],
    "locktime_cltv": ["locktime_cltv", "OP_CHECKLOCKTIMEVERIFY", "OP_DROP"],
    "locktime_csv": ["locktime_csv", "OP_CHECKSEQUENCEVERIFY", "OP_DROP"],
    "signature": ["signature"],
}

SIGHASH_ALL = 1
SIGHASH_NONE = 2
SIGHASH_SINGLE = 3
SIGHASH_ANYONECANPAY = 80

SEQUENCE_LOCKTIME_DISABLE_FLAG = 1 << 31  # To enable sequence time locks
SEQUENCE_LOCKTIME_TYPE_FLAG = (
    1 << 22
)  # If set use timestamp based lock otherwise use block height
SEQUENCE_LOCKTIME_GRANULARITY = 9
SEQUENCE_LOCKTIME_MASK = 0x0000FFFF
SEQUENCE_ENABLE_LOCKTIME = 0xFFFFFFFE
SEQUENCE_REPLACE_BY_FEE = 0xFFFFFFFD

SIGNATURE_VERSION_STANDARD = 0
SIGNATURE_VERSION_SEGWIT = 1

# Mnemonics
DEFAULT_LANGUAGE = "english"

# Networks
DEFAULT_NETWORK = "bitcoin"
NETWORK_DENOMINATORS = {  # source: https://en.bitcoin.it/wiki/Units, https://en.wikipedia.org/wiki/Metric_prefix
    0.00000000000001: "µsat",
    0.00000000001: "msat",
    0.000000001: "n",
    0.00000001: "sat",
    0.0000001: "fin",
    0.000001: "µ",
    0.001: "m",
    0.01: "c",
    0.1: "d",
    1: "",
    10: "da",
    100: "h",
    1000: "k",
    1000000: "M",
    1000000000: "G",
    1000000000000: "T",
    1000000000000000: "P",
    1000000000000000000: "E",
    1000000000000000000000: "Z",
    1000000000000000000000000: "Y",
}

if os.name == "nt" and locale.getpreferredencoding() != "UTF-8":
    # TODO: Find a better windows hack
    import _locale

    _locale._getdefaultlocale = lambda *args: ["en_US", "utf8"]
elif locale.getpreferredencoding() != "UTF-8":
    raise EnvironmentError(
        "Locale is currently set to '%s'. "
        "This library needs the locale set to UTF-8 to function properly"
        % locale.getpreferredencoding()
    )

# Keys / Addresses
SUPPORTED_ADDRESS_ENCODINGS = ["base58", "bech32"]
ENCODING_BECH32_PREFIXES = ["bc", "tb", "ltc", "tltc", "tdash", "tdash", "blt"]
DEFAULT_WITNESS_TYPE = "legacy"
BECH32M_CONST = 0x2BC830A3

# Wallets
WALLET_KEY_STRUCTURES = [
    {
        "purpose": None,
        "script_type": "p2pkh",
        "witness_type": "legacy",
        "multisig": False,
        "encoding": "base58",
        "description": "Single key wallet with no hierarchical deterministic key structure",
        "key_path": ["m"],
    },
    {
        "purpose": 44,
        "script_type": "p2pkh",
        "witness_type": "legacy",
        "multisig": False,
        "encoding": "base58",
        "description": "Legacy wallet using pay-to-public-key-hash scripts",
        "key_path": [
            "m",
            "purpose'",
            "coin_type'",
            "account'",
            "change",
            "address_index",
        ],
    },
    {
        "purpose": 45,
        "script_type": "p2sh",
        "witness_type": "legacy",
        "multisig": True,
        "encoding": "base58",
        "description": "Legacy multisig wallet using pay-to-script-hash scripts",
        "key_path": ["m", "purpose'", "cosigner_index", "change", "address_index"],
    },
    {
        "purpose": 48,
        "script_type": "p2sh-p2wsh",
        "witness_type": "p2sh-segwit",
        "multisig": True,
        "encoding": "base58",
        "description": "Segwit multisig wallet using pay-to-wallet-script-hash scripts nested in p2sh scripts",
        "key_path": [
            "m",
            "purpose'",
            "coin_type'",
            "account'",
            "script_type'",
            "change",
            "address_index",
        ],
    },
    {
        "purpose": 48,
        "script_type": "p2wsh",
        "witness_type": "segwit",
        "multisig": True,
        "encoding": "bech32",
        "description": "Segwit multisig wallet using native segwit pay-to-wallet-script-hash scripts",
        "key_path": [
            "m",
            "purpose'",
            "coin_type'",
            "account'",
            "script_type'",
            "change",
            "address_index",
        ],
    },
    {
        "purpose": 49,
        "script_type": "p2sh-p2wpkh",
        "witness_type": "p2sh-segwit",
        "multisig": False,
        "encoding": "base58",
        "description": "Segwit wallet using pay-to-wallet-public-key-hash scripts nested in p2sh scripts",
        "key_path": [
            "m",
            "purpose'",
            "coin_type'",
            "account'",
            "change",
            "address_index",
        ],
    },
    {
        "purpose": 84,
        "script_type": "p2wpkh",
        "witness_type": "segwit",
        "multisig": False,
        "encoding": "bech32",
        "description": "Segwit multisig wallet using native segwit pay-to-wallet-public-key-hash scripts",
        "key_path": [
            "m",
            "purpose'",
            "coin_type'",
            "account'",
            "change",
            "address_index",
        ],
    },
    # {
    #     'purpose': 86,
    #     'script_type': 'p2tr',
    #     'witness_type': 'segwit',
    #     'multisig': False,
    #     'encoding': 'bech32',
    #     'description': 'Taproot single key wallet using P2TR transactions',
    #     'key_path': ["m", "purpose'", "coin_type'", "account'", "change", "address_index"]
    # },
]

# UNITTESTS
UNITTESTS_FULL_DATABASE_TEST = False

# CACHING
SERVICE_CACHING_ENABLED = True


def read_config():
    config = configparser.ConfigParser()

    def config_get(section, var, fallback, is_boolean=False):
        try:
            if is_boolean:
                val = config.getboolean(section, var, fallback=fallback)
            else:
                val = config.get(section, var, fallback=fallback)
            return val
        except Exception:
            return fallback

    global FW_INSTALL_DIR, FW_DATABASE_DIR, DEFAULT_DATABASE, FW_DATA_DIR, FW_CONFIG_FILE
    global ALLOW_DATABASE_THREADS, DEFAULT_DATABASE_CACHE
    global FW_LOG_FILE, LOGLEVEL, ENABLE_fluxwallet_LOGGING
    global TIMEOUT_REQUESTS, DEFAULT_LANGUAGE, DEFAULT_NETWORK, DEFAULT_WITNESS_TYPE
    global UNITTESTS_FULL_DATABASE_TEST, SERVICE_CACHING_ENABLED
    global SERVICE_MAX_ERRORS, BLOCK_COUNT_CACHE_TIME, MAX_TRANSACTIONS

    # Read settings from Configuration file provided in OS environment~/.fluxwallet/ directory
    config_file_name = os.environ.get("FW_CONFIG_FILE")
    if not config_file_name:
        FW_CONFIG_FILE = Path("~/.fluxwallet/config.ini").expanduser()
    else:
        FW_CONFIG_FILE = Path(config_file_name)
        if not FW_CONFIG_FILE.is_absolute():
            FW_CONFIG_FILE = Path(Path.home(), ".fluxwallet", FW_CONFIG_FILE)
        if not FW_CONFIG_FILE.exists():
            FW_CONFIG_FILE = Path(FW_INSTALL_DIR, "data", config_file_name)
        if not FW_CONFIG_FILE.exists():
            raise IOError(
                "fluxwallet configuration file not found: %s" % str(FW_CONFIG_FILE)
            )
    data = config.read(str(FW_CONFIG_FILE))
    FW_DATA_DIR = Path(
        config_get("locations", "data_dir", fallback="~/.fluxwallet")
    ).expanduser()
    # Database settings
    FW_DATABASE_DIR = Path(
        FW_DATA_DIR, config_get("locations", "database_dir", "database")
    )
    FW_DATABASE_DIR.mkdir(parents=True, exist_ok=True)
    default_databasefile = DEFAULT_DATABASE = config_get(
        "locations", "default_databasefile", fallback="fluxwallet.sqlite"
    )
    if not default_databasefile.startswith(
        "postgresql"
    ) or default_databasefile.startswith("mysql"):
        DEFAULT_DATABASE = str(Path(FW_DATABASE_DIR, default_databasefile))
    default_databasefile_cache = DEFAULT_DATABASE_CACHE = config_get(
        "locations", "default_databasefile_cache", fallback="fluxwallet_cache.sqlite"
    )
    if not default_databasefile_cache.startswith(
        "postgresql"
    ) or default_databasefile_cache.startswith("mysql"):
        DEFAULT_DATABASE_CACHE = str(Path(FW_DATABASE_DIR, default_databasefile_cache))
    ALLOW_DATABASE_THREADS = config_get(
        "common", "allow_database_threads", fallback=True, is_boolean=True
    )
    SERVICE_CACHING_ENABLED = config_get(
        "common", "service_caching_enabled", fallback=True, is_boolean=True
    )

    # Log settings
    ENABLE_fluxwallet_LOGGING = config_get(
        "logs", "enable_fluxwallet_logging", fallback=True, is_boolean=True
    )
    FW_LOG_FILE = Path(
        FW_DATA_DIR, config_get("logs", "log_file", fallback="fluxwallet.log")
    )
    FW_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    LOGLEVEL = config_get("logs", "loglevel", fallback=LOGLEVEL)

    # Service settings
    TIMEOUT_REQUESTS = int(
        config_get("common", "timeout_requests", fallback=TIMEOUT_REQUESTS)
    )
    SERVICE_MAX_ERRORS = int(
        config_get("common", "service_max_errors", fallback=SERVICE_MAX_ERRORS)
    )
    MAX_TRANSACTIONS = int(
        config_get("common", "max_transactions", fallback=MAX_TRANSACTIONS)
    )
    BLOCK_COUNT_CACHE_TIME = int(
        config_get("common", "block_count_cache_time", fallback=BLOCK_COUNT_CACHE_TIME)
    )

    # Other settings
    DEFAULT_LANGUAGE = config_get(
        "common", "default_language", fallback=DEFAULT_LANGUAGE
    )
    DEFAULT_NETWORK = config_get("common", "default_network", fallback=DEFAULT_NETWORK)
    DEFAULT_WITNESS_TYPE = config_get(
        "common", "default_witness_type", fallback=DEFAULT_WITNESS_TYPE
    )

    full_db_test = os.environ.get("UNITTESTS_FULL_DATABASE_TEST")
    if full_db_test:
        if full_db_test in [1, True, "True", "true", "TRUE"]:
            UNITTESTS_FULL_DATABASE_TEST = True

    if not data:
        return False
    return True


# Copy data and settings to default settings directory if install.log is not found
def initialize_lib():
    global FW_INSTALL_DIR, FW_DATA_DIR, FLUXWALLET_VERSION
    instlogfile = Path(FW_DATA_DIR, "install.log")
    if instlogfile.exists():
        return

    with instlogfile.open("w") as f:
        install_message = (
            "fluxwallet installed, check further logs in fluxwallet.log\n\n"
            "If you remove this file all settings will be reset again to the default settings. "
            "This might be usefull after an update or when problems occur.\n\n"
            "Installation parameters. Include this parameters when reporting bugs and issues:\n"
            "fluxwallet version: %s\n"
            "Installation date : %s\n"
            "Python            : %s\n"
            "Compiler          : %s\n"
            "Build             : %s\n"
            "OS Version        : %s\n"
            "Platform          : %s\n"
            % (
                FLUXWALLET_VERSION,
                datetime.now().isoformat(),
                platform.python_version(),
                platform.python_compiler(),
                platform.python_build(),
                platform.version(),
                platform.platform(),
            )
        )
        f.write(install_message)

    # Copy data and settings file
    from shutil import copyfile

    for file in Path(FW_INSTALL_DIR, "data").iterdir():
        if file.suffix not in [".ini", ".json"]:
            continue
        copyfile(str(file), Path(FW_DATA_DIR, file.name))


# Initialize library
read_config()

with open(Path(FW_INSTALL_DIR, "config/VERSION"), "r") as f:
    FLUXWALLET_VERSION = f.read().strip()

initialize_lib()
