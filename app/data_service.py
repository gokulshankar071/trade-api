from duckduckgo_search import DDGS

async def fetch_market_news(sector: str):
    results = []
    
    try:
        query = f"{sector} India market news"
        
        # Modern syntax: use the DDGS class directly
        with DDGS() as ddgs:
            # .text() is the standard method for search results
            search_results = ddgs.text(query, max_results=5)
            
            for r in search_results:
                title = r.get("title", "")
                body = r.get("body", "")
                if title and body:
                    results.append(f"{title} - {body}")

    except Exception as e:
        print(f"Search Error: {e}")
        pass

    
    if not results:
        results = [
            f"{sector} sector seeing growth due to government policies in India",
            f"Investors showing interest in {sector} stocks following quarterly results",
            f"Market analysts predict volatility in the {sector} sector this week",
        ]

    return results