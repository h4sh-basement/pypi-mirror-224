import json

def merge_deltas(original, delta):
    """
    Pushes the delta into the original and returns that.

    Great for reconstructing OpenAI streaming responses -> complete message objects.
    """
    for key, value in delta.items():
        if isinstance(value, dict):
            if key not in original:
                original[key] = value
            else:
                merge_deltas(original[key], value)
        else:
            if key in original:
                original[key] += value
            else:
                original[key] = value
    return original

def escape_newlines_in_json_string_values(s):
    result = []
    in_string = False
    for ch in s:
        if ch == '"' and (len(result) == 0 or result[-1] != '\\'):
            in_string = not in_string
        if in_string and ch == '\n':
            result.append('\\n')
        else:
            result.append(ch)
    return ''.join(result)

def parse_partial_json(s):
    # Initialize a stack to keep track of open braces, brackets, and strings.
    stack = []
    is_inside_string = False
    escaped = False

    # Process each character in the string one at a time.
    for char in s:
        if is_inside_string:
            if char == '"' and not escaped:
                is_inside_string = False
            elif char == '\\':
                escaped = not escaped
            else:
                escaped = False
        else:
            if char == '"':
                is_inside_string = True
                escaped = False
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            elif char == '}' or char == ']':
                if stack and stack[-1] == char:
                    stack.pop()
                else:
                    # Mismatched closing character; the input is malformed.
                    return None

    # If we're still inside a string at the end of processing, we need to close the string.
    if is_inside_string:
        s += '"'

    # Close any remaining open structures in the reverse order that they were opened.
    for closing_char in reversed(stack):
        s += closing_char

    # Attempt to parse the modified string as JSON.
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        # If we still can't parse the string as JSON, return None to indicate failure.
        return None
