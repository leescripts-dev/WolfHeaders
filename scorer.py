SECURITY_HEADERS = {
    "Content-Security-Policy":
        "Protects against Cross-Site Scripting (XSS).",

    "Strict-Transport-Security":
        "Forces browsers to use HTTPS.",

    "X-Frame-Options":
        "Protects against clickjacking.",

    "X-Content-Type-Options":
        "Prevents MIME-type sniffing.",

    "Referrer-Policy":
        "Controls referrer information.",

    "Permissions-Policy":
        "Restricts browser features.",

    "Cross-Origin-Embedder-Policy":
        "Provides cross-origin isolation.",

    "Cross-Origin-Opener-Policy":
        "Protects browsing contexts.",

    "Cross-Origin-Resource-Policy":
        "Restricts resource sharing."
}


def analyze_headers(headers):
    results = []

    score = 0

    for header, description in SECURITY_HEADERS.items():

        present = header in headers

        if present:
            score += 1

        results.append({
            "header": header,
            "present": present,
            "description": description
        })

    return score, len(SECURITY_HEADERS), results