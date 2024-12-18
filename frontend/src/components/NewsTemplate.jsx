import React from "react";
import "./NewsTemplate.css";

const NewsTemplate = ({ date, views, title, content, chartImageUrl }) => {
  return (
    <div className="news-template">
      <h1 className="news-title">
        {title || "Breaking News: Market Hits Record High"}
      </h1>

      <div className="news-meta">
        <span className="news-date">{date || "2023. 10. 1."}</span>
        <span className="news-views">Views: {views || "1500"}</span>
      </div>

      <div className="ticker-container">
        <span className="ticker">AAPL</span>
        <span className="ticker">GOOGL</span>
        <span className="ticker">AMZN</span>
      </div>

      <p className="news-content">
        {content ||
          "The stock market reached an all-time high today, driven by strong earnings reports..."}
      </p>

      <a href="#" className="read-more">
        Read Original Article
      </a>
    </div>
  );
};

export default NewsTemplate;
