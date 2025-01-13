def http_status(status):
    match status:
        case 200:
            return  "ok"
        case 404:
            return "not found"
        case 500:
            return  "internal server error"
        case _:
            return "unknown status"

print(http_status(5004))