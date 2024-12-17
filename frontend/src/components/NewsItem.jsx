import React, {useState} from "react";
import { Link } from "react-router-dom";
import "./NewsItem.css";

const NewsItem = ({ title, ticker, currentPrice, pricePointChange, priceChange, date, content }) => {
    const [open, setOpen] = useState(false);
    const handleOpen = () => {
        setOpen(!open);
    }
    return (
        <div className="news-item">
            <h3 onClick={handleOpen}>{title}</h3>
            <div className="news-item-content">
                <div className="ticker-price-box">
                    <Link className="ticker-box" to={`/ticker/${ticker}`}>{ticker}</Link>
                    {priceChange[0] === '+' ? 
                    <div className="price-change-up">
                        <div className="price-change">{currentPrice} {pricePointChange} ({priceChange})</div>
                    </div> : <div className="price-change-down">
                        <div className="price-change">{currentPrice} {pricePointChange} ({priceChange})</div>
                    </div>}
                </div>
                <div className="date-box">{date}</div>
            </div>
            {open && <div className="news-content">{content}</div>}
        </div>
    );
};

export default NewsItem;