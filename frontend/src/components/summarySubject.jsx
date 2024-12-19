import React from "react";
import { useParams } from "react-router-dom";
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


const SummarySubject = () => {
  const { id } = useParams();
  const newsItem = list.find((item) => item.id === parseInt(id));

  if (!newsItem) {
    return <div className="summary-error">Article not found</div>;
  }

  return (
    <div className="summary-subject">
      <h1 className="summary-title">{newsItem.title}</h1>
      <div className="summary-meta">
        <span className="summary-date">
          {new Date(newsItem.createdAt).toLocaleDateString()}
        </span>
        <span className="summary-views">Views: {newsItem.views}</span>
      </div>
      <div className="summary-tickers">
        {newsItem.tickerIds.map((ticker) => (
          <span key={ticker} className="ticker-tag">
            {ticker}
          </span>
        ))}
      </div>
      <p className="summary-body">{newsItem.body}</p>
      <div className="summary-footer">
        <a
          href={newsItem.originalUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="original-link"
        >
          Read Original Article
        </a>
      </div>
    </div>
  );
};

export default SummarySubject;
