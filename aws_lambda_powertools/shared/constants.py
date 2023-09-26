TRACER_CAPTURE_RESPONSE_ENV: str = "POWERTOOLS_TRACER_CAPTURE_RESPONSE"
TRACER_CAPTURE_ERROR_ENV: str = "POWERTOOLS_TRACER_CAPTURE_ERROR"
TRACER_DISABLED_ENV: str = "POWERTOOLS_TRACE_DISABLED"

LOGGER_LOG_SAMPLING_RATE: str = "POWERTOOLS_LOGGER_SAMPLE_RATE"
LOGGER_LOG_EVENT_ENV: str = "POWERTOOLS_LOGGER_LOG_EVENT"
LOGGER_LOG_DEDUPLICATION_ENV: str = "POWERTOOLS_LOG_DEDUPLICATION_DISABLED"

MIDDLEWARE_FACTORY_TRACE_ENV: str = "POWERTOOLS_TRACE_MIDDLEWARES"

METRICS_NAMESPACE_ENV: str = "POWERTOOLS_METRICS_NAMESPACE"

DATADOG_FLUSH_TO_LOG: str = "DD_FLUSH_TO_LOG"

SERVICE_NAME_ENV: str = "POWERTOOLS_SERVICE_NAME"
XRAY_TRACE_ID_ENV: str = "_X_AMZN_TRACE_ID"
LAMBDA_TASK_ROOT_ENV: str = "LAMBDA_TASK_ROOT"


LAMBDA_FUNCTION_NAME_ENV: str = "AWS_LAMBDA_FUNCTION_NAME"

XRAY_SDK_MODULE: str = "aws_xray_sdk"
XRAY_SDK_CORE_MODULE: str = "aws_xray_sdk.core"

IDEMPOTENCY_DISABLED_ENV: str = "POWERTOOLS_IDEMPOTENCY_DISABLED"

PARAMETERS_SSM_DECRYPT_ENV: str = "POWERTOOLS_PARAMETERS_SSM_DECRYPT"
PARAMETERS_MAX_AGE_ENV: str = "POWERTOOLS_PARAMETERS_MAX_AGE"

LOGGER_LAMBDA_CONTEXT_KEYS = [
    "function_arn",
    "function_memory_size",
    "function_name",
    "function_request_id",
    "cold_start",
    "xray_trace_id",
]

# JSON indentation level
PRETTY_INDENT: int = 4
COMPACT_INDENT = None

POWERTOOLS_DEV_ENV: str = "POWERTOOLS_DEV"
POWERTOOLS_DEBUG_ENV: str = "POWERTOOLS_DEBUG"

POWERTOOLS_TRACEBACK_ENV: str = "POWERTOOLS_LOGGER_ENHANCED_TRACEBACK"