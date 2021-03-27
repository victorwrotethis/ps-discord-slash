from enum import IntEnum
import os


class GenericConfig:
    APP_ID = 789525379047358464  # os.environ.get('application_id')
    JAEGER_EVENTS_GUILD = 207168033918025729  # os.environ.get('jaeger_events_guild')
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

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self.value


class JaegerEventChannel(IntEnum):
    SLASH_SPAM = 790298629721554974
    OVO_BOT_DEV = 738473349042274324

    def __getstate__(self):
        """Allows JsonPickle just to retrieve the value"""
        return self.value
