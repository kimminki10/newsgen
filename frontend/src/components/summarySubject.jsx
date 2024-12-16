import React from "react";
import { useParams } from "react-router-dom";
import { list } from "../data/newsList";
import "./Summary.css";

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
