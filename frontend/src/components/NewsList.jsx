import React from "react";
import { Link } from "react-router-dom";
import './NewsList.css';

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
    }
]


const NewsList = () => {
    return (
        <div className="news-list">
            {list.map((news) => (
                <div key={news.id} className="news-item">
                    <h2>{news.title}</h2>
                    <p>{news.summary}</p>
                    <Link to={`/articles/${news.id}`}>Read more</Link>
                </div>
            ))}
        </div>
    )
};

export default NewsList;