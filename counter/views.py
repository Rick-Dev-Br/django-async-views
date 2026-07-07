import asyncio
import time

from django.http import JsonResponse


def index(request):
    return JsonResponse(
        {
            "message": "Projeto Django Async Views",
            "counter_url": "/contador/",
            "example": "/contador/?seconds=3",
        }
    )


def parse_seconds(value, default=3, maximum=10):
    try:
        seconds = int(value)
    except (TypeError, ValueError):
        return default

    return min(max(seconds, 0), maximum)


async def async_time_counter(request):
    total_seconds = parse_seconds(request.GET.get("seconds"))
    started_at = time.perf_counter()
    ticks = []

    for second in range(1, total_seconds + 1):
        await asyncio.sleep(1)
        ticks.append(second)

    elapsed_seconds = round(time.perf_counter() - started_at, 2)

    return JsonResponse(
        {
            "message": "Contador assincrono finalizado",
            "mode": "async",
            "requested_seconds": total_seconds,
            "ticks": ticks,
            "elapsed_seconds": elapsed_seconds,
        }
    )
