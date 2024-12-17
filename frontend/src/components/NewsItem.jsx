import React from "react";
import "./NewsItem.css";

const NewsItem = ({ title, ticker, currentPrice, pricePointChange, priceChange, date }) => {
    return (
        <div className="news-item">
            <h3>{title}</h3>
            <div className="news-item-content">
                <div className="ticker-price-box">
                    <div className="ticker-box">{ticker}</div>
                    {priceChange[0] === '+' ? 
                    <div className="price-change-up">
                        <div className="price-change">{currentPrice} {pricePointChange} ({priceChange})</div>
                    </div> : <div className="price-change-down">
                        <div className="price-change">{currentPrice} {pricePointChange} ({priceChange})</div>
                    </div>}
                </div>
                <div className="date-box">{date}</div>
            </div>
        </div>
    );
};

export default NewsItem;