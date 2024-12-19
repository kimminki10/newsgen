import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link, useParams } from "react-router-dom";
import "./NewsList.css";
import NewsItem from "./NewsItem";

const TickerTitleItem = ({ tickerData }) => {
  console.log(tickerData);
  const isUp = tickerData.price_diff > 0;
  const last_price = Math.abs(tickerData.last_price)
  const price_diff = Math.abs(tickerData.price_diff)
  const percentage_diff = Math.abs(tickerData.percentage_diff)
  return (
    <div className="ticker-title-item">
      <div className="ticker-title">{tickerData.ticker_name}</div>
      {isUp ? (
        <div className="price-change-up ticker-title-stock">
          <div>{`${last_price} ▲${price_diff} (${percentage_diff})%`}</div>
        </div>
      ) : (
        <div className="price-change-down ticker-title-stock">
          <div>{`${last_price} ▼${price_diff} (${percentage_diff})%`}</div>
        </div>
      )}
    </div>
  );
}
const NewsList = () => {
  const {ticker} = useParams();
  const [tickerData, setTickerData] = useState({});
  const [articles, setArticles] = useState([]);
  useEffect(() => {
    const fetchTickerData = async () => {
      try {
        const response = await axios.get(`/api/ticker/${ticker}/`);
          const { articles, ...rest } = response.data;
          setTickerData(rest);
          setArticles(articles);
        } catch (error) {
          console.error("Error fetching ticker data:", error);
        }
      };
      fetchTickerData();
  }, [ticker]);

  return (
    <div className="news-list">
      <div className="ticker-info">
        <TickerTitleItem tickerData={tickerData} />
      </div>

      {articles.length !== 0 ?
      articles.map((news) => (
        <NewsItem
                    key={news.id}
                    title={news.title}
                    ticker={ticker}
                    date={tickerData.updated_at}
                    currentPrice={tickerData.last_price}
                    pricePointChange={tickerData.percentage_diff}
                    priceChange={tickerData.price_diff}
                    content={news.content}
                />
      ))
      : 
      <p>No news found for this ticker</p>}
    </div>
  );
};

export default NewsList;
