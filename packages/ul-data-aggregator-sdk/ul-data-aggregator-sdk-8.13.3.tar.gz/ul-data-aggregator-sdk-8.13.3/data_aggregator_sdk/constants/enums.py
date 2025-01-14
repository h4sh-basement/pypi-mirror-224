from enum import Enum, unique


class NetworkTypeEnum(Enum):
    """
    Enumeration of network types
    """
    input = "input"
    output = "output"

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class DeviceModificationTypeEnum(Enum):
    """
    Enumeration of modification types for devices
    """
    smart_meter = "smart_meter"
    modem = "modem"

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class NetworkSysTypeEnum(Enum):  # TODO: move to reception sdk
    """
    Enumeration of system types for application networks
    """
    OUTPUT_OLD_LK = "OUTPUT_OLD_LK"
    OUTPUT_NEW_LK = "OUTPUT_NEW_LK"
    OUTPUT_DATA_LOGGER_DEVICE_DATA = "OUTPUT_DATA_LOGGER_DEVICE_DATA"
    OUTPUT_DATA_AGGREGATOR_DEVICE_DATA = "OUTPUT_DATA_AGGREGATOR_DEVICE_DATA"
    INPUT_NBIOT = "INPUT_NBIOT"
    INPUT_LORA = "INPUT_LORA"
    INPUT_KAFKA_BS0 = "INPUT_KAFKA_BS0"
    INPUT_HTTP_BS = "INPUT_HTTP_BS"
    INPUT_NEW_LK = "INPUT_NEW_LK"
    INPUT_EXTERNAL_API = "INPUT_EXTERNAL_API"
    INPUT_UNIVERSAL_API = "INPUT_UNIVERSAL_API"

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class ProtocolEnum(Enum):
    """
    Enumeration of protocols for packets
    """
    WATER5_V_NERO_V0 = 'WATER5_V_NERO_V0'
    NCP_SMP_V0 = 'NCP_SMP_V0'
    SMP_V0 = 'SMP_V0'
    SMP_M_GAS_METER_V0 = 'SMP_M_GAS_METER_V0'
    SMP_M_ENERGY_METER_V0 = 'SMP_M_ENERGY_METER_V0'
    SMP_M_JUPITER_08B_V0 = 'SMP_M_JUPITER_08B_V0'
    SMP_M_JUPITER_12B_V0 = 'SMP_M_JUPITER_12B_V0'
    SMP_M_JUPITER_16B_V0 = 'SMP_M_JUPITER_16B_V0'
    SMP_M_WATER_METER_04B_V0 = 'SMP_M_WATER_METER_04B_V0'
    SMP_M_WATER_METER_08B_V0 = 'SMP_M_WATER_METER_08B_V0'
    SMP_M_WATER_METER_12B_V0 = 'SMP_M_WATER_METER_12B_V0'
    SMP_M_WATER_METER_16B_V0 = 'SMP_M_WATER_METER_16B_V0'
    SMP_M_HEAT_PROXY_METER_16B_V0 = 'SMP_M_HEAT_PROXY_METER_16B_V0'
    SMP_M_HEAT_GROUP_METER_V0 = 'SMP_M_HEAT_GROUP_METER_V0'
    WATER5_V_JUPITER_FREESCALE_V0 = 'WATER5_V_JUPITER_FREESCALE_V0'
    WATER5_V_JUPITER_STM_V0 = 'WATER5_V_JUPITER_STM_V0'
    WATER5_V_FLUO_STM_V0 = 'WATER5_V_FLUO_STM_V0'
    WATER5_V_FLUO_FREESCALE_V0 = 'WATER5_V_FLUO_FREESCALE_V0'
    WATER5_V_FLUO_A_V0 = 'WATER5_V_FLUO_A_V0'
    WATER5_V_FLUO_S_V0 = 'WATER5_V_FLUO_S_V0'
    WATER5_V_GAS_V0 = 'WATER5_V_GAS_V0'
    WATER5_V_JUPITER_LORA_V0 = 'WATER5_V_JUPITER_LORA_V0'
    WATER5_V_FLUO_LORA_V0 = 'WATER5_V_FLUO_LORA_V0'
    SMP_M_INTERNAL_INFO_DATA = 'SMP_M_INTERNAL_INFO_DATA'
    ARVAS_API_V0 = 'ARVAS_API_V0'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class IntegrationV0MessageErrorType(Enum):
    """
    Enumeration of error types
    """
    none = 'none'
    device_unidentified = 'device_unidentified'
    data_undecryptable = 'data_undecryptable'
    data_unparsable = 'data_unparsable'
    mac_duplicated = 'mac_duplicated'
    packet_from_the_future = 'packet_from_the_future'
    packet_from_the_past = 'packet_from_the_past'
    error_unidentified = 'error_unidentified'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class EncryptionType(Enum):  # DO NOT CHANGE, DEPENDENCY BY RECEPTION INTERFACE!!!!!!!
    """
    Enumeration of encryption types
    """
    NO_ENCRYPTION = 'NO_ENCRYPTION'
    XTEA_V_NERO_V0 = 'XTEA_V_NERO_V0'
    AES_ECB_V_NERO_V0 = 'AES_ECB_V_NERO_V0'
    KUZNECHIK_V_NERO_V0 = 'KUZNECHIK_V_NERO_V0'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class ResourceKind(Enum):
    """
    Enumeration of resource kinds for devices
    """
    COMMON_CONSUMED = 'COMMON_CONSUMED'
    COMMON_GENERATED = 'COMMON_GENERATED'
    COMMON_ACTIVE_GENERATED = 'COMMON_ACTIVE_GENERATED'
    COMMON_ACTIVE_CONSUMED = 'COMMON_ACTIVE_CONSUMED'
    COMMON_REACTIVE_GENERATED = 'COMMON_REACTIVE_GENERATED'
    COMMON_REACTIVE_CONSUMED = 'COMMON_REACTIVE_CONSUMED'
    PHASE_A_ACTIVE_CONSUMED = 'PHASE_A_ACTIVE_CONSUMED'
    PHASE_A_ACTIVE_GENERATED = 'PHASE_A_ACTIVE_GENERATED'
    PHASE_A_REACTIVE_CONSUMED = 'PHASE_A_REACTIVE_CONSUMED'
    PHASE_A_REACTIVE_GENERATED = 'PHASE_A_REACTIVE_GENERATED'
    PHASE_B_ACTIVE_CONSUMED = 'PHASE_B_ACTIVE_CONSUMED'
    PHASE_B_ACTIVE_GENERATED = 'PHASE_B_ACTIVE_GENERATED'
    PHASE_B_REACTIVE_CONSUMED = 'PHASE_B_REACTIVE_CONSUMED'
    PHASE_B_REACTIVE_GENERATED = 'PHASE_B_REACTIVE_GENERATED'
    PHASE_C_ACTIVE_CONSUMED = 'PHASE_C_ACTIVE_CONSUMED'
    PHASE_C_ACTIVE_GENERATED = 'PHASE_C_ACTIVE_GENERATED'
    PHASE_C_REACTIVE_CONSUMED = 'PHASE_C_REACTIVE_CONSUMED'
    PHASE_C_REACTIVE_GENERATED = 'PHASE_C_REACTIVE_GENERATED'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class DeviceValueMarker(Enum):
    """
    Enumeration of markers for device values
    """
    NO_DOUBT = 'NO_DOUBT'
    OVERFLOW = 'OVERFLOW'
    OVERFLOW_SUSPICIOUS = 'OVERFLOW_SUSPICIOUS'
    NOT_CHECKED = 'NOT_CHECKED'
    REJECTED_OVERFLOW = 'REJECTED_OVERFLOW'
    REJECTED_VALUE = 'REJECTED_VALUE'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


