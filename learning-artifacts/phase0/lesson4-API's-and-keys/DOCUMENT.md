# Phase 0, Lesson 4: APIs and Keys

## What an API request does

Your program sends a request to a service. The service checks the request and sends back a response, often as JSON.

| Part | Purpose |
|---|---|
| Endpoint | The URL that receives the request. |
| API key | Identifies your account and authorizes your request. |
| Request body | Names the model and describes the task. |
| Response body | Holds the result and usage information. |

## Keep API keys private

Read the key from the `ANTHROPIC_API_KEY` environment variable. Do not write a real key in a Python file, commit, or chat message.

You can store a key in a local `.env` file. Keep `.env` in `.gitignore` so Git does not add it to a commit. This script does not load `.env` files, so export the key in your shell as shown below.

Set a key in the current shell like this:

```bash
export ANTHROPIC_API_KEY="your-key-goes-here"
```

Use your own key in your terminal. Never replace the placeholder in this document with a real key.

## Two ways to send a request

The Anthropic Python SDK builds and sends the request for you. It also turns the JSON response into Python objects.

Raw HTTP makes each part visible. The program builds the URL, headers, and JSON body, then sends a POST request.

Anthropic's raw request uses the `x-api-key` header for authentication. It also sends the `anthropic-version` header.

Both methods send a model name, a token limit, and a message. Both return response text and input and output token counts.

## Common API errors

| Status | Meaning | What to check |
|---|---|---|
| 401 | The request is not authenticated. | Check that the key is set and valid. |
| 429 | The request reached a rate limit. | Wait before you try again. |

Read the status code and error message before changing your code. Network problems can also stop a request from reaching the service.

## Exercise script

`exercise.py` supports the SDK, raw HTTP, or both methods. It reads the key from the environment and does not print the key.

Run a dry check without sending a request:

```bash
python exercise.py --dry-run --method both
```

After you have a valid key and API credits, make one SDK request:

```bash
python exercise.py --method sdk
```

Use `--method http` to send the same prompt with raw HTTP. Use `--method both` to send two requests and compare their replies and token counts. Both mode makes two API calls.

Use a fake key to view an authentication error:

```bash
python exercise.py --method http --invalid-key
```

The script defaults to `claude-sonnet-5`. Set `LLM_MODEL` or pass `--model` to choose another model ID.

## Practice record

- I added `.env` to the repository's `.gitignore` file.
- I wrote the SDK and raw HTTP request paths in `exercise.py`.
- Python syntax checking and dry-run mode passed. The dry run sent no API request.
- A live request and response comparison are still pending because I do not have API credits.
