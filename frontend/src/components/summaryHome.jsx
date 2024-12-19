import React from "react";
import { Link } from "react-router-dom";
import "./Summary.css";

const list = [
  {
    id: 1,
    title: "Breaking News: Market Hits Record High",
    body: "The stock market reached an all-time high today, driven by strong earnings reports...",
    createdAt: "2023-10-01T10:00:00Z",
    tickerIds: ["AAPL", "GOOGL", "AMZN"],
    views: 1500,
    originalUrl: "https://news.example.com/market-high",
    summary: "The stock market reached an all-time high today...",
  },
  {
    id: 2,
    title: "Tech Giants Release New Gadgets",
    body: "Several tech giants have released their latest gadgets in a highly anticipated event...",
    createdAt: "2023-10-02T12:00:00Z",
    tickerIds: ["AAPL", "MSFT"],
    views: 1200,
    originalUrl: "https://news.example.com/new-gadgets",
    summary: "Several tech giants have released their latest gadgets...",
  },
  {
    id: 3,
    title: "Economic Growth Slows Down",
    body: "The latest economic reports indicate a slowdown in growth, raising concerns among investors...",
    createdAt: "2023-10-03T14:00:00Z",
    tickerIds: ["SPY", "DIA"],
    views: 900,
    originalUrl: "https://news.example.com/economic-growth",
    summary: "The latest economic reports indicate a slowdown in growth...",
  },
];

const SummaryHome = () => {
  return (
    <div className="summary-home">
      <h1 className="summary-home-title">Latest News Summaries</h1>
      <div className="summary-grid">
        {list.map((news) => (
          <div key={news.id} className="summary-card">
            <h2 className="card-title">{news.title}</h2>
            <div className="card-meta">
              <span className="card-date">
                {new Date(news.createdAt).toLocaleDateString()}
              </span>
              <span className="card-views">Views: {news.views}</span>
            </div>
            <p className="card-summary">{news.summary}</p>
            <div className="card-tickers">
              {news.tickerIds.map((ticker) => (
                <span key={ticker} className="ticker-tag">
                  {ticker}
                </span>
              ))}
            </div>
            <Link to={`/summary/${news.id}`} className="read-more-link">
              View Full Summary
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SummaryHome;