@unique
class IntegrationV0MessageEvent(Enum):
    """
    Enumeration of events for devices
    """
    BATTERY_IS_LOW = 'BATTERY_IS_LOW'
    MAGNET_WAS_DETECTED = 'MAGNET_WAS_DETECTED'
    CASE_WAS_OPENED = 'CASE_WAS_OPENED'
    TEMPERATURE_LIMIT = 'TEMPERATURE_LIMIT'
    OTHER = 'OTHER'
    SYS_NO_DATA = 'SYS_NO_DATA'

    FLOW_REVERSE = 'FLOW_REVERSE'
    FLOW_SPEED_OVER_LIMIT = 'FLOW_SPEED_OVER_LIMIT'
    CONTINUES_CONSUMPTION = 'CONTINUES_CONSUMPTION'
    NO_WATER = 'NO_WATER'  # don't use
    NO_RESOURCE = 'NO_RESOURCE'
    BATTERY_WARNING = 'BATTERY_WARNING'
    BATTERY_OR_TEMPERATURE_LIMITS = 'BATTERY_OR_TEMPERATURE_LIMITS'

    RESET = 'RESET'  # REASON IS UNAVAILABLE
    RESET_POWER_ON = 'RESET_POWER_ON'
    RESET_PIN = 'RESET_PIN'
    RESET_LOW_VOLTAGE = 'RESET_LOW_VOLTAGE'
    RESET_SOFTWARE = 'RESET_SOFTWARE'
    RESET_WATCHDOG = 'RESET_WATCHDOG'
    RESET_HARD_FAULT = 'RESET_HARD_FAULT'

    ERROR = 'ERROR'  # REASON IS UNAVAILABLE
    ERROR_SENSOR = 'ERROR_SENSOR'
    ERROR_SYSTEM = 'ERROR_SYSTEM'
    ERROR_SENSOR_MEASUREMENT = 'ERROR_SENSOR_MEASUREMENT'
    ERROR_SENSOR_TEMPERATURE = 'ERROR_SENSOR_TEMPERATURE'
    ERROR_MEASUREMENT = 'ERROR_MEASUREMENT'
    ERROR_METER_SYNC = 'ERROR_METER_SYNC'
    ERROR_LOW_VOLTAGE = 'ERROR_LOW_VOLTAGE'
    ERROR_INTERNAL_CLOCK = 'ERROR_INTERNAL_CLOCK'
    ERROR_FLASH = 'ERROR_FLASH'
    ERROR_EEPROM = 'ERROR_EEPROM'
    ERROR_RADIO = 'ERROR_RADIO'
    ERROR_DISPLAY = 'ERROR_DISPLAY'
    ERROR_PLC = 'ERROR_PLC'
    ERROR_RESET = 'ERROR_RESET'
    IMPACT_POWER_LOST = 'IMPACT_POWER_LOST'
    IMPACT_MAGNET = 'IMPACT_MAGNET'
    IMPACT_CLEAT_TAMPER = 'IMPACT_CLEAT_TAMPER'
    IMPACT_RADIO = 'IMPACT_RADIO'

    # Journal event items
    NONE = 'NONE'
    SUCCESSFUL_AUTO_DIAGNOSTIC = 'SUCCESSFUL_AUTO_DIAGNOSTIC'
    SETUP_UPDATE = 'SETUP_UPDATE'
    SWITCH_WINTER_DAYLIGHT = 'SWITCH_WINTER_DAYLIGHT'
    SWITCH_SUMMER_DAYLIGHT = 'SWITCH_SUMMER_DAYLIGHT'
    RECORD_DATETIME = 'RECORD_DATETIME'
    CHANGE_OFFSET_DAILY_CLOCK = 'CHANGE_OFFSET_DAILY_CLOCK'
    PERMISSION_SWITCH_DAYLIGHT_ON = 'PERMISSION_SWITCH_DAYLIGHT_ON'
    PERMISSION_SWITCH_DAYLIGHT_OFF = 'PERMISSION_SWITCH_DAYLIGHT_OFF'
    CHANGE_DATE_TIME_SWITCH_DAYLIGHT = 'CHANGE_DATE_TIME_SWITCH_DAYLIGHT'
    ERASE_EEPROM = 'ERASE_EEPROM'
    NULLIFY_TARIFF_ACCUMULATION = 'NULLIFY_TARIFF_ACCUMULATION'
    NULLIFY_INTERVAL_ACCUMULATION = 'NULLIFY_INTERVAL_ACCUMULATION'
    RESET_PASSWORD = 'RESET_PASSWORD'
    RESET_POWER_LOST_TIME_COUNTER = 'RESET_POWER_LOST_TIME_COUNTER'
    RESET_MAGNET_IMPACT_TIME_COUNTER = 'RESET_MAGNET_IMPACT_TIME_COUNTER'
    RESET_POWER_INCREASE_TIME_COUNTER = 'RESET_POWER_INCREASE_TIME_COUNTER'
    RESET_POWER_DECREASE_TIME_COUNTER = 'RESET_POWER_DECREASE_TIME_COUNTER'
    RESET_MAINTS_FREQ_DIVERGENCE_TIME_COUNTER = 'RESET_MAINTS_FREQ_DIVERGENCE_TIME_COUNTER'
    RESET_POWER_OVER_LIMIT_TIME_COUNTER = 'RESET_POWER_OVER_LIMIT_TIME_COUNTER'
    CHANGE_CAPACITY_DATA_LCD = 'CHANGE_CAPACITY_DATA_LCD'
    CHANGE_TARIFF_METHODS = 'CHANGE_TARIFF_METHODS'
    CHANGE_TARIFF_PROGRAMS = 'CHANGE_TARIFF_PROGRAMS'
    CHANGE_ACTUAL_SEASON_SCHEDULES = 'CHANGE_ACTUAL_SEASON_SCHEDULES'
    CHANGE_CONSUMPTION_LIMIT = 'CHANGE_CONSUMPTION_LIMIT'
    CHANGE_LOW_THRESHOLD_VOLTAGE = 'CHANGE_LOW_THRESHOLD_VOLTAGE'
    CHANGE_HIGH_THRESHOLD_VOLTAGE = 'CHANGE_HIGH_THRESHOLD_VOLTAGE'
    CHANGE_MAINTS_FREQ_THRESHOLD = 'CHANGE_MAINTS_FREQ_THRESHOLD'
    CHANGE_THRESHOLD_LOW_CONSUMPTION = 'CHANGE_THRESHOLD_LOW_CONSUMPTION'
    RECHARGE_ENERGY_PAYMENT = 'RECHARGE_ENERGY_PAYMENT'
    UNSUCCESSFUL_AUTO_DIAGNOSTIC_INTERNAL_CLOCK = 'UNSUCCESSFUL_AUTO_DIAGNOSTIC_INTERNAL_CLOCK'
    ABNORMAL_COUNTER_AUTOSTART = 'ABNORMAL_COUNTER_AUTOSTART'
    EXTERNAL_POWER_LOST = 'EXTERNAL_POWER_LOST'
    EXTERNAL_POWER_DETECTED = 'EXTERNAL_POWER_DETECTED'
    START_POWER_OVER_LIMIT = 'START_POWER_OVER_LIMIT'
    STOP_POWER_OVER_LIMIT = 'STOP_POWER_OVER_LIMIT'
    ENERGY_OVER_LIMIT_1 = 'ENERGY_OVER_LIMIT_1'
    ENERGY_OVER_LIMIT_2 = 'ENERGY_OVER_LIMIT_2'
    ENERGY_OVER_LIMIT_3 = 'ENERGY_OVER_LIMIT_3'
    WRONG_PASSWORD_BLOCK = 'WRONG_PASSWORD_BLOCK'
    WRONG_PASSWORD_APPEAL = 'WRONG_PASSWORD_APPEAL'
    EXHAUST_DAILY_BATTERY_LIFE_LIMIT = 'EXHAUST_DAILY_BATTERY_LIFE_LIMIT'
    START_MAGNET_IMPACT = 'START_MAGNET_IMPACT'
    STOP_MAGNET_IMPACT = 'STOP_MAGNET_IMPACT'
    VIOLATION_TERMINAL_BLOCK_SEAL = 'VIOLATION_TERMINAL_BLOCK_SEAL'
    RECOVERY_TERMINAL_BLOCK_SEAL = 'RECOVERY_TERMINAL_BLOCK_SEAL'
    VIOLATION_CASE_SEAL = 'VIOLATION_CASE_SEAL'
    RECOVERY_CASE_SEAL = 'RECOVERY_CASE_SEAL'
    TIME_OUT_SYNC_LIMIT = 'TIME_OUT_SYNC_LIMIT'
    CRITICAL_DIVERGENCE_TIME = 'CRITICAL_DIVERGENCE_TIME'
    OVERHEAT_COUNTER_START = 'OVERHEAT_COUNTER_START'
    OVERHEAT_COUNTER_STOP = 'OVERHEAT_COUNTER_STOP'
    UNSUCCESSFUL_AUTO_DIAGNOSTIC_MEMORY = 'UNSUCCESSFUL_AUTO_DIAGNOSTIC_MEMORY'
    LOW_BATTERY_CAPACITY = 'LOW_BATTERY_CAPACITY'
    RECOVERY_BATTERY_WORKING_VOLTAGE = 'RECOVERY_BATTERY_WORKING_VOLTAGE'
    LOW_CONSUMPTION = 'LOW_CONSUMPTION'
    RESET_FLAG_LOW_CONSUMPTION = 'RESET_FLAG_LOW_CONSUMPTION'
    CHANGE_VALIDATION_SETTINGS = 'CHANGE_VALIDATION_SETTINGS'
    UNSUCCESSFUL_AUTO_DIAGNOSTIC_MEASUREMENT_BLOCK = 'UNSUCCESSFUL_AUTO_DIAGNOSTIC_MEASUREMENT_BLOCK'
    UNSUCCESSFUL_AUTO_DIAGNOSTIC_CALCULATION_BLOCK = 'UNSUCCESSFUL_AUTO_DIAGNOSTIC_CALCULATION_BLOCK'
    UNSUCCESSFUL_AUTO_DIAGNOSTIC_POWER_BLOCK = 'UNSUCCESSFUL_AUTO_DIAGNOSTIC_POWER_BLOCK'
    UNSUCCESSFUL_AUTO_DIAGNOSTIC_SCREEN = 'UNSUCCESSFUL_AUTO_DIAGNOSTIC_SCREEN'
    UNSUCCESSFUL_AUTO_DIAGNOSTIC_RADIO = 'UNSUCCESSFUL_AUTO_DIAGNOSTIC_RADIO'
    MAINS_VOLTAGE_LOST_PHASE_A_START = 'MAINS_VOLTAGE_LOST_PHASE_A_START'
    MAINS_VOLTAGE_LOST_PHASE_A_STOP = 'MAINS_VOLTAGE_LOST_PHASE_A_STOP'
    MAINS_VOLTAGE_LOST_PHASE_B_START = 'MAINS_VOLTAGE_LOST_PHASE_B_START'
    MAINS_VOLTAGE_LOST_PHASE_B_STOP = 'MAINS_VOLTAGE_LOST_PHASE_B_STOP'
    MAINS_VOLTAGE_LOST_PHASE_C_START = 'MAINS_VOLTAGE_LOST_PHASE_C_START'
    MAINS_VOLTAGE_LOST_PHASE_C_STOP = 'MAINS_VOLTAGE_LOST_PHASE_C_STOP'
    VOLTAGE_LAYDOWN_PHASE_A_START = 'VOLTAGE_LAYDOWN_PHASE_A_START'
    VOLTAGE_LAYDOWN_PHASE_A_STOP = 'VOLTAGE_LAYDOWN_PHASE_A_STOP'
    VOLTAGE_LAYDOWN_PHASE_B_START = 'VOLTAGE_LAYDOWN_PHASE_B_START'
    VOLTAGE_LAYDOWN_PHASE_B_STOP = 'VOLTAGE_LAYDOWN_PHASE_B_STOP'
    VOLTAGE_LAYDOWN_PHASE_C_START = 'VOLTAGE_LAYDOWN_PHASE_C_START'
    VOLTAGE_LAYDOWN_PHASE_C_STOP = 'VOLTAGE_LAYDOWN_PHASE_C_STOP'
    OVERVOLTAGE_PHASE_A_START = 'OVERVOLTAGE_PHASE_A_START'
    OVERVOLTAGE_PHASE_A_STOP = 'OVERVOLTAGE_PHASE_A_STOP'
    OVERVOLTAGE_PHASE_B_START = 'OVERVOLTAGE_PHASE_B_START'
    OVERVOLTAGE_PHASE_B_STOP = 'OVERVOLTAGE_PHASE_B_STOP'
    OVERVOLTAGE_PHASE_C_START = 'OVERVOLTAGE_PHASE_C_START'
    OVERVOLTAGE_PHASE_C_STOP = 'OVERVOLTAGE_PHASE_C_STOP'
    OVERCURRENT_PHASE_A_START = 'OVERCURRENT_PHASE_A_START'
    OVERCURRENT_PHASE_A_STOP = 'OVERCURRENT_PHASE_A_STOP'
    OVERCURRENT_PHASE_B_START = 'OVERCURRENT_PHASE_B_START'
    OVERCURRENT_PHASE_B_STOP = 'OVERCURRENT_PHASE_B_STOP'
    OVERCURRENT_PHASE_C_START = 'OVERCURRENT_PHASE_C_START'
    OVERCURRENT_PHASE_C_STOP = 'OVERCURRENT_PHASE_C_STOP'
    CURRENT_SUM_THRESHOLD_LOW_START = 'CURRENT_SUM_THRESHOLD_LOW_START'
    CURRENT_SUM_THRESHOLD_LOW_STOP = 'CURRENT_SUM_THRESHOLD_LOW_STOP'
    FREQ_OUT_PHASE_A_START = 'FREQ_OUT_PHASE_A_START'
    FREQ_OUT_PHASE_A_STOP = 'FREQ_OUT_PHASE_A_STOP'
    FREQ_OUT_PHASE_B_START = 'FREQ_OUT_PHASE_B_START'
    FREQ_OUT_PHASE_B_STOP = 'FREQ_OUT_PHASE_B_STOP'
    FREQ_OUT_PHASE_C_START = 'FREQ_OUT_PHASE_C_START'
    FREQ_OUT_PHASE_C_STOP = 'FREQ_OUT_PHASE_C_STOP'
    PHASE_ORDER_DISTURBANCE_START = 'PHASE_ORDER_DISTURBANCE_START'
    PHASE_ORDER_DISTURBANCE_STOP = 'PHASE_ORDER_DISTURBANCE_STOP'
    RADIO_IMPACT_START = 'RADIO_IMPACT_START'
    RADIO_IMPACT_STOP = 'RADIO_IMPACT_STOP'
    DAYLIGHT_TIME_SWITCH = 'DAYLIGHT_TIME_SWITCH'
    DAYLIGHT_TIME_MODE_DATES_CHANGE = 'DAYLIGHT_TIME_MODE_DATES_CHANGE'
    INTERNAL_CLOCK_SYNC = 'INTERNAL_CLOCK_SYNC'
    METROLOGY_CHANGE = 'METROLOGY_CHANGE'
    PROFILE_CONF_CHANGE = 'PROFILE_CONF_CHANGE'
    TARIFFICATION_METHOD_CHANGE = 'TARIFFICATION_METHOD_CHANGE'
    PERMISSION_CHANGE_SETTINGS_POWER_CONTROL = 'PERMISSION_CHANGE_SETTINGS_POWER_CONTROL'
    CONTROL_LEVEL_MAINS_CHANGE = 'CONTROL_LEVEL_MAINS_CHANGE'
    PERMISSION_CHANGE_SETTINGS_CONSUMPTION_CONTROL = 'PERMISSION_CHANGE_SETTINGS_CONSUMPTION_CONTROL'
    LOAD_RELAY_CONDITION_SETTINGS_CHANGE = 'LOAD_RELAY_CONDITION_SETTINGS_CHANGE'
    SIGNALIZATION_RELAY_CONDITION_SETTINGS_CHANGE = 'SIGNALIZATION_RELAY_CONDITION_SETTINGS_CHANGE'
    INTERFACE_SIGNALIZATION_CONDITION_SETTINGS_CHANGE = 'INTERFACE_SIGNALIZATION_CONDITION_SETTINGS_CHANGE'
    INDICATION_SETTINGS_CHANGE = 'INDICATION_SETTINGS_CHANGE'
    SOUND_SIGNAL_CONDITION_SETTINGS_CHANGE = 'SOUND_SIGNAL_CONDITION_SETTINGS_CHANGE'
    LOAD_RELAY_STATE_CHANGE = 'LOAD_RELAY_STATE_CHANGE'
    SIGNALIZATION_RELAY_STATE_CHANGE = 'SIGNALIZATION_RELAY_STATE_CHANGE'

    SYSTEM__CIRCUIT_BREAK_T_SENSOR_1 = 'SYSTEM__CIRCUIT_BREAK_T_SENSOR_1'
    SYSTEM__CIRCUIT_BREAK_T_SENSOR_2 = 'SYSTEM__CIRCUIT_BREAK_T_SENSOR_2'
    SYSTEM__CIRCUIT_BREAK_T_SENSOR_3 = 'SYSTEM__CIRCUIT_BREAK_T_SENSOR_3'
    SYSTEM__ERROR_DELTA_T = 'SYSTEM__ERROR_DELTA_T'
    SYSTEM__CONSUMPTION_LOWER_G_MIN_CHANNEL_RATE_1 = 'SYSTEM__CONSUMPTION_LOWER_G_MIN_CHANNEL_RATE_1'
    SYSTEM__CONSUMPTION_LOWER_G_MIN_CHANNEL_RATE_2 = 'SYSTEM__CONSUMPTION_LOWER_G_MIN_CHANNEL_RATE_2'
    SYSTEM__CONSUMPTION_LOWER_G_MIN_CHANNEL_RATE_3 = 'SYSTEM__CONSUMPTION_LOWER_G_MIN_CHANNEL_RATE_3'
    SYSTEM__CONSUMPTION_LOWER_G_MAX_CHANNEL_RATE_1 = 'SYSTEM__CONSUMPTION_LOWER_G_MAX_CHANNEL_RATE_1'
    SYSTEM__CONSUMPTION_LOWER_G_MAX_CHANNEL_RATE_2 = 'SYSTEM__CONSUMPTION_LOWER_G_MAX_CHANNEL_RATE_2'
    SYSTEM__CONSUMPTION_LOWER_G_MAX_CHANNEL_RATE_3 = 'SYSTEM__CONSUMPTION_LOWER_G_MAX_CHANNEL_RATE_3'
    SYSTEM__NO_COOLANT_CHANNEL_RATE_1 = 'SYSTEM__NO_COOLANT_CHANNEL_RATE_1'
    SYSTEM__NO_COOLANT_CHANNEL_RATE_2 = 'SYSTEM__NO_COOLANT_CHANNEL_RATE_2'
    SYSTEM__NO_COOLANT_CHANNEL_RATE_3 = 'SYSTEM__NO_COOLANT_CHANNEL_RATE_3'
    SYSTEM__CIRCUIT_BREAK_STIMULATION_CHANNEL_RATE_1 = 'SYSTEM__CIRCUIT_BREAK_STIMULATION_CHANNEL_RATE_1'
    SYSTEM__CIRCUIT_BREAK_STIMULATION_CHANNEL_RATE_2 = 'SYSTEM__CIRCUIT_BREAK_STIMULATION_CHANNEL_RATE_2'
    SYSTEM__CIRCUIT_BREAK_PRESSURE_SENSOR_1 = 'SYSTEM__CIRCUIT_BREAK_PRESSURE_SENSOR_1'
    SYSTEM__CIRCUIT_BREAK_PRESSURE_SENSOR_2 = 'SYSTEM__CIRCUIT_BREAK_PRESSURE_SENSOR_2'
    SYSTEM__CIRCUIT_BREAK_PRESSURE_SENSOR_3 = 'SYSTEM__CIRCUIT_BREAK_PRESSURE_SENSOR_3'
    SYSTEM__REVERSE = 'SYSTEM__REVERSE'

    DEVICE__POWER_SUPPLY_LOST = 'DEVICE__POWER_SUPPLY_LOST'
    DEVICE__POWER_SUPPLY_ENABLED = 'DEVICE__POWER_SUPPLY_ENABLED'
    DEVICE__COMMON_SETTINGS_CHANGED = 'DEVICE__COMMON_SETTINGS_CHANGED'
    DEVICE__ALARM_DIGITAL_INPUT_1 = 'DEVICE__ALARM_DIGITAL_INPUT_1'
    DEVICE__ALARM_OVERRATE_DIGITAL_INPUT_1 = 'DEVICE__ALARM_OVERRATE_DIGITAL_INPUT_1'
    DEVICE__ALARM_OVERRATE_DIGITAL_INPUT_2 = 'DEVICE__ALARM_OVERRATE_DIGITAL_INPUT_2'
    DEVICE__ALARM_UNDERRATE_DIGITAL_INPUT_1 = 'DEVICE__ALARM_UNDERRATE_DIGITAL_INPUT_1'
    DEVICE__ALARM_UNDERRATE_DIGITAL_INPUT_2 = 'DEVICE__ALARM_UNDERRATE_DIGITAL_INPUT_2'
    DEVICE__ALARM_T_HIGH_DIGITAL_INPUT_1 = 'DEVICE__ALARM_T_HIGH_DIGITAL_INPUT_1'
    DEVICE__ALARM_T_HIGH_DIGITAL_INPUT_2 = 'DEVICE__ALARM_T_HIGH_DIGITAL_INPUT_2'
    DEVICE__ALARM_T_LOW_DIGITAL_INPUT_1 = 'DEVICE__ALARM_T_LOW_DIGITAL_INPUT_1'
    DEVICE__ALARM_T_LOW_DIGITAL_INPUT_2 = 'DEVICE__ALARM_T_LOW_DIGITAL_INPUT_2'
    DEVICE__ALARM_DELTA_T_HIGH_DIGITAL_INPUT_1 = 'DEVICE__ALARM_DELTA_T_HIGH_DIGITAL_INPUT_1'
    DEVICE__ALARM_DELTA_T_HIGH_DIGITAL_INPUT_2 = 'DEVICE__ALARM_DELTA_T_HIGH_DIGITAL_INPUT_2'
    DEVICE__ALARM_DELTA_T_LOW_DIGITAL_INPUT_1 = 'DEVICE__ALARM_DELTA_T_LOW_DIGITAL_INPUT_1'
    DEVICE__ALARM_DELTA_T_LOW_DIGITAL_INPUT_2 = 'DEVICE__ALARM_DELTA_T_LOW_DIGITAL_INPUT_2'
    DEVICE__ALARM_POWER_HIGH_DIGITAL_INPUT_1 = 'DEVICE__ALARM_POWER_HIGH_DIGITAL_INPUT_1'
    DEVICE__ALARM_POWER_HIGH_DIGITAL_INPUT_2 = 'DEVICE__ALARM_POWER_HIGH_DIGITAL_INPUT_2'
    DEVICE__ALARM_POWER_LOW_DIGITAL_INPUT_1 = 'DEVICE__ALARM_POWER_LOW_DIGITAL_INPUT_1'
    DEVICE__ALARM_POWER_LOW_DIGITAL_INPUT_2 = 'DEVICE__ALARM_POWER_LOW_DIGITAL_INPUT_2'
    DEVICE__MEASURE_CHANNELS_SETTINGS_CHANGED = 'DEVICE__MEASURE_CHANNELS_SETTINGS_CHANGED'
    DEVICE__SYSTEM_SETTINGS_CHANGED_1 = 'DEVICE__SYSTEM_SETTINGS_CHANGED_1'
    DEVICE__SYSTEM_SETTINGS_CHANGED_2 = 'DEVICE__SYSTEM_SETTINGS_CHANGED_2'
    DEVICE__SYSTEM_SETTINGS_CHANGED_3 = 'DEVICE__SYSTEM_SETTINGS_CHANGED_3'
    DEVICE__SYSTEM_SETTINGS_CHANGED_4 = 'DEVICE__SYSTEM_SETTINGS_CHANGED_4'
    DEVICE__DIGITAL_I_O_SETTINGS_CHANGED = 'DEVICE__DIGITAL_I_O_SETTINGS_CHANGED'
    DEVICE__DATETIME_CHANGED = 'DEVICE__DATETIME_CHANGED'
    DEVICE__ETHERNET_SETTINGS_CHANGED = 'DEVICE__ETHERNET_SETTINGS_CHANGED'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class IntegrationV0MessageMetaBSChannelProtocol(Enum):
    nbfi = 'nbfi'
    unbp = 'unbp'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class IntervalSelectValue(Enum):
    half_hour = '30 minute'
    hour = '60 minutes'
    day = '1 day'
    week = '1 week'
    month = '1 month'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class DeviceHack(Enum):
    """
    electricity_profile_packets_days_ago_is_zero: change profile window logic when days_ago = 0 when days_ago=0 fill full hours profile values after packet receive

    electricity_daily_packet_overload_value: change overload value of daily packet to 838861.0, bug was fixed in mid-April 2023 firmware 147:14:17:3:1:1

    electricity_phase_packet_generation_total_enrg_overload_value: change overload value for total energy to 33554431 in generated phase packets
    electricity_phase_packet_consumption_total_enrg_overload_value: change overload value for total energy to 33554431 in consumed phase packets
    """

    electricity_profile_packets_days_ago_is_zero = 'electricity_profile_packets_days_ago_is_zero'
    electricity_phase_packet_generated_total_enrg_overload_value = 'electricity_phase_packet_generated_total_enrg_overload_value'
    electricity_phase_packet_consumed_total_enrg_overload_value = 'electricity_phase_packet_consumed_total_enrg_overload_value'
    electricity_daily_packet_overload_value = 'electricity_daily_packet_overload_value'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class DeviceTimeTransition(Enum):
    """
    Enumeration of seasons change
    """
    summer = 'summer'
    winter = 'winter'
    unknown = 'unknown'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class DeviceClockOutOfSyncType(Enum):
    """
    Enumeration of clock sync states
    """
    synced = 'synced'
    out_of_sync_warning = 'out_of_sync_warning'
    out_of_sync_critical = 'out_of_sync_critical'
    unsynchronized = 'unsynchronized'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class DownlinkTaskType(Enum):
    time_sync = 'time_sync'
    firmware_update = 'firmware_update'
    unbp_message = 'unbp_message'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class ScheduleType(Enum):
    on_capture = 'on_capture'
    schedule = 'schedule'
    asap = 'asap'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class ReglamentType(Enum):
    ul_pr_dl_none = 'ul_pr_dl_none'
    ul_pr_dl_rm_on_capture = 'ul_pr_dl_rm_on_capture'
    ul_pr_dl_rm = 'ul_pr_dl_rm'
    ul_rm_dl_rm = 'ul_rm_dl_rm'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class SignalModulation(Enum):
    fsk = 'fsk'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class DownlinkTaskStatus(Enum):
    created = 'created'
    bs_ack = 'bs_ack'
    bs_executed_succeed = 'bs_executed_succeed'
    bs_executed_failed = 'bs_executed_failed'
    bs_skipped = 'bs_skipped'
    canceled = 'canceled'
    bs_deleted = 'bs_deleted'

    def __repr__(self) -> str:
        return f'{type(self).__name__}.{self.name}'


class DataAggregatorApiUserType(Enum):
    base_station = "base_station"
    api_user = "api_user"
    other = "other"
    USPD = "USPD"
    universal_data_input_api = "universal_data_input_api"
