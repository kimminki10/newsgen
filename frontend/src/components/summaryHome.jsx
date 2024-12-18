import React from "react";
import { Link } from "react-router-dom";
import { list } from "../data/newsList";
import "./Summary.css";

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
