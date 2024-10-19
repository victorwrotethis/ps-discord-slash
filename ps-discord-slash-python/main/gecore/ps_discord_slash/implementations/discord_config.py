from enum import IntEnum
import os


class GenericConfig:
    APP_ID = 789525379047358464  # os.environ.get('application_id')
    JAEGER_EVENTS_GUILD = 207168033918025729  # os.environ.get('jaeger_events_guild')
    TEST_GUILD = 621502053373706241
    NO_FUN = 282944414127489032
    DB_URL = 'http://localhost:8000'  # os.environ.get('db_url')

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self


class JaegerEventRoles(IntEnum):
    PSB_ADMIN = 332587654111821827
    PICKUPS_ADMIN = 703422762386980895
    ARMOR_PICKUPS_STAFF = 779188829080780801
    POG_ADMIN = 739632481698840648
    OVO_STAFF = 333398154739187722
    PIL_STAFF = 702573421044826162
    PSB_SENIOR_STAFF = 703435761596366940
    JAEGER_FLIPPER = 332590290944655371
    OVO_REP = 298828610590998528
    COMMUNITY_REP = 845489451781849148
    LS_CAPTAIN = 476408783787261962
    LS_REP = 772270365745086464
    NAMED_USER = 333060137919184896
    PRAC_REP = 694400853850849310
    PIL_CAPTAIN = 702306785729445941
    LS_ORGANIZER = 703423270011142212
    LS_REF = 714220457821470791
    FAKE_ROLE = 1321241245
    EXTRA_FAKE_ROLE = 2352345
    HAVE_I_ADDED_FAKE_ROLES_YET = 23352345
    EDWARDIAN = 954028692387016734

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self.value


class NoFunRoles(IntEnum):
    ROLL_CALLER = 1175621424187179098


class NoFunChannel(IntEnum):
    ROLL_CALL = 601397426934251520
    ROLL_CALL_BOT = 1082033236789702676


class JaegerEventChannel(IntEnum):
    SLASH_SPAM = 790298629721554974
    OVO_BOT_DEV = 738473349042274324
    OVO_BASES_TEST = 954091556116242482

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self.value
