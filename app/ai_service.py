import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Initialize the client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

async def generate_market_report(sector, news):
    prompt = f"""
    You are a financial market analyst specializing in the Indian market.
    Sector: {sector}
    News Context: {news}

    Generate a professional markdown report with:
    1. Sector Overview
    2. Key Trends
    3. Trade Opportunities
    4. Risk Factors
    5. Short Conclusion
    """

    try:
        # This block MUST be indented inside the function
        response = client.models.generate_content(
            model="gemini-flash-latest", 
            contents=prompt
        )
        
        if response and response.text:
            return response.text
        return "AI generated an empty response."

    except Exception as e:
        if "429" in str(e):
            return "AI is currently busy (Rate Limit). Please wait 30 seconds and try again."
        return f"AI Error: {str(e)}"