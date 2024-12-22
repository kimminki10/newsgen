from journalist import prompts
import os
from langchain_openai import AzureChatOpenAI

class AzureAPI:
    def __init__(self, topic):
        if topic not in ["title", "short_content", "long_content", "tts"]:
            raise ValueError("Invalid topic. Choose from 'title', 'short_content', 'long_content', 'tts'.")
        self.messages = [
            ("system", prompts.prompts_dict[topic]),
        ]
        self.openai = AzureChatOpenAI(
            azure_deployment="gpt-4",
            api_version="2024-08-01-preview",
        )

    def get_response(self, content):
        self.response = self.openai.invoke(self.messages + [("user", content)])
        return self.response.content

if __name__=="__main__":
    from dotenv import load_dotenv
    load_dotenv()
    api = AzureAPI("title")
    content = api.get_response("""
Shares of Nvidia (NASDAQ: NVDA) have doubled in each of the last two years. The stock soared 239% in 2023 and is up 170% year to date at the time of this writing. Investors expect Nvidia to report another year of strong growth in 2025 as $1 trillion worth of data center infrastructure transitions to more advanced hardware for artificial intelligence (AI).

It might be tempting to buy the stock anticipating another year of outstanding returns. But let's look at where Nvidia's data center business stands heading into the new year, and what investors should expect from the stock.

Revenue growth is starting to slow
The consensus Wall Street estimate calls for revenue to increase 51% in the coming fiscal year (ending Jan. 2026). That is a tremendous amount of growth for a company expected to report $129 billion in revenue this year.

Nvidia's launch of Blackwell, which is scheduled to ramp up in 2025, is the wild card that could surprise to the upside. Blackwell is a complete computing platform that utilizes multiple chips to deliver breakthrough performance for generative AI, quantum computing, and other high-performance computing tasks.


"Blackwell demand is staggering, and we are racing to scale supply to meet the incredible demand customers are placing on us," CFO Colette Kress said on the company's fiscal 2025 Q3 earnings call.

But this demand may already be reflected in analysts' estimates. The biggest headwind for Nvidia is that Blackwell sales will be up against very difficult growth comparisons. Revenue grew 94% year over year in fiscal Q3, down from 122% in Q2 and 262% in Q1.

Where will the stock be in one year?
Kress' comment about near-term demand for Blackwell indicates Nvidia is still well positioned to see incredible demand, even if revenue growth is starting to slow. AI models are only getting larger and smarter, which will require more powerful GPUs over time. But investors should be aware of the risks that could limit the stock's gains next year.

In terms of competition, Advanced Micro Devices (NASDAQ: AMD) is also seeing strong growth with its Instinct data center graphics processing units (GPUs). AMD's data center segment posted revenue growth of 122% year over year last quarter, outpacing its larger rival.


Still, this isn't enough growth for AMD to take a meaningful amount of market share. Nvidia has the most robust supply chain to meet demand. Its data center GPU business generated $30.8 billion in revenue last quarter, significantly higher than AMD's quarterly data center revenue of $3.5 billion

A greater risk for Nvidia investors might be slowing growth and the impact that could have on valuation. The stock trades at a price-to-earnings (P/E) ratio of 54, and this is consistent with the stock's previous five-year trading history. That said, it's important to recognize this premium valuation is likely anchored to investors' bullish expectations for triple-digit growth rates. Those days are likely over.

Wall Street analysts expect Nvidia's earnings to grow roughly in line with revenue next year at 50%. If investors decide to bid the stock down to, say, a 40 P/E this time next year, that would put the share price at $177 based on next year's earnings estimate, implying upside of 28%. And that P/E multiple would still represent a big premium over the average stock.


The potential for a lower P/E multiple as Nvidia's growth slows is why I wouldn't buy the stock with the expectation of another year of monster returns. It's very possible the stock will deliver a more modest performance in 2025, so investors should only buy shares as part of a long-term investment.

Should you invest $1,000 in Nvidia right now?
Before you buy stock in Nvidia, consider this:

The Motley Fool Stock Advisor analyst team just identified what they believe are the 10 best stocks for investors to buy now… and Nvidia wasn’t one of them. The 10 stocks that made the cut could produce monster returns in the coming years.

Consider when Nvidia made this list on April 15, 2005... if you invested $1,000 at the time of our recommendation, you’d have $822,755!*

Stock Advisor provides investors with an easy-to-follow blueprint for success, including guidance on building a portfolio, regular updates from analysts, and two new stock picks each month. The Stock Advisor service has more than quadrupled the return of S&P 500 since 2002*.

See the 10 stocks »

*Stock Advisor returns as of December 16, 2024

John Ballard has positions in Advanced Micro Devices and Nvidia. The Motley Fool has positions in and recommends Advanced Micro Devices and Nvidia. The Motley Fool has a disclosure policy.

Nvidia Stock Keeps Growing for Investors, but Is It Time to Lower Expectations for 2025? was originally published by The Motley Foo
""")
    print(content)