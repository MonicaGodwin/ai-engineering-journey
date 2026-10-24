"""Make one Anthropic Messages API request through the SDK or raw HTTP."""

import argparse
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


API_URL = "https://api.anthropic.com/v1/messages"
DEFAULT_MODEL = "claude-sonnet-5"
DEFAULT_PROMPT = "What is a neural network in one sentence?"


def show_result(label: str, result: dict) -> None:
    """Print the reply and token counts without printing request secrets."""
    text = "\n".join(
        block.get("text", "")
        for block in result.get("content", [])
        if block.get("type") == "text"
    )
    usage = result.get("usage", {})
    print(f"{label}: {text or '(no text returned)'}")
    print(
        "Tokens used: "
        f"{usage.get('input_tokens', '?')} in, "
        f"{usage.get('output_tokens', '?')} out"
    )


def call_with_sdk(api_key: str, model: str, prompt: str) -> int:
    """Send the request with the optional Anthropic Python SDK."""
    try:
        import anthropic
    except ImportError:
        print("SDK unavailable. Install it with: python -m pip install anthropic")
        return 1

    try:
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model=model,
            max_tokens=256,
            messages=[{"role": "user", "content": prompt}],
        )
    except Exception as error:
        print(f"SDK request failed: {type(error).__name__}: {error}")
        return 1

    result = {
        "content": [
            {"type": block.type, "text": block.text}
            for block in response.content
            if getattr(block, "type", None) == "text"
        ],
        "usage": {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
        },
    }
    show_result("SDK response", result)
    return 0


def call_with_raw_http(api_key: str, model: str, prompt: str) -> int:
    """Send the same request with Python's standard-library HTTP client."""
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }
    body = json.dumps(
        {
            "model": model,
            "max_tokens": 256,
            "messages": [{"role": "user", "content": prompt}],
        }
    ).encode("utf-8")
    request = Request(API_URL, data=body, headers=headers, method="POST")

    try:
        with urlopen(request, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        try:
            details = json.loads(error.read().decode("utf-8"))
            api_error = details.get("error", {})
            message = api_error.get("message", "No error details returned")
            error_type = api_error.get("type", "API error")
        except (json.JSONDecodeError, UnicodeDecodeError):
            message = "The server returned a non-JSON error body"
            error_type = "HTTP error"

        print(f"HTTP {error.code} {error_type}: {message}")
        if error.code == 401:
            print("Check that ANTHROPIC_API_KEY is valid and active.")
        elif error.code == 429:
            print("The rate limit was reached. Wait before trying again.")
        return 1
    except URLError as error:
        print(f"Network request failed: {error.reason}")
        return 1
    except json.JSONDecodeError:
        print("The server returned invalid JSON.")
        return 1

    show_result("Raw HTTP response", result)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--method",
        choices=("sdk", "http", "both"),
        default="sdk",
        help="Use the SDK, raw HTTP, or both (both sends two requests).",
    )
    parser.add_argument("--prompt", default=DEFAULT_PROMPT)
    parser.add_argument(
        "--model",
        default=os.environ.get("LLM_MODEL", DEFAULT_MODEL),
        help="Model ID. Defaults to LLM_MODEL or the current lesson model.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show request settings without contacting the API.",
    )
    parser.add_argument(
        "--invalid-key",
        action="store_true",
        help="Send a fake key to demonstrate an authentication error.",
    )
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if args.dry_run:
        print("Dry run. No API request was sent.")
        print(f"Method: {args.method}")
        print(f"Model: {args.model}")
        print(f"API key configured: {'yes' if api_key else 'no'}")
        return 0

    if args.invalid_key:
        api_key = "sk-ant-invalid-for-auth-check"
    elif not api_key:
        print("Set ANTHROPIC_API_KEY in your shell before making a request.")
        print("Do not put the key in this file or paste it into chat.")
        return 2

    methods = ("sdk", "http") if args.method == "both" else (args.method,)
    exit_codes = []
    for method in methods:
        print(f"\nRequest method: {method}")
        if method == "sdk":
            exit_codes.append(call_with_sdk(api_key, args.model, args.prompt))
        else:
            exit_codes.append(call_with_raw_http(api_key, args.model, args.prompt))

    return 1 if any(exit_codes) else 0


if __name__ == "__main__":
    sys.exit(main())
