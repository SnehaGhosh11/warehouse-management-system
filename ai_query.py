import pandas as pd
from sqlalchemy import create_engine
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

# Load data from database
engine = create_engine("sqlite:///wms.db", echo=False)
df = pd.read_sql("SELECT * FROM sales", con=engine)

# Setup AI (using your API key directly - for local only)
llm = OpenAI(api_token="my secret key")

smart_df = SmartDataframe(df, config={"llm": llm})

while True:
    query = input("Ask about your sales data (or type exit): ")
    if query.lower() == "exit":
        break
    answer = smart_df.chat(query)
    print("AI Answer:\n", answer)
