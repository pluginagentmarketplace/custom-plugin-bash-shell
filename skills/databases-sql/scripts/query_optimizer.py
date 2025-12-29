#!/usr/bin/env python3
"""SQL query analysis and optimization suggestions."""

def analyze_query(query: str) -> dict:
    suggestions = []
    query_lower = query.lower()

    if "select *" in query_lower:
        suggestions.append("Avoid SELECT * - specify columns")

    if "where" not in query_lower and "join" in query_lower:
        suggestions.append("Add WHERE clause for JOIN")

    if "order by" in query_lower and "limit" not in query_lower:
        suggestions.append("Add LIMIT with ORDER BY")

    return {"query": query, "suggestions": suggestions}

if __name__ == "__main__":
    print(analyze_query("SELECT * FROM users"))
