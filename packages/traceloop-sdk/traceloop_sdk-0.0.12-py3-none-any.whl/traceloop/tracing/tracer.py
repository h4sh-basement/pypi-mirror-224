import os
from typing import Optional

from opentelemetry import trace, context
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from traceloop.instrumentation.openai import OpenAIInstrumentor
import importlib.util

from traceloop.semconv import SpanAttributes
from traceloop.tracing.no_log_span_batch_processor import NoLogSpanBatchProcessor

TRACER_NAME = "traceloop.tracer"
TRACELOOP_API_ENDPOINT = "https://api.traceloop.dev/v1/traces"


def span_processor_on_start(span, parent_context):
    span.set_attribute(SpanAttributes.TRACELOOP_CORRELATION_ID, Tracer.get_correlation_id())


class Tracer:
    __instance = None
    __correlation_id = None

    @staticmethod
    def init(app_name: Optional[str] = None):
        api_key = os.getenv("TRACELOOP_API_KEY")
        api_endpoint = os.getenv("TRACELOOP_API_ENDPOINT") or TRACELOOP_API_ENDPOINT
        print(f"Initializing Traceloop Tracer... API endpoint: {api_endpoint}")

        if app_name is not None:
            os.environ["OTEL_SERVICE_NAME"] = app_name

        provider = TracerProvider()
        exporter = OTLPSpanExporter(
            endpoint=api_endpoint,
            headers={
                "Authorization": f"Bearer {api_key}",
            }
        )
        processor = NoLogSpanBatchProcessor(exporter)
        processor.on_start = span_processor_on_start
        provider.add_span_processor(processor)
        trace.set_tracer_provider(provider)
        Tracer.__instance = trace.get_tracer(TRACER_NAME)

        if importlib.util.find_spec("openai") is not None:
            OpenAIInstrumentor().instrument()

        if importlib.util.find_spec("requests") is not None:
            from opentelemetry.instrumentation.requests import RequestsInstrumentor
            RequestsInstrumentor().instrument(excluded_urls="^https://api.openai.com")

        if importlib.util.find_spec("mysql") is not None:
            from opentelemetry.instrumentation.mysql import MySQLInstrumentor
            MySQLInstrumentor().instrument()

    @staticmethod
    def instance():
        if Tracer.__instance is None:
            raise Exception("Tracer is not initialized")
        return Tracer.__instance

    @staticmethod
    def set_correlation_id(correlation_id: str):
        Tracer.__correlation_id = correlation_id

    @staticmethod
    def get_correlation_id():
        return Tracer.__correlation_id
